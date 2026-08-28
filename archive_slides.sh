#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$repo_root"

default_report_date="$(date +%Y%m%d)"

read -r -p "报告系列（直接回车使用 X）: " report_series
report_series="${report_series:-X}"
read -r -p "汇报日期（YYYYMMDD，直接回车使用 ${default_report_date}）: " report_date
report_date="${report_date:-${default_report_date}}"
read -r -p "额外归档标签（直接回车表示无）: " archive_tag

if [[ ! "${report_series}" =~ ^[A-Za-z][A-Za-z0-9_-]*$ ]]; then
  echo "ERROR: 报告系列必须以字母开头，且只能包含字母、数字、下划线和连字符。" >&2
  exit 2
fi
if [[ ! "${report_date}" =~ ^[0-9]{8}$ ]] || \
   [[ "$(date -d "${report_date}" +%Y%m%d 2>/dev/null || true)" != "${report_date}" ]]; then
  echo "ERROR: 汇报日期必须是有效的 YYYYMMDD 日期。" >&2
  exit 2
fi
if [[ -n "$archive_tag" ]] && [[ ! "$archive_tag" =~ ^[A-Za-z0-9][A-Za-z0-9._-]*$ ]]; then
  echo "ERROR: 标签只能包含字母、数字、点、下划线和连字符，且必须以字母或数字开头。" >&2
  exit 2
fi

report_id="$report_date"
if [[ -n "$archive_tag" ]]; then
  report_id="${report_date}-${archive_tag}"
fi

archive_dir="archive/${report_id}"
published_pdf="pbpb_updates/${report_series}_update_${report_date:2}.pdf"
if [[ -e "$archive_dir" ]]; then
  echo "ERROR: 归档目录已存在：${archive_dir}" >&2
  echo "请重新运行并提供不同标签；脚本不会覆盖已有归档。" >&2
  exit 3
fi
if [[ -z "${archive_tag}" && -e "${published_pdf}" ]]; then
  echo "ERROR: 历史更新 PDF 已存在：${published_pdf}" >&2
  echo "脚本不会覆盖已发布版本；请先核实报告日期和现有文件。" >&2
  exit 3
fi

echo "归档 ID：${report_id}"
echo "运行 slides 构建与检查..."

bash fastcheck_slides.sh
latexmk -pdf -outdir=build slides/main.tex

for required_file in \
  slides/main.tex \
  slides/project_setup.tex \
  build/main.pdf
do
  if [[ ! -f "$required_file" ]]; then
    echo "ERROR: 缺少归档输入：${required_file}" >&2
    exit 4
  fi
done

mkdir -p "$archive_dir"
cp slides/main.tex "$archive_dir/main.tex"
cp slides/project_setup.tex "$archive_dir/project_setup.tex"
cp build/main.pdf "$archive_dir/main.pdf"

echo "归档完成：${archive_dir}"
echo "已保存：main.tex、project_setup.tex、main.pdf"

if [[ -z "${archive_tag}" ]]; then
  mkdir -p pbpb_updates
  cp build/main.pdf "${published_pdf}"
  echo "历史更新 PDF：${published_pdf}"
else
  echo "带标签的临时/补充归档不发布到 pbpb_updates/。"
fi
