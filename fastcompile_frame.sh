#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${repo_root}"

frame_label=${1:-}
if [[ -z "${frame_label}" ]]; then
  echo "Usage: bash fastcompile_frame.sh <frame-label>" >&2
  exit 2
fi
if [[ ! "${frame_label}" =~ ^[A-Za-z0-9_-]+$ ]]; then
  echo "Invalid frame label: ${frame_label}" >&2
  exit 2
fi

frame_outdir="tmp/${frame_label}"
mkdir -p "${frame_outdir}"

export TEXINPUTS="../AN/utils/general//:./utils//:./:"
pdflatex \
  -interaction=nonstopmode \
  -halt-on-error \
  -output-directory="${frame_outdir}" \
  -jobname="frame-${frame_label}" \
  "\\def\\onlyframes{${frame_label}}\\input{slides/main.tex}" >/dev/null

# A second pass resolves remember-picture/overlay coordinates used by some frames.
pdflatex \
  -interaction=nonstopmode \
  -halt-on-error \
  -output-directory="${frame_outdir}" \
  -jobname="frame-${frame_label}" \
  "\\def\\onlyframes{${frame_label}}\\input{slides/main.tex}" >/dev/null

pdftoppm \
  -png \
  -singlefile \
  -r 150 \
  "${frame_outdir}/frame-${frame_label}.pdf" \
  "${frame_outdir}/frame-${frame_label}" >/dev/null 2>&1

echo "PDF: ${frame_outdir}/frame-${frame_label}.pdf"
echo "PNG: ${frame_outdir}/frame-${frame_label}.png"
