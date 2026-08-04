> Lifecycle: archived on 2026-08-02. Producer request work is complete; the still-ready H007 artifact handoff is tracked only in shared `../../../../docs/progress.md` and awaits user confirmation.

# H007 request：修正 H006 二维分解图的误差显示与标签

## Request metadata

- Request ID：`H007`
- Producer：`JPsiJPsi`
- Consumer：`pre-updates`
- 关联 artifact：`H006`
- 状态：`ready；consumer validation passed；awaiting user confirmation`
- 请求日期：2026-07-31

## 背景与已确认问题

当前 `pre-updates/build/main.pdf` 的 P5--P9 使用 H006 accepted artifact。
对 producer 的 machine-readable outputs 和绘图实现核对后，确认中心值与二维分解
定义一致，但部分 PDF 的 `TH2Poly` 误差文字不能按统计误差解释：

1. `dps_normalized_map.pdf` 中出现数千量级的 `±` 数值。它们与缩放前
   mixed-pair error 相符，而不是归一化后 DPS yield 的 `dps_error`。
   例如图中 `47.21 ± 3392.98`，对应 `cells.csv` 的正确归一化结果应为
   `47.2069 ± 5.0068`。
2. `sps_data_driven_map.pdf` 中的 `±0.00` 及其他误差存在错位，不能代表
   `cells.csv` 中的 `sps_error`。例如 `1852.9732` 的正确误差为
   `48.8977`。
3. `sps_weight_map.pdf` 和 `dps_weight_map.pdf` 没有显式设置逐格 weight
   uncertainty；当前 `TEXT E` 显示的数值符合 ROOT 默认
   `sqrt(bin content)`，例如 `sqrt(0.87)≈0.93`，不具有统计意义。
4. `marginals_weighted.pdf` 的右图横轴显示 signed `y(J/psi)`，而正文指标写作
   `D(|y|)`；需要统一所画变量与指标标签。

## 请求目标

请在 `JPsiJPsi/tests/atlas_data_driven_sps/` 代码侧修正并重新生成适合 slides
展示的 P5--P9 图。不得改变已经确认的 selection、二维分 bin、control region、
event-mixing、SPS/DPS 分解或中心值定义。

### A. P5：event-mixing marginal validation

修正 `marginals_weighted.pdf` 的变量/标签一致性：

- 若右图画 signed `y(J/psi)`，则图中文字和距离指标使用同一 signed-y 定义；
- 若保留 `D(|y|)`，则右图横轴和分布也改为 `|y(J/psi)|`；
- 图内明确 Data 与 mixed sample 均为 normalized shape；
- 保留 Data 2492 selected pair candidates、5M cross-event mixed pairs 的现有口径。

### B. P6：Data prompt-prompt yield map

重新生成或确认 `pp_yield_map.pdf`：

- 每格显示 `N_PP^i ± fitted uncertainty`；
- 数值必须逐格匹配 `fit_results.csv` 的 `pp_yield` 和 `pp_error`；
- 图名/标题明确为 Data prompt-prompt fitted yield；
- 保留 14-cell adaptive binning 和当前坐标定义。

### C. P7：normalized mixed-DPS yield map

修正 `dps_normalized_map.pdf`：

- 每格中心值匹配 `cells.csv` 的 `dps`；
- 若显示误差，必须匹配 `cells.csv` 的 `dps_error`，并正确包含
  control-region normalization 的相关传播；
- 不得显示缩放前的 `mix_pair_error`；
- 若二维图无法可靠展示相关误差，则完全移除逐格 `±`，并在 metadata 中说明
  uncertainty 由 joint statistical propagation 处理。

### D. P8：data-driven SPS yield map

修正 `sps_data_driven_map.pdf`：

- 每格中心值匹配 `cells.csv` 的 `sps = data - dps`；
- 若显示误差，必须匹配 `cells.csv` 的 `sps_error`；
- 唯一负格保留 signed central value，不截断为零；
- 图或 metadata 保留该格与零相容的说明，当前 nominal 数值约为
  `-0.999 ± 6.058`，即 `-0.165 sigma`；
- 不得继续显示错位的 `±0.00` 或其他对象的 bin error。

### E. P9：SPS/DPS weight maps

修正 `sps_weight_map.pdf` 和 `dps_weight_map.pdf`：

