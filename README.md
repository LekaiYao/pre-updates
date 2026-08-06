# Analysis Slides

个人维护的 Beamer 分析进展项目。`main` 保存可复用框架，每个具体分析使用
`analysis/<name>` 长期 branch。当前通用框架面向 lxplus、TeX Live 2020 和
`pdflatex`，不依赖任一分析目录或外部 Analysis Note。

## Branch 模型

```text
main          通用框架、构建、视觉 QA 和内容治理
analysis/x    X-specific slides、数字、图片路径和术语
analysis/jj   JJ-specific slides、数字、图片路径和术语
```

完整协作规则见 `REPOSITORY_WORKFLOW.md`。内容审核规则见
`SLIDES_GUIDE.md`。

## 文件结构

```text
slides/main.tex           可独立编译的最小示例
slides/project_setup.tex  branch-local metadata 入口
utils/theme_setup.tex     通用主题和语义颜色
utils/common_macros.tex   通用布局与 conclusion helper
utils/beamer_setup.tex    可选 HEP 粒子和 collider 宏
fastcheck_slides.sh       快速语法检查
fastcompile_frame.sh      单页排版快速编译与 PNG 渲染
archive_slides.sh         极简 slides 归档
latexmkrc                 本地 TeX 搜索路径
```

`main` 中的文字和状态均为 demo，不是物理结果。新分析从 `main` 创建 branch
后，必须替换 metadata 和 demo 内容，并指定该分析的权威数据与术语来源。

## 构建

```bash
bash fastcheck_slides.sh
latexmk -pdf -outdir=build slides/main.tex
```

构建后使用官方 `pdf` skill 对 `build/main.pdf` 做逐页视觉检查。

## 本地提交 hook

本仓库使用版本化 hook，首次 checkout 后启用：

```bash
git config core.hooksPath .githooks
```

`pre-commit` 只检查 `slides/**/*.tex` 本次 staged 新增的可见正文。若出现独立的
`H{编号}`、`A{编号}`、`C{编号}`，提交会失败；应将对应文本重写为面向听众的
物理或方法表述。TeX 注释、artifact 路径、输入文件和 label 不属于渲染正文。

完整扫描可手动运行：

```bash
python3 scripts/check_tex_internal_ids.py --all
```

## 单页排版迭代

为目标 frame 设置稳定的 `label` 后运行：

```bash
bash fastcompile_frame.sh demo-title
```

脚本只编译该 frame，执行两次 `pdflatex` 以解析 overlay 坐标，并生成：

```text
tmp/demo-title/frame-demo-title.pdf
tmp/demo-title/frame-demo-title.png
```

人工逐页调整期间只运行单页编译；页面确认后再执行一次完整构建。`tmp/` 不入库，
一轮 slides 正式收尾后清理。脚本不包含分析项目的外部路径，额外 TeX 搜索路径由
项目环境或 `TEXINPUTS` 提供。

## 极简归档

完成一版 slides 并通过视觉检查后运行：

```bash
bash archive_slides.sh
```

脚本会在归档前询问是否增加标签。直接回车时使用日期作为 report ID，例如
`20260730`；输入 `test` 时使用 `20260730-test`。归档目录包含：

```text
archive/<report-id>/
├── main.tex
├── project_setup.tex
└── main.pdf
```

脚本会先运行 fastcheck 和完整 `latexmk` 构建，再复制当前源码与编译结果。
已有的归档目录不会被覆盖。该机制假设仓库中的通用 TeX 配置以及 slides 引用
的图片路径和内容保持可用，不以完全封闭的环境复现为目标。

## Skills 分工

- `beamer-lxplus`：修改 Beamer 源码、fastcheck、完整编译和结构审查；
- 官方 `pdf`：渲染最终 PDF，检查裁切、重叠、字号和图形可读性。

skills 不判断分析数字是否可信。数据溯源、AN 用语和内部标签 denylist 由各
分析 branch 的规则维护。

## 新分析的最小流程

1. 从 `main` 创建 `analysis/<name>`；
2. 修改 `slides/project_setup.tex`；
3. 加入分析局部宏和权威来源说明；
4. 用已核实内容替换 demo frames；
5. 每个叙事单元后起草并人工审核 `Interim conclusion`；
6. 运行 fastcheck、完整编译和逐页 PDF 检查。

更新既有分析 deck 时，还应遵守 `SLIDES_GUIDE.md` 的两层计划、从零更新、
artifact 复用和人工批准版式规则。
