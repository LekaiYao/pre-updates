# H015 request：data-driven JJ update 统一 presentation figure package

## Request metadata

- Request ID：`H015`
- Requester / consumer：`pre-updates`
- Producer / fact owner：`JPsiJPsi`
- 状态：`open；用户已批准统一提出图片制作需求`
- 日期：2026-08-29
- Requester copy：`pre-updates/docs/requests/active/H015_JPsiJPsi_data_driven_slide_figure_package.md`
- Producer copy：`JPsiJPsi/docs/requests/active/H015_preupdates_data_driven_slide_figure_package.md`
- Expected answer workspace：`JPsiJPsi/docs/answers/H015_preupdates_data_driven_slide_figures/`
- Accepted physics baseline：H014 accepted package，producer version
  `sync/chensh-20260730@24823a5d476c18aee1f3134e86da645063965ef1`
- Request-start producer state：`sync/chensh-20260730@b89508566a2096bf40e3a99addac7d09fd901e2b`，
  2026-08-29 requester 检查时 tracked worktree clean
- Consumer purpose：约 30 分钟、面向不完全熟悉 JJ 分析的 data-driven SPS/DPS 方法介绍
- Human gate：本 request 的统一制图范围已由用户于 2026-08-29 批准；任何物理定义或数值变化仍需新的用户 gate

## 背景与职责边界

pre-updates 已完成 P1--P7。P8 起需要展示当前 12-cell PP extraction、control-region
normalization、single-J/fit QA、bootstrap 和 method systematic。分析相空间、control region、
fit output 和数值型 diagnostics 由 JPsiJPsi 代码、metadata 和实际输出定义，不再由 slides
侧自行重建分析示意图。

H014 中 `pp_yield_map.pdf` 与 `sps_significance_map.pdf` 的可见标题仍写
`adaptive 14 cells`，与实际 current 12-cell geometry 冲突，已被 consumer 明确排除。
本 request 将这些修正与后续整套 update 的 presentation figures 合并一次提出，避免逐页
建立多个零散 request。

本 request 授权：

- 只基于 H014 accepted machine-readable outputs、fit results、ROOT objects 和 metadata
  重新绘图或制作 presentation-ready summary plots；
- 为现有图修正标题、标签、布局和 stale 12/14-cell 描述；
- 增加纯绘图/汇总代码、figure manifest、metadata 和可复现命令；
- 在不重新拟合的前提下，从已有 fit result / dataset 绘制 fit projections。

本 request 不授权：

- 改变或重新优化 selection、fit model、cell geometry、control region、central scheme、
  bootstrap ensemble、systematic definition 或最终数值；
- 重跑 fit、bootstrap、systematic variations、event production 或 ROOT production；
- 用新计算替代 H014 accepted 数值。若某图不能由现有输出完成，请标记 `blocked` 或
  `needs-new-analysis`，不要自动扩大工作范围。

## 全局绘图要求

所有图统一满足：

- 主交付为 vector PDF，并提供同内容 PNG preview；
- 16:9 slides 中可读：轴标题、legend、cell text 不小于常规 presentation 尺寸；
- 使用 reader-facing physics title；禁止出现 H014/H015、test route、internal nominal、
  global nominal、cross-check、artifact path 等内部状态或协作文字；
- 本 update 的图中不把 MC template fit 标作 “nominal”，也不把 data-driven 标作
  “cross-check”；
- current geometry 必须明确为 12 cells，禁止残留 `adaptive 14 cells`；
- 变量统一写为 `|Delta y|`、`|Delta phi|`、`m(J/psi J/psi)`、`|y(J/psi J/psi)|`；
- 图中数值必须来自随图提交的 machine-readable source，不从 PDF 反抄；
- 每张图提供 title、selection、normalization、weight/error definition、生成脚本、命令、
  Git branch/HEAD、SHA256、生成时间和 caveat。

## 统一图片清单

### F01 — P8：Data prompt-prompt yield map

建议文件名：`pp_yield_map_current12.pdf/png`

- Exact title：`Prompt-prompt yield in Data`
- 使用 H014 current 12-cell `(|Delta y|,|Delta phi|)` geometry；
- 每格显示 `N_PP^i +/- fitted uncertainty`，逐格匹配 accepted `cells.csv` / PP-fit output；
- 标明 12/12 cell fits accepted；不得出现 14-cell title。

### F02 — P9：12-cell geometry and control region

建议文件名：`control_region_geometry_current12.pdf/png`

- Exact title：`Data-driven control region in the 12-cell phase space`
- 只画当前 12-cell 边界并突出单个 CR：
  `1.8 <= |Delta y| < 4.0`、`|Delta phi| <= pi/2`；
- 轴刻度显示 `0, 0.6, 1.2, 1.8, 4.0` 与 `0, pi/2, 3pi/4, pi`；
- 不在 slides 侧重画该 geometry；本图是 geometry/CR 的事实源视觉化。

### F03 — P9/P10：DPS and SPS component maps

建议文件名：`dps_sps_decomposition_current12.pdf/png`，可为两 panel 或两张同风格 PDF。

- Panel titles：`CR-normalized data-derived DPS yield`、`Data-derived SPS residual`；
- DPS 中心值/误差匹配 accepted `dps`/`dps_error`；
- SPS 中心值/误差匹配 accepted `sps`/`sps_error`；
- signed SPS residual 保留，不截断负值；
- 与 F01 使用完全一致的 12-cell geometry、配色和文字格式。

### F04 — P6/P12：single-J fit summary

建议文件名：`single_jpsi_fit_summary.pdf/png`

