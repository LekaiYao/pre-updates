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
