> Lifecycle: accepted and archived on 2026-08-07 after consumer technical review and user physics gate. Live cross-project status is tracked only in shared `../../../../docs/progress.md`.

# H013 request：由当前 data-driven f_DPS 计算 DPS 与有效截面

## Request metadata

- Request ID：H013
- Requester / consumer：pre-updates
- Producer / fact owner：JPsiJPsi
- 状态：accepted and archived
- 日期：2026-08-07
- Requester archive：`pre-updates/docs/requests/archive/H013_JPsiJPsi_data_driven_sigma_eff_propagation.md`
- Producer answer workspace：`JPsiJPsi/docs/answers/H013_preupdates_data_driven_sigma_eff/`
- 输入基线：accepted H011 data-driven central/stat/provisional-syst package，以及当前 AN 中的截面输入
- Human gate：completed 2026-08-07；central 与 provisional partial systematic accepted，
  statistical covariance 保持 unresolved/pending

## 目标与职责边界

请根据当前已接受的 data-driven `f_DPS` 计算 fiducial `sigma_DPS` 和
`sigma_eff`，重点解决 AN 截面误差与当前 `f_DPS` 误差如何一致组合。JPsiJPsi
负责核对代码、AN 当前文本、metadata 和实际输出，并给出可审计的计算与推荐口径；
pre-updates 只在 artifact 后续转为 `accepted` 后决定是否写入 slides。

本 request 授权新增轻量、确定性的 post-processing 脚本和 machine-readable 输出，
不授权修改 selection、fit、data-driven central、AN nominal 或系统误差定义，也不授权
新增 fit、bootstrap production 或大规模重跑。若可靠 covariance 必须依赖新的联合
resampling/fit，请写成 follow-up proposal 并停止，不得用未经验证的相关性替代。

## 已知输入（必须重新核对，不得直接照抄）

1. H011 accepted data-driven internal central：
   `f_DPS = 0.169980427756`。
2. 当前 slides 采用的 statistical label：500 个成功 full-chain source-event bootstrap
   replicas 的 sample SD `0.056796474528`；必须同时披露 500/529 attempts、29 failures
   及 successful-only conditional-selection caveat。
3. 当前 provisional partial systematic：category 与 control-region 独立 group-envelope
   quadrature，`+0.007382225292/-0.010590504745`；必须拆分来源，且不得称为完整
   systematic uncertainty。
4. 当前 AN pair fiducial cross section 在 `AN/8_Result.tex` 中写为
   `37.2 +/- 0.6 (stat.) +/- 2.5 (syst.) pb`。
5. 当前 AN `sigma_eff` 使用的 single-J/psi visible input 在
   `AN/ApxF_Other_Results.tex` 中写为
   `BR(J/psi->mu+mu-) sigma(J/psi) = 10.63 +/- 0.01 +/- 0.09 nb`；旧 E4
   post-processing 还单列 luminosity 与 branching-fraction treatment。
6. 当前 CMS MC-template nominal comparison 的 code-side corrected value 是
   `sigma_eff = 1.26191 mb`，AN 已更新为约 `1.26 mb`；任何旧 `1.59 mb` 都是 stale，
   禁止使用。

请核对以上每项的当前 source path、commit/文件状态、fiducial phase space、单位、
visible/full cross-section convention、branching fraction 和 luminosity treatment。
若 AN、代码或 metadata 不一致，以当前代码、实际 metadata 和 AN 当前文件为依据并报告差异。

## A. 中心值计算

请使用并明确验证：

- `sigma_DPS = f_DPS * sigma_pair_total`；
- `sigma_eff = (1/2) * sigma_single^2 / sigma_DPS`，并说明这里使用的是 visible
  cross sections 还是已除 branching fraction 的 cross sections；
- pb、nb、mb 的全部换算和 pair-specific `m(J/psi J/psi)>7.5 GeV` 对 single-inclusive
  numerator 的适用性；
- 与旧 H006 E4 和当前 CMS MC-template nominal post-processing 的 convention 是否一致。

输出未经格式化截断的 machine-precision 值，以及适合文档/slides 的建议舍入值；后者
只作为 producer recommendation，不自动成为 final result。

## B. 统计误差与 covariance

`f_DPS` bootstrap 与 AN pair total cross section 使用同一 CMS pair-data sample，不能在
没有论证时直接视为统计独立。请从 estimator 和数据流判断二者的统计相关性，并使用

