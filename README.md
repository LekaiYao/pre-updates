# pre-updates

本项目使用 Beamer 维护 X(3872) / B meson 分析进展报告，并与
XGBoost 训练产出和 Analysis Note（AN）保持数据一致。

## Skills 分工

### `beamer-lxplus`

负责创建、修改、编译和审查 Beamer 源码，适配 lxplus 上的
`pdflatex`、`latexmk` 和 TeX Live 2020 环境。

典型用法：

```text
使用 $beamer-lxplus 更新 slides/main.tex，
加入最新的 XGBoost overtraining 结果并完成编译检查。
```

可用于：

- 创建或重构 Beamer slides；
- 规划章节、页面结构和信息密度；
- 复用现有模板、主题和粒子宏；
- 检查 columns、table、block、TikZ 和文字布局；
- 执行 fastcheck 与完整 latexmk 编译；
- 检查 TeX error、缺失图片、引用和 overflow；
- 以 review、audit、pedagogy、excellence 等模式审查 slides。

只做审查、不修改文件时，可使用：

```text
使用 $beamer-lxplus audit slides/main.tex
```

### 官方 `pdf`

负责完整编译后的 PDF 视觉验收。

典型用法：

```text
使用 $pdf 检查 build/main.pdf 的所有页面，
重点检查裁切、重叠、字体大小和图片可读性。
```

可用于：

- 将 PDF 渲染成 PNG；
- 逐页检查文字、图片或表格裁切；
- 检查 block、图例、公式和图形是否重叠；
- 检查字体、配色和视觉层级的一致性；
- 对比历史 PDF 的版式和信息密度；
- 在交付前验证实际 PDF，而不只依赖 LaTeX 日志。

新安装的 skill 通常从下一轮 Codex 会话开始自动进入可用列表。

## 推荐工作流

```text
核实分析结果及来源
  → 使用 $beamer-lxplus 修改 Beamer 源码
  → bash fastcheck_slides.sh
  → latexmk -pdf -outdir=build slides/main.tex
  → 使用 $pdf 做逐页视觉检查
  → 修正并重新编译
  → 更新 ../docs/progress.md
```

## 与分析端联动

两个 skills 都是通用文档工具，不负责判断本分析的数据是否可信。
分析联动规则继续由项目的 `AGENTS.md` 管理，包括：

- 读取 `../docs/roadmap.md` 确认当前优先级；
- 以 `../docs/ml_results.md` 作为 ML 指标数据源；
- 从 `../AN/` 核实 selection、fit、efficiency 和 systematics；
- 检查 XGBoost 和 AN 图文件是否真实存在；
- 禁止在 slides 中使用无出处或未经验证的数字；
- 发现命名或路径不一致时报告用户；
- 完成一版 slides 后更新 `../docs/progress.md`。

短期内不需要额外创建分析联动 skill。等完整 slides 工作流稳定运行一轮后，
再考虑把重复步骤提炼成 `x-analysis-slides` 等项目专用 skill。

## 项目入口

- `slides/main.tex`：当前 Beamer 主文件；
- `slides/legacy_main.tex`：重构前旧稿；
- `build/main.pdf`：本地完整编译产物，不入库；
- `utils/beamer_setup.tex`：自包含粒子宏；
- `SLIDES_GUIDE.md`：阶段性结论、CMS 用语和标签分级的人工审核规则；
- `REPOSITORY_WORKFLOW.md`：通用 `main` 与各分析长期 branch 的维护方案；
- `docs/bootstrap.md`：当前状态和下一步；
- `AGENTS.md`：项目长期规则和数据联动约束。

## 编译

```bash
bash fastcheck_slides.sh
latexmk -pdf -outdir=build slides/main.tex
```