- 中心值分别匹配 `cells.csv` 的 `weight_sps` 和 `weight_dps`；
- 保持逐格 `w_SPS + w_DPS = 1`；
- 禁止将 ROOT 默认 `sqrt(bin content)` 显示为 weight uncertainty；
- 推荐当前版本只显示中心值，不显示 `±`；
- 如果 producer 决定显示 uncertainty，必须使用完整相关传播，至少包含
  Data PP yield covariance、control-region normalization、source-event
  bootstrap covariance以及比值分子/分母相关性，并提供 machine-readable 数表。

## 预期输出

请在 producer 项目中提供：

1. 修正后的五类 PDF：
   - `marginals_weighted.pdf`
   - `pp_yield_map.pdf`
   - `dps_normalized_map.pdf`
   - `sps_data_driven_map.pdf`
   - `sps_weight_map.pdf`
   - `dps_weight_map.pdf`
2. 对应 machine-readable values；现有 CSV 可复用，但需明确每张图使用的字段。
3. metadata/summary，逐图说明：
   - 图中变量与归一化；
   - 中心值字段；
   - `±` 的定义，或为什么不显示逐格误差；
   - 生成脚本、配置和 Git commit。
4. producer 完成数值核对和视觉检查后，将新 artifact 登记为 `ready`，不要直接
   标记为 `accepted`。

## Consumer 验收条件

`pre-updates` 将在 artifact 为 `ready` 后执行：

1. 逐格核对 PDF 中心值与 CSV；
2. 如图中保留 `±`，逐格核对其字段和传播定义；
3. 检查 P5 的变量与 CDF 指标一致；
4. 检查 P7--P9 不再出现数千量级错配、`±0.00` 错位或 `sqrt(weight)`；
5. 完成 slides 展示尺寸下的视觉检查；
6. 将验收结论提交用户确认。只有用户确认后才标记 `accepted` 并替换 slides。

## Slides 后续更新要求

新图通过 `ready -> consumer 验收 -> user confirmation -> accepted` 后，
`pre-updates` 才执行以下更新：

- 替换 P5--P9 对应图片；
- 为每张图在 slides 正文中写出清晰图名；
- 每张图增加一句简短含义说明：
  - P5：mixing 保持单个 J/psi marginal shape；
  - P6：逐格 mass-lifetime fit 得到 Data PP yield；
  - P7：control-region 归一化后的 mixed-DPS yield；
  - P8：Data PP 减去 DPS 得到 data-driven SPS yield；
  - P9：二维分解得到逐格 SPS/DPS component weights；
- 重新完整编译，检查 LaTeX warnings，并逐页视觉 QA。

## 职责边界与 human physics gate

- `JPsiJPsi` 负责分析代码、误差定义、数值产物与 producer metadata。
- `pre-updates` 只负责 artifact 验收、slides 引用、图名/解释文字和视觉 QA。
- 本 request 只修正显示和可解释性，不授权修改 selection、fit、nominal、
  systematics 或最终数值。
- 任何物理定义或最终数值变化必须单独提交用户确认。


## Consumer validation evidence（2026-07-31）

- Producer artifact：`../JPsiJPsi/tests/atlas_data_driven_sps/results/h007_fixed_2d_maps/`
- Producer commit：`35e036994841f7f0100d5dd36c32464e7ef235e0`
- `cells.csv` 与 H006 nominal `templates_2d_adaptive14_unified_mJJ7p5/cells.csv` byte-for-byte 一致。
- 14 cells 全部满足 `weight_sps + weight_dps = 1`；无负 error；`data = dps + sps` 总量闭合残差约 `1.5e-9`。
- P5 `single_pt` 和 `single_abs_y` 的 Data/mixed shape 均分别归一到 1；右图变量和标签统一为 `|y(J/psi)|`。
- P6 PDF 的中心值和误差匹配 `data`/`data_error`。
- P7 PDF 的中心值和误差匹配 `dps`/`dps_error`，不再显示 `mix_pair_error`。
- P8 PDF 的中心值和误差匹配 `sps`/`sps_error`；负格保留为 `-1.0 ± 6.1`。
- P9 两张图仅显示中心值，标题明确标注 `central value only`，不再出现 ROOT 默认 `sqrt(weight)`。
- 六张 PDF 已完成渲染、页面边界、标签、数值和 PDF 布局文字检查。本环境的图片查看 helper 因 `.agents` sandbox 故障不可用；未发现裁切、缺字或字段错配。
- 当前结论：consumer 数值和展示验收通过，等待用户确认；尚未复制到 `slides/figures/accepted/H006/`，尚未替换 P5--P9。