`Var(f P) = P^2 Var(f) + f^2 Var(P) + 2 f P Cov(f,P)`

作为审计基准，其中 `f=f_DPS`、`P=sigma_pair_total`。请交付：

1. 现有 artifacts 是否足以确定或估计 `Cov(f,P)`；
2. 若足够，给出 covariance 的取得方式、数值、验证和 joint propagated result；
3. 若不足，给出清楚标注的 independent-input approximation，并做相关性敏感性扫描
   （至少 `rho=-1,0,+1`，或更有物理依据的范围）；
4. 说明 500-success bootstrap 的 failures/conditioning 如何限制该统计结果；
5. 不得把同一 pair-yield fluctuation 同时计入 `f_DPS` bootstrap 和 AN cross-section
   statistical uncertainty 而不讨论 double counting。

single-J/psi statistical uncertainty进入 `sigma_eff` 时也须单列。若它与 CMS pair-data
统计独立，请给出依据；若不能证明，保留为假设。

## C. 系统误差、相关性与避免重复计入

请建立 source-level correlation map，而不是只对总误差做平方和。至少逐项判断：

- data-driven category group；
- data-driven control-region group；
- pair acceptance、efficiency、pair trigger、fit/yield extraction、luminosity、branching
  fraction及 AN `2.5 pb` 中的其他来源；
- single-J/psi bin systematic、luminosity、branching fraction及其来源实验；
- H011 明确尚未评估的 corrections、functional form、fixed-shape、binning、factorization
  和 CR-purity sources。

对每项标明：进入 `f_DPS`、`sigma_pair_total`、`sigma_single` 的位置，相关/不相关/未知，
是否已包含，是否需要去除或可相消，以及依据路径。特别核对：

- `f_DPS` 的 nominal pair correction 与 AN pair cross-section systematics 是否共享
  acceptance/efficiency/trigger 变化；
- CMS pair 与 ATLAS single-J/psi luminosity是否独立；
- visible-cross-section 公式中的 branching fraction 是否精确相消，避免重复加入；
- 分母的 asymmetric uncertainty 映射到 `sigma_eff` 时方向应反转，并保留非线性和
  非对称性。

当前 `f_DPS` systematic 明确不完整。因此即使完成数值传播，也只能给出
`provisional/partial systematic` 的 `sigma_DPS` 和 `sigma_eff`，除非另有新的用户 gate。

## D. 传播实现与对照方案

请由 codes 选择并说明合适的实现（analytic Jacobian、endpoint propagation、toy
propagation 或其组合），但必须保留 source-level breakdown 和 asymmetric directions。
至少输出三套清楚区分的结果：

1. 推荐结果：只使用有依据的 correlation/cancellation；
2. `rho=0` independent-input reference；
3. 未知相关性的范围或敏感性结果。

同时重现旧 H006 E4 和当前 CMS MC-template nominal 的已知结果作为 implementation
cross-check；该对照不得改变当前 data-driven 结果的定位。

## 预期交付

在 producer answer workspace 中提供：

1. `answer.md`：直接结论、推荐误差口径、限制及是否需要后续联合 resampling；
2. `inputs.json`：所有输入、单位、phase space、source path、hash/commit 和状态；
3. `results.csv` 或 JSON：`sigma_DPS`、`sigma_eff` 的中心值、stat、provisional syst、
   asymmetric directions、舍入值和 scenario label；
4. `uncertainty_source_map.csv`：逐源 included/excluded/correlation/cancellation 状态；
5. 可复现 post-processing 脚本及最小运行说明；
6. 对旧 H006 E4 与 CMS MC-template nominal 的 numerical cross-check；
7. 若现有输入不能支持 covariance，单列 proposed follow-up，不执行新 production；
8. artifact 状态先设为 `ready`，不得直接标记 `accepted`。

## Consumer 验收条件

- requester copy 与 producer `request.md` byte-identical；
- 所有输入和公式均可追溯到当前 AN、codes 和 accepted H011 artifact；
- 不引用 stale `1.59 mb`，不把 data-driven 结果称为 CMS nominal；
- covariance、independence 和 cancellation 均有逐源依据，未知项没有被静默设为零；
- 500/529 bootstrap caveat 与 incomplete systematic scope 保留；
- central、stat、systematics、相关性方案和最终数值经用户确认后，artifact 才可从
  `ready` 转为 `accepted` 并供 slides 使用。
