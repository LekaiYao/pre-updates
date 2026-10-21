#!/usr/bin/env python3
"""Check literal internal IDs in slide sources; this is not a TeX interpreter."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

CONFIG = ".tex-internal-ids.json"
HUNK = re.compile(r"^@@ -[0-9]+(?:,[0-9]+)? \+([0-9]+)(?:,([0-9]+))? @@")
COMMAND = re.compile(r"\\([A-Za-z@]+)\*?|\\.")
# Only the first mandatory argument is hidden. Display text in later arguments
# (e.g. \href{target}{text}) and citation notes remains subject to checking.
HIDDEN_ARGUMENT = {
    "includegraphics", "pgfimage", "includepdf", "graphicspath",
    "input", "include", "bibliography", "addbibresource", "label",
    "ref", "pageref", "eqref", "autoref", "cref", "Cref",
    "cite", "citep", "citet", "nocite", "href", "hyperlink", "hypertarget",
}
HIDDEN_OPTIONS = {"includegraphics", "pgfimage", "includepdf", "addbibresource", "label"}


def git(*args: str) -> str:
    return subprocess.run(
        ["git", *args], check=True, stdout=subprocess.PIPE,
        stderr=subprocess.PIPE, encoding="utf-8", errors="surrogateescape",
    ).stdout


def load_pattern(config: str) -> re.Pattern | None:
    data = json.loads(config)
    if not isinstance(data, dict) or set(data) != {"prefixes"}:
        raise ValueError('configuration must contain only a "prefixes" list')
    prefixes = data["prefixes"]
    if not isinstance(prefixes, list) or any(
        not isinstance(p, str) or re.fullmatch(r"[A-Za-z]+", p) is None
        for p in prefixes
    ):
        raise ValueError("prefixes must be a list of nonempty ASCII-letter strings")
    if not prefixes:
        return None
    alternatives = "|".join(re.escape(p) for p in sorted(set(prefixes), key=len, reverse=True))
    return re.compile(r"(?<![A-Za-z0-9_])(?:" + alternatives + r")[0-9]+(?![A-Za-z0-9_])")


def blank(chars: list[str], start: int, end: int) -> None:
    # Preserve positions and newlines for useful source diagnostics.
    for i in range(start, end):
        if chars[i] not in "\r\n":
            chars[i] = " "


def without_comments(text: str) -> str:
    chars = list(text)
    i = 0
    while i < len(text):
        if text[i] == "\\":
            i += 2  # An escaped percent is visible; \\ followed by % is not.
        elif text[i] == "%":
            end = text.find("\n", i)
            if end < 0:
                end = len(text)
            blank(chars, i, end)
            i = end
        else:
            i += 1
    return "".join(chars)


def group_end(text: str, start: int) -> int | None:
    """End of a balanced {...} or [...] group, allowing nested/escaped braces."""
    pairs = {"{": "}", "[": "]"}
    stack = [pairs[text[start]]]
    i = start + 1
    while i < len(text):
        ch = text[i]
        if ch == "\\":
            i += 2
            continue
        if ch == "{" or (ch == "[" and stack[-1] == "]"):
            stack.append(pairs[ch])
        elif ch == stack[-1]:
            stack.pop()
            if not stack:
                return i + 1
        i += 1
    return None


def skip_space(text: str, pos: int) -> int:
    while pos < len(text) and text[pos].isspace():
        pos += 1
    return pos


def visible_source(text: str) -> str:
    text = without_comments(text)
    chars = list(text)
    # Full documents: check body only. Fragments: check the entire source.
    start = re.search(r"\\begin\s*\{document\}", text)
    if start:
        blank(chars, 0, start.end())
        end = re.search(r"\\end\s*\{document\}", text[start.end():])
        if end:
            blank(chars, start.end() + end.start(), len(text))
    for match in COMMAND.finditer(text):
        if chars[match.start()] == " ":
            continue
        name = match.group(1)
        blank(chars, match.start(), match.end())
        pos = skip_space(text, match.end())
        # Skip non-rendered options; retain e.g. cite prenotes/postnotes.
        while pos < len(text) and text[pos] == "[":
            end = group_end(text, pos)
            if end is None:
                break
            if name in HIDDEN_OPTIONS or name == "hyperref":
                blank(chars, pos, end)
            pos = skip_space(text, end)
        if pos >= len(text) or text[pos] != "{":
            continue
        end = group_end(text, pos)
        if end is None:
            continue
        if name in HIDDEN_ARGUMENT or name in {"begin", "end"}:
            blank(chars, pos, end)
        if name == "begin" and text[pos + 1:end - 1] == "frame":
            pos = skip_space(text, end)
            if pos < len(text) and text[pos] == "[":
                end = group_end(text, pos)
                if end is not None:
                    blank(chars, pos, end)
    return "".join(chars)


def scan(path: str, text: str, selected: set[int] | None, pattern: re.Pattern):
    findings = []
    for number, line in enumerate(visible_source(text).splitlines(), 1):
        if selected is not None and number not in selected:
            continue
        ids = sorted(set(pattern.findall(line)))
        if ids:
            findings.append((path, number, ids, line.strip()))
    return findings


def staged_files() -> list[str]:
    return [p for p in git("diff", "--cached", "--name-only", "-z", "--diff-filter=ACMR").split("\0")
            if p.startswith("slides/") and p.endswith(".tex")]


def added_lines(path: str) -> set[int]:
    diff = git("diff", "--cached", "--unified=0", "--no-color", "--no-ext-diff",
               "--no-textconv", "--", path)
    selected = set()
    number = None
    for line in diff.splitlines():
        hunk = HUNK.match(line)
        if hunk:
            number = int(hunk.group(1))
        elif number is not None:
            if line.startswith("+"):
                selected.add(number)
                number += 1
            elif line.startswith(" "):
                number += 1
    return selected


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--staged", action="store_true", help="check added lines from Git's index")
    mode.add_argument("--all", action="store_true", help="check all slides/**/*.tex in the worktree")
    parser.add_argument("--config", default=CONFIG, help="repository-relative JSON configuration")
    args = parser.parse_args()
    try:
        os.chdir(git("rev-parse", "--show-toplevel").strip())
        config_path = Path(args.config)
        if config_path.is_absolute() or ".." in config_path.parts:
            raise ValueError("--config must be a path within the repository")
        config = git("show", f":{config_path.as_posix()}") if args.staged else config_path.read_text(encoding="utf-8")
        pattern = load_pattern(config)
        if pattern is None:
            print("TeX internal-ID check inactive: configure prefixes in " + args.config)
            return 0
        findings = []
        if args.staged:
            for path in staged_files():
                findings.extend(scan(path, git("show", f":{path}"), added_lines(path), pattern))
        else:
            for path in sorted(Path("slides").rglob("*.tex")):
                findings.extend(scan(str(path), path.read_text(encoding="utf-8"), None, pattern))
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        detail = exc.stderr.strip() if isinstance(exc, subprocess.CalledProcessError) else str(exc)
        print("ERROR: internal-ID check could not run: " + detail, file=sys.stderr)
        return 2
    if not findings:
        print("TeX internal-ID check OK")
        return 0
    print("ERROR: internal collaboration IDs in slide text:", file=sys.stderr)
    for path, number, ids, line in findings:
        print(f"  {path}:{number}: {', '.join(ids)}: {line}", file=sys.stderr)
    print("Rewrite the passage using reader-facing terminology; keep internal IDs in comments or provenance.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
