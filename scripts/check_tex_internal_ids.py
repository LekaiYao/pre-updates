#!/usr/bin/env python3
"""Reject internal collaboration IDs added to rendered slide text."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


INTERNAL_ID = re.compile(
    r"(?<![A-Za-z0-9_])(?:H|A|C)[0-9]+(?![A-Za-z0-9_])"
)
HUNK = re.compile(r"^@@ -[0-9]+(?:,[0-9]+)? \+([0-9]+)(?:,([0-9]+))? @@")
NON_RENDERED_COMMAND = re.compile(
    r"""\\(?:includegraphics(?:\[[^\]]*\])?|input|include|bibliography|addbibresource|label)\s*\{[^{}]*\}"""
)


def run_git(*args: str) -> str:
    return subprocess.run(
        ["git", *args],
        check=True,
        text=True,
        stdout=subprocess.PIPE,
    ).stdout


def staged_tex_files() -> list[str]:
    names = run_git(
        "diff", "--cached", "--name-only", "--diff-filter=ACMR"
    ).splitlines()
    return [
        name
        for name in names
        if name.startswith("slides/") and name.endswith(".tex")
    ]


def staged_text(path: str) -> str:
    return run_git("show", f":{path}")


def added_line_numbers(path: str) -> set[int]:
    diff = run_git("diff", "--cached", "--unified=0", "--no-color", "--", path)
    added: set[int] = set()
    new_line: int | None = None
    for raw in diff.splitlines():
        match = HUNK.match(raw)
        if match:
            new_line = int(match.group(1))
            continue
        if new_line is None or raw.startswith("---") or raw.startswith("+++"):
            continue
        if raw.startswith("+"):
            added.add(new_line)
            new_line += 1
        elif raw.startswith("-"):
            continue
        elif raw.startswith(" "):
            new_line += 1
    return added


def strip_comment(line: str) -> str:
    escaped = False
    for index, char in enumerate(line):
        if char == "%" and not escaped:
            return line[:index]
        if char == "\\":
            escaped = not escaped
        else:
            escaped = False
    return line


def rendered_body_lines(text: str):
    in_document = False
    for line_number, raw in enumerate(text.splitlines(), start=1):
        if r"\begin{document}" in raw:
            in_document = True
            continue
        if r"\end{document}" in raw:
            break
        if not in_document:
            continue
        visible = strip_comment(raw)
        visible = NON_RENDERED_COMMAND.sub("", visible)
        yield line_number, visible


def scan(path: str, text: str, selected_lines: set[int] | None):
    findings = []
    for line_number, visible in rendered_body_lines(text):
        if selected_lines is not None and line_number not in selected_lines:
            continue
        matches = sorted(set(INTERNAL_ID.findall(visible)))
        if matches:
            findings.append((path, line_number, matches, visible.strip()))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check rendered slide text for internal collaboration IDs."
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--staged", action="store_true", help="check staged added lines")
    mode.add_argument("--all", action="store_true", help="check all slides TeX body lines")
    args = parser.parse_args()

    findings = []
    if args.staged:
        for path in staged_tex_files():
            findings.extend(scan(path, staged_text(path), added_line_numbers(path)))
    else:
        for path in sorted(Path("slides").rglob("*.tex")):
            findings.extend(scan(str(path), path.read_text(), None))

    if not findings:
        print("TeX internal-ID check OK")
        return 0

    print(
        "ERROR: internal collaboration IDs are forbidden in rendered slide text.",
        file=sys.stderr,
    )
    for path, line_number, matches, visible in findings:
        print(
            f"  {path}:{line_number}: {', '.join(matches)}: {visible}",
            file=sys.stderr,
        )
    print(
        "Rewrite each affected passage with reader-facing physics wording; "
        "keep internal IDs only in comments or provenance files.",
        file=sys.stderr,
    )
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
