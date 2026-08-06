#!/usr/bin/env bash
# ================================================================
# fastcheck_slides.sh — Fast LaTeX syntax check for beamer slides
#
# Pattern: same approach as AN/fastcheck.sh — wrapper injection
# + pdflatex -draftmode for sub-second pass.
#
# Usage:
#   bash fastcheck_slides.sh                 # check slides/main.tex
#   bash fastcheck_slides.sh slides/foo.tex  # check specific file
#
# Full build:
#   latexmk -pdf slides/main.tex
# ================================================================
set -euo pipefail
cd "$(dirname "$0")"

# project root (.) needed for \input{../utils/beamer_setup.tex} resolution
# when main.tex is \input from a /tmp wrapper
export TEXINPUTS="../AN/utils/general//:./utils//:./:${TEXINPUTS:-}"
MAIN="${1:-slides/main.tex}"

if [[ ! -f "$MAIN" ]]; then
  echo "Missing TeX source: $MAIN" >&2
  exit 2
fi

# Content-policy hook: analysis-internal handoff labels must not enter slide body.
python3 scripts/check_tex_internal_ids.py "$MAIN"

# Generate all temporary files in a unique directory
CHECK_DIR=$(mktemp -d /tmp/slides_fastcheck.XXXXXX)
WRAPPER="$CHECK_DIR/wrapper.tex"
LOG="$CHECK_DIR/pdflatex.log"
cleanup() { rm -rf "$CHECK_DIR"; }
trap cleanup EXIT

cat > "$WRAPPER" <<'LATEX'
% --- Local fastcheck injections for beamer slides ---
% beamer loads graphicx internally, so pass draft to the class
\PassOptionsToClass{draft}{beamer}       % figures → empty boxes (speed)
% Override \includegraphics to avoid slow EOS file lookups during fastcheck
\AtBeginDocument{%
  \renewcommand{\includegraphics}[2][]{\fbox{\texttt{\detokenize{#2}}}}%
}
% --- End of injections ---
LATEX

printf '\\input{%s}\n' "$MAIN" >> "$WRAPPER"

# Single-pass fast check (no refs/cites resolution, no PDF output)
set +e
pdflatex -draftmode -interaction=nonstopmode -halt-on-error \
  -output-directory="$CHECK_DIR" -jobname=check "$WRAPPER" >"$LOG" 2>&1
status=$?
set -e

if grep -qiE "^!|LaTeX Error|Fatal error|Undefined control sequence" "$LOG"; then
  echo "FASTCHECK: LaTeX errors found:"
  grep -iE "^!|LaTeX Error|Fatal error|Undefined control sequence" "$LOG" | head -15
  exit 1
elif [ $status -ne 0 ]; then
  echo "FASTCHECK: pdflatex exited $status (see "$LOG")"
  exit $status
else
  echo "FASTCHECK OK: $MAIN (refs/cites unresolved in single pass)"
fi
