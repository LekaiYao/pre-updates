# H016 request：data-driven JJ 最新结果、最终传播与汇报图片

## Request metadata

- Request ID：`H016`
- Requester / consumer：`pre-updates`
- Producer / fact owner：`JPsiJPsi`（代码侧；规则适用于承担分析代码与结果生产的项目）
- 状态：`open`
- 日期：2026-08-29
- Requester copy：`pre-updates/docs/requests/active/H016_JPsiJPsi_data_driven_final_results_and_figures.md`
- Expected producer copy：`JPsiJPsi/docs/requests/active/H016_preupdates_data_driven_final_results_and_figures.md`
- Expected answer workspace：`JPsiJPsi/docs/answers/H016_preupdates_data_driven_final_results/`
- Consumer purpose：纳入本轮约 30 分钟的 data-driven JJ 方法介绍
- Human gate：selection、fit、systematics、相关性方案与最终物理数值仍须用户确认；producer package 先设为 `ready`

## 目标

请代码侧基于当前 Git、代码、metadata 和实际输出，提供一份自洽的 data-driven 最新结果总结，
并完成当前 `f_DPS` 对 `sigma_DPS` 和 `sigma_eff`（有效截面）的最终计算/传播及汇报图片。
pre-updates 不从共享摘要猜测结果，只消费经 consumer 验收转为 `accepted` 的交付。

## 必须核对的当前基线

1. 当前 accepted data-driven 结果：
   `f_DPS=0.170423232645`，固定 500/500 full-workflow bootstrap
   `stat=0.059331299623`，method systematic
   `+0.010177290968/-0.011083850610`。
2. 当前 method systematic 的三个组合组为 single-J category、CR definition/purity、
   pure-DPS full-workflow closure，向上/向下分别做 quadrature。
3. 当前 CR 中心处理采用 zero SPS leakage；CR systematic 同时扫描 zero-leakage 与
   SPS-MC leakage variants。MC-leakage variant 已实际进入最终 envelope：负向边界
   `-0.006494652437` 来自 `|Delta phi|<=110 deg` 的 MC-leakage treatment。
4. 共享状态目前记录的 `sigma_DPS=6.339744254394 pb` 及其误差仍需用当前代码和输入复核；
   H013 的旧 `f_DPS=0.169980427756` 传播不是当前最终结果，不能直接复用。
5. 当前 AN 的 MC-template 结果与 data-driven 结果是不同方法；交付中不要把前者标作
   “nominal”，也不要把后者标作 “cross-check”。禁止引用 stale `sigma_eff=1.59 mb`。

若以上摘要与实际 Git、代码或 metadata 不一致，以事实源为准，并在 answer 开头列出差异。

## A. 最新 data-driven 结果总结

请用 reader-facing 语言总结：数据/selection、single-J extraction、event mixing、12-cell PP
fits、CR normalization、`f_DPS` estimator、fixed-500 bootstrap、三项 method systematic 和
最终 `f_DPS`。每项给出事实源路径、producer branch/HEAD、状态及必要 caveat，不复制冗长日志。

## B. `sigma_DPS` 与 `sigma_eff` 最终计算

请使用当前输入重新审计并计算：

- `sigma_DPS = f_DPS * sigma_pair_total`；
- `sigma_eff = (1/2) * sigma_single^2 / sigma_DPS`；
- 明确 pair/single cross section、fiducial phase space、visible/full convention、单位换算、
  branching fraction 与 luminosity treatment；
- 给出 machine precision 和适合 slides 的舍入值；
- 给出 stat 与 asymmetric systematic 的 source-level 传播，说明 covariance/correlation、
  cancellation 和 double-counting 处理。

H013 中 `Cov(f_DPS,sigma_pair_total)` 未解决。请优先核对当前 artifacts 是否已能给出有依据的
最终统计传播；若仍不能，请明确区分：可冻结的最终中心值、条件性/reference 误差、仍需新增
production 才能解决的部分。不得把未知 covariance 静默设为零或把 `rho=0` 包装为最终结论。

## C. SPS MC leakage 的当前使用与改进记录

请在 answer、uncertainty source map 和 summary metadata 中明确记录：

- SPS MC 用于估计各 CR 的 `r_SPS^CR`；MC-leakage treatment 在 DPS normalization 前扣除
  相应 SPS contribution；
- zero/MC-leakage variants 与 CR 边界变化共同形成一个 CR definition/purity envelope，
  不作为另一项独立误差重复平方和；
- 当前最终 method systematic 因此包含对 SPS MC leakage estimate 的依赖；
- 将“降低或替代该 SPS-MC 依赖”列为后续可能改进点，例如数据约束、替代生成器/模型或
  更直接的 leakage validation；本 request 不授权自动改变已接受的中心值或系统误差定义。

## D. Presentation figures

请提供 vector PDF 与同内容 PNG，至少包括：

1. 当前最终 `f_DPS` 结果及 stat/method-syst summary；
2. `sigma_DPS` 最终计算与 uncertainty breakdown；
3. `sigma_eff` 最终计算与 uncertainty breakdown；
4. 一张适合结论页的 data-driven result summary，可并列 `f_DPS`、`sigma_DPS`、`sigma_eff`；
5. 一张清楚标出 CR zero/MC-leakage variants 已进入 envelope 的系统误差图；若 H015 F07
   已足够，可复用并在新 manifest 中精确引用，不重复绘图。

图中只显示可由 machine-readable source 支持且已明确状态的结果。若某个误差仍非 final，
必须在图和 metadata 中使用准确的状态标签，不得用视觉省略掩盖。

## 预期交付

请在 expected answer workspace 提供：

1. 与 requester copy byte-identical 的 `request.md`；
2. `answer.md`：直接结论、与共享摘要的差异、推荐 slides 口径和 human gates；
3. `inputs.json`、`results.csv/json`、`uncertainty_source_map.csv`；
4. 可复现的确定性计算/传播脚本与运行说明；
5. figures 的 PDF/PNG、machine sources、manifest、SHA256、生成时间和 producer Git provenance；
6. tracked dirty files 及 ownership；
7. package 状态设为 `ready`，等待 pre-updates consumer review，不得直接设为 `accepted`。

## Consumer acceptance criteria

- requester/producer request byte-identical，版本、输入、phase space 和单位可审计；
- 最新 `f_DPS`、`sigma_DPS`、`sigma_eff` 的算术和逐源误差传播闭合；
- covariance/相关性未知项没有被静默忽略，历史 H013 数值没有冒充当前结果；
- SPS MC leakage 的实际纳入方式、envelope 归属和后续改进点均明确记录；
- figures 与 machine tables 数值一致，slides 尺寸无裁切、遮挡或不可读标签；
- 用户确认最终数值和物理口径后，consumer 才可将对应 artifacts 转为 `accepted`。
