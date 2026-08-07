# JJ data-driven formal slides：first-draft QA

状态：正式首版已完成，等待用户内容与页面节奏 review。Physics wording 和输入 artifact
均已通过既有 gate；本轮未新增分析结果、fit、bootstrap 或 plot。

## Deck identity

- Source：`slides/main.tex`
- Metadata：`slides/project_setup.tex`
- Build：`build/main.pdf`（ignored，可重建）
- Pages：30（23 页 main，包括 title/thanks；7 页 backup）
- Aspect ratio：16:9
- PDF SHA256：`6e94ce17a663f61b83be2adbebbdff7f9d5c793b990f65a7e57ebd1b871e7643`
- TeX SHA256：`87930da2060df5dcf990c81819706a05f83892fe56a58185a4cafeb2d7770ef2`
- Metadata SHA256：`310420d27d8785248df945058649bad86732b07c6277e39a01817b6f3d8a4491`

## Lifecycle and inputs

- Pre-update deck 已冻结于 `archive/20260807_pre_h011/`；冻结 PDF 为 31 页，SHA256
  `c612050b72e070bf55194e2c513ef043a79f613470cc76a682bb0fc5f97fa087`。
- 新 deck 只复用项目 theme/macros、title-page geometry 和 centered thanks-box format；
  旧正文与 backup 未保留在新 `main.tex`。
- H011 16 个新 PDF 已复制到 `slides/figures/accepted/H011/`；逐项 SHA256 与 accepted
  figure manifest 匹配。
- H011/H012 的 13 个 machine-readable/provenance 文件已复制到
  `slides/data/accepted/H011/`；stale nominal-comparison PDF 未复制、未引用。
- Historical recap/backup 仅使用已 accepted 的 `slides/figures/accepted/H006/` 输入。

## Content coverage

- Main：4 页 recap、5 页方法升级、3 张 central maps、6 张 major-support projections、
  category/CR breakdown、500-success bootstrap `stat`、provisional `syst`、CMS nominal
  comparison、takeaways 和 thanks。
- Backup：central weights、signed-cell diagnostic、剩余 pair-kinematic yields、DPS-MC
  benchmark、historical validation、previous uncertainty machinery、bootstrap policy。
- 当前结果始终称 data-driven internal central/cross-check；只在最后与 CMS MC-template
  nominal 比较。Category 与 CR 来源分别展示后再做用户批准的 quadrature。
- Bootstrap 页和结论页均保留 500/529、29 failures 和 conditional-selection caveat。
- TeX 可见正文不含独立内部协作编号。

## Verification

- `bash fastcheck_slides.sh`：passed。
- `latexmk -pdf -outdir=build slides/main.tex`：passed，30 页。
- Warning audit：0 overfull、0 underfull、0 undefined control/citation、0 fatal error。
- `python3 scripts/check_tex_internal_ids.py --all`：passed。
- `bash fastcompile_frame.sh title`、`thanks`、`p21`：均生成单页 PDF/PNG，passed。
- Poppler 将 30 页全部渲染为 PNG；三组 contact-sheet review 和关键 P21 focused review
  未发现裁切、图文重叠、框内溢出、不可读 glyph 或错误旋转。
- Beamer quality-loop self-score：95/100；满足正式首版交付阈值。保留用户对页面节奏、
  标题措辞和主文/backup 分配的 review，不将其视为物理 gate。
