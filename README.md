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
figures/logos/            通用机构 logo 资产与命名索引
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
封面参与者、reporter、日期及实际显示的 logo 均在 `slides/project_setup.tex`
按分析填写；`main` 只提供匿名占位符、通用几何和 logo 资产库，不预设参与机构。

## 构建

```bash
bash fastcheck_slides.sh
latexmk -pdf -outdir=build slides/main.tex
```

构建后使用官方 `pdf` skill 对 `build/main.pdf` 做逐页视觉检查。

## 内部协作编号检查

首次 checkout 后启用版本化提交检查：

```bash
git config core.hooksPath .githooks
```

各分析在 `.tex-internal-ids.json` 配置自己的编号前缀，例如：

```json
{"prefixes": ["REQ", "TASK"]}
```

这会检查独立的 `REQ12`、`TASK3` 等字面编号；前缀区分大小写，只允许英文字母，
后接数字。main 的默认列表为空，检查会明确报告尚未启用；通用模板不预设分析的
denylist。配置文件应纳入版本管理。

`pre-commit` 只检查 Git 暂存区中 `slides/**/*.tex` 新增的行，并使用暂存区的配置。
未暂存的源码或配置修改不会替代待提交内容。配置缺失或格式错误会阻止提交；首次启用
或修改前缀后，还应手动做一次全量检查：

```bash
python3 scripts/check_tex_internal_ids.py --all
python3 -B -m unittest discover -s tests -v
```

检查覆盖完整文档正文和没有 document 环境的 TeX 片段，保留准确行号。
它跳过注释、常用图片/输入/引用命令的路径或标识参数、frame 的选项；
标题、图注和超链接的可见文字仍会检查。命中后须重写对应语句，不能只删掉编号而丢失上下文。

这是字面源码检查，不执行 TeX 宏展开、不解析自定义命令或条件分支，也不读取图片/PDF
中的文字；完整文档的导言区不扫描。它可能对未使用的片段或宏定义报出结果，不能代替
最终 PDF 的人工检查。迁移到已有分析分支时，应保留该分支的编号前缀和局部规则。

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
3. 从 `figures/logos/` 选择与参与者 affiliation 对应的 logo；
4. 加入分析局部宏和权威来源说明；
5. 用已核实内容替换 demo frames；
6. 每个叙事单元后起草并人工审核 `Interim conclusion`；
7. 运行 fastcheck、完整编译和逐页 PDF 检查。

更新既有分析 deck 时，还应遵守 `SLIDES_GUIDE.md` 的两层计划、从零更新、
artifact 复用和人工批准版式规则。
