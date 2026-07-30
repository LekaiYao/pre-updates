#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

export TEXINPUTS="./utils//:./slides//:./:${TEXINPUTS:-}"
MAIN="${1:-slides/main.tex}"

if [[ ! -f "$MAIN" ]]; then
  echo "Missing TeX source: $MAIN" >&2
  exit 2
fi

# Generate all temporary files in a unique directory
CHECK_DIR=$(mktemp -d /tmp/analysis-slides-fastcheck.XXXXXX)
WRAPPER="$CHECK_DIR/wrapper.tex"
LOG="$CHECK_DIR/pdflatex.log"
cleanup() { rm -rf "$CHECK_DIR"; }
trap cleanup EXIT

cat > "$WRAPPER" <<'LATEX'
\PassOptionsToClass{draft}{beamer}
\AtBeginDocument{%
  \renewcommand{\includegraphics}[2][]{\fbox{\texttt{\detokenize{#2}}}}%
}
LATEX

printf '\\input{%s}\n' "$MAIN" >> "$WRAPPER"

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
  echo "FASTCHECK: pdflatex exited $status (log: $LOG)"
  exit $status
else
  echo "FASTCHECK OK: $MAIN (references/citations are not resolved)"
fi
