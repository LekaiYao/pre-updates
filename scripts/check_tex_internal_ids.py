#!/usr/bin/env python3
"""Reject standalone internal workflow/comment IDs in user-facing TeX body."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
PATTERN = re.compile(r"(?<![A-Za-z0-9_])(?:H|A|B)[0-9]+(?![A-Za-z0-9_])")


def tex_body(line: str) -> str:
    """Remove unescaped TeX comments before applying the body-text policy."""
    return re.split(r"(?<!\\)%", line, maxsplit=1)[0]


requested = [Path(arg) for arg in sys.argv[1:]]
targets = requested or sorted((ROOT / "slides").rglob("*.tex"))
violations: list[str] = []

for target in targets:
    path = target if target.is_absolute() else ROOT / target
    if not path.is_file():
        continue
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        body = tex_body(line)
        if PATTERN.search(body):
            violations.append(f"{path.relative_to(ROOT)}:{lineno}: {body.strip()}")

if violations:
    print(
        "INTERNAL-ID CHECK FAILED: rewrite standalone H/A/B-number labels in TeX body.",
        file=sys.stderr,
    )
    print("\n".join(violations), file=sys.stderr)
    raise SystemExit(1)

print("INTERNAL-ID CHECK OK: no standalone H/A/B-number labels in TeX body")
