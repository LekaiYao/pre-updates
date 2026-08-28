#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${repo_root}"

part_name=${1:-}
frame_labels=${2:-}
part_source=${3:-}
if [[ -z "${part_name}" || -z "${frame_labels}" ]]; then
  echo "Usage: bash fastcompile_frame.sh <part-name> <frame-label[,frame-label,...]> [part-source.tex]" >&2
  exit 2
fi
if [[ ! "${part_name}" =~ ^p[0-9]+[A-Za-z0-9_-]*$ && ! "${part_name}" =~ ^backup_[A-Za-z0-9_-]+$ ]]; then
  echo "Invalid part name (must start with p{n}, or backup_ for provisional backup groups): ${part_name}" >&2
  exit 2
fi
if [[ ! "${frame_labels}" =~ ^[A-Za-z0-9_-]+(,[A-Za-z0-9_-]+)*$ ]]; then
  echo "Invalid frame label list: ${frame_labels}" >&2
  exit 2
fi
if [[ -n "${part_source}" ]]; then
  if [[ ! "${part_source}" =~ ^slides/sections/[A-Za-z0-9_./-]+\.tex$ ]]; then
    echo "Invalid part source: ${part_source}" >&2
    exit 2
  fi
  if [[ ! -f "${part_source}" ]]; then
    echo "Missing part source: ${part_source}" >&2
    exit 2
  fi
  preview_definition="\\def\\previewpart{${part_source}}"
else
  preview_definition=""
fi

frame_outdir="tmp/${part_name}"
frame_jobname="preview"
mkdir -p "${frame_outdir}"

export TEXINPUTS="../AN/utils/general//:./utils//:./:"
pdflatex \
  -interaction=nonstopmode \
  -halt-on-error \
  -output-directory="${frame_outdir}" \
  -jobname="${frame_jobname}" \
  "\\def\\onlyframes{${frame_labels}}${preview_definition}\\input{slides/main.tex}" >/dev/null

# A second pass resolves remember-picture/overlay coordinates used by some frames.
pdflatex \
  -interaction=nonstopmode \
  -halt-on-error \
  -output-directory="${frame_outdir}" \
  -jobname="${frame_jobname}" \
  "\\def\\onlyframes{${frame_labels}}${preview_definition}\\input{slides/main.tex}" >/dev/null

# Keep one stable preview location and remove stale page images from a
# previously compiled frame group.
find "${frame_outdir}" -maxdepth 1 -type f -name "${frame_jobname}-*.png" -delete
pdftoppm \
  -png \
  -r 150 \
  "${frame_outdir}/${frame_jobname}.pdf" \
  "${frame_outdir}/${frame_jobname}" >/dev/null 2>&1

echo "Part: ${part_name}"
echo "Frames: ${frame_labels}"
if [[ -n "${part_source}" ]]; then
  echo "Draft source: ${part_source}"
fi
echo "PDF: ${frame_outdir}/${frame_jobname}.pdf"
echo "PNG: ${frame_outdir}/${frame_jobname}-*.png"