- Exact title：`Prompt single-J/psi extraction in Data`
- 展示 Jpsi1/Jpsi2 独立 single-J fit 的 mass 与 decay-length projections；
- data、total model、prompt、nonprompt、combinatorial components 可辨认；
- 基于已有 central two-stage fit result，不重新拟合；
- caption/metadata 记录 status、covQual、EDM 和 fitted prompt-yield closure，图内不放内部 route 名。

### F05 — P11/P17：single-J category dependence

建议文件名：`single_jpsi_category_dependence.pdf/png`

- Exact title：`Single-J/psi category dependence`
- 点图/forest plot 展示 current central、`pT=15 GeV` split、`|y|=1.2` split 的
  `f_DPS` 与 signed shift；
- 使用 H014 accepted values：central `0.170423232645`、pT15 `0.171201624240`、
  abs-y1p2 `0.164176471713`；
- 清楚标出 category envelope `+0.000778391595/-0.006246760932`；
- 不把任一 alternative 标为新的 nominal。

### F06 — P15：fixed-500 bootstrap distribution

建议文件名：`bootstrap_fdps_fixed500.pdf/png`

- Exact title：`Full-workflow bootstrap distribution`
- 直方图使用 H014 accepted fixed 500/500 replicas；不使用 H011 500/529 ensemble；
- 标出 current central `0.170423232645`、ensemble mean `0.170392853017`、
  sample SD `0.059331299623`；可同时标 median 和 16/84% quantiles；
- 图或 caption 明确 `500/500 successful replicas; no replacement attempts`；
- histogram bins 必须记录于 metadata，不通过视觉调参暗示额外结论。

### F07 — P16：control-region definition and purity variations

建议文件名：`control_region_variations.pdf/png`

- Exact title：`Control-region definition and purity variations`
- 点图/forest plot 展示 accepted baseline 与 `phi70_zero`、`phi70_purity`、
  `phi110_zero`、`phi110_purity`、`dy2p4_zero_or_purity`；
- central reference 为 `0.170423232645`，数值和 signed shifts 逐项匹配
  `systematic_breakdown.csv`；
- 标出 group envelope `+0.007830845807/-0.006494652437`；
- zero-leakage 与 MC-leakage variants 在 legend 中清楚区分。

### F08 — P18：pure-DPS full-workflow closure

建议文件名：`pure_dps_full_workflow_closure.pdf/png`

- Exact title：`Pure-DPS full-workflow closure`
- 显示 expected `f_DPS=1` 与 recovered `1.037868194160`；
- 清楚展示 relative closure bias `0.037868194160` 如何映射为当前 Data
  absolute uncertainty `0.006453620063`；
- caption 明确该项依赖 current DPS MC 被视作正确的条件。

### F09 — P20：method-systematic breakdown and combination

建议文件名：`method_systematic_breakdown.pdf/png`

- Exact title：`Data-driven method uncertainty`
- 同图展示三个 included groups：single-J category、CR definition/purity、pure-DPS closure；
- 使用 asymmetric signed group values，并展示分别向上/向下 quadrature；
- combined result `+0.010177290968/-0.011083850610`；
- 图中只画 included groups；deferred/diagnostic sources 由 slides coverage table 解释，
  不得把它们画成零误差。

### F10 — focused backup：SPS residual significance map

建议文件名：`sps_significance_map_current12.pdf/png`

- Exact title：`SPS residual significance by cell`
- 使用 current 12-cell geometry，彻底移除 stale 14-cell title；
- signed significance 和 machine source 逐格一致；
- caption 明确 diagnostic only，不能读作 global significance 或额外 systematic。

## 不重复请求的图片与 slides-side 内容

- H014 accepted 的四张 1D projection template-fit PDFs 及 component-yield PDFs 可继续按
  accepted manifest 复用，本 request 不重复生成；
- AN template-fit 输入和 fit-result 图已用于 P2/P3，不在 JPsiJPsi request 中重复；
- 不含分析数据的叙事 workflow、公式、结果对照表、included/deferred coverage matrix、
  thanks 页由 slides 侧排版，不要求 producer 生成装饰性图片。

## 预期交付

请在 `JPsiJPsi/docs/answers/H015_preupdates_data_driven_slide_figures/` 提供：

1. `request.md`：与 requester/producer request copy byte-identical；
2. `answer.md`：逐张图的完成/blocked 状态、直接结论和 caveat；
3. `figure_manifest.csv` 与 `figure_manifest.md`；
4. F01--F10 的 PDF 和 PNG，或对 blocked 项给出精确原因；
5. 每张图对应 machine-readable CSV/JSON；
6. 绘图代码、配置和无歧义复现命令；
7. producer branch/HEAD、tracked dirty files 及其 ownership；
8. package-level SHA256 index。

Producer 完成后将 package 状态设为 `ready`，不得直接设为 `accepted`。pre-updates 将进行
hash、machine source、title、12-cell geometry、数值/误差、可见措辞和 slides-size visual QA；
只有 consumer review 与用户确认均通过后，图片才能进入正式 slides。

## Consumer acceptance criteria

- request copies 与 answer 中 request byte-identical；
- 没有重新拟合、重跑 ensemble 或改变 H014 accepted physics definition/value；
- F01--F03/F10 全部使用 actual current 12-cell geometry，无任何 stale 14-cell title；
- F04 fit projections 对应已接受的两阶段 central fit，QA metadata 闭合；
- F05--F09 数值逐项匹配 H014 accepted machine tables，rounding 不改变含义；
- 每张 PDF/PNG、machine source、代码和 metadata 的 hash/provenance 完整；
- 所有标题和可见文字满足本 update 的 reader-facing/禁用措辞规则；
- presentation 尺寸无裁切、重叠、不可读标签或过密 cell text。
