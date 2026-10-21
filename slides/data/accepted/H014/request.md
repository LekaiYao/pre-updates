# H014 request：最新 data-driven nominal 方法与误差分析 presentation package

## Request metadata

- Request ID：H014
- Requester / consumer：pre-updates
- Producer / fact owner：JPsiJPsi
- 状态：requested
- 日期：2026-08-28
- Requester 文件：`pre-updates/docs/requests/active/H014_JPsiJPsi_data_driven_latest_nominal_uncertainty_package.md`
- Producer answer workspace：`JPsiJPsi/docs/answers/H014_preupdates_data_driven_latest_nominal_uncertainty/`
- Accepted baseline：2026-08-07 accepted H011/H012 nominal-method package 与 H013 propagation package
- Consumer purpose：制作一套约 30 分钟、初步预估约 25 页但不设硬性页数上限的 data-driven JJ 方法介绍
- Human gate：data-driven internal nominal、statistical uncertainty、method systematic、最终数值及与 CMS nominal 的定位均须由用户确认；producer `ready` 不等于 slides `accepted`

## 背景与职责边界

pre-updates 将从零制作一套面向不完全熟悉 JJ 分析的组内报告，重点解释 data-driven
SPS/DPS separation 在 JJ 分析中的作用、当前 data-driven nominal 方法和误差分析。
2026-08-07 旧 deck 保持冻结，不作为本轮增量修改对象。

共享 `progress.md` 已登记 H014，但当前可供 slides 消费的 accepted physics baseline 仍是
2026-08-07；JPsiJPsi 当前 handoff 已记录其后 nominal definition、bootstrap 和
method-systematic 研究，但 slides 不根据共享摘要或 handoff 自行猜测最新结论。请 producer
以当前代码、metadata、Git 状态和实际输出为准，给出相对 2026-08-07 baseline 的最新
delta 和可验收 artifacts。

本 request 只授权：

- 核对、总结和组织已经完成的代码侧工作与现有 artifacts；
- 生成必要的 documentation、manifest、hash/index 和 reader-facing summary；
- 明确现有结果的状态、限制和 human physics gates。

本 request 不授权新增或重跑 analysis、fit、bootstrap、systematic variation、plot、ROOT
production，也不授权修改 selection、nominal、systematic 定义或物理数值。若现有材料不足，
只列出缺口和建议，等待单独人工批准。

本文中的 data-driven nominal 仅指 data-driven 方法内部的当前 nominal scheme。除非经过
新的用户 physics gate，不得将其表述为替代 CMS MC-template nominal。

## A. L0：有界的最新 delta summary

请提供一至两页、最多八项 slide-relevant changes。每项使用以下字段：

```text
Area / status:
Change from 2026-08-07 accepted baseline:
Current conclusion:
Evidence and producer version:
Artifact status and path:
Limitations / human gate:
```

至少逐项明确以下类别为 `unchanged`、`changed`、`in progress`、`blocked` 或
`not applicable`，不得以沉默代替状态：

- dataset、candidate/sample 和 event-mixing source definition；
- selection、acceptance、efficiency 和 corrections；
- single-J extraction、fit/calibration 和 data-derived DPS construction；
- PP fit、control region、二维 cell/binning 和 SPS/DPS decomposition；
- 当前 data-driven internal nominal definition 与选择依据；
- statistical treatment、bootstrap ensemble 和 QA；
- method/systematic sources、组合规则、included/excluded/deferred coverage；
- central/provisional/final 数值、现有 figures/tables/artifacts 及未解决限制。

L0 不粘贴日志、长表、raw JSON 或完整 hash 清单；细节进入 L1/L2。

## B. L1：当前 nominal definition 与 artifact index

请从实际代码和 metadata 重新冻结当前 data-driven internal nominal 的完整事实定义，至少
包括：

- input Data/MC samples、event/candidate counts、selection 和 fiducial phase space；
- single-J source pool、slot treatment、fit model、calibration、sPlot/sWeight 定义；
- cross-event/cross-slot pairing、same-source rejection、all-pairs/sampling rule；
- correction、PP extraction、二维 cell geometry、control-region normalization；
- SPS/DPS algebra、reported estimator、projection treatment；
- 相对 H011 accepted baseline 的变化及当前方案被选为 nominal 的直接 evidence；
- 当前状态是 proposed、provisional、user-frozen 或 producer-final；
- precise Git branch/HEAD、tracked dirty files，以及 ignored tests/artifacts 的 provenance。

同时提供 L1 artifact index。每项至少记录：精确路径、格式、SHA256、生成代码/配置、
producer version、生成日期、状态（`accepted`/`ready`/`planned`/`missing`）、支持的 claim、
必要 caveat。只索引现有 artifacts，不复制大型 ROOT/PDF 集合。

## C. 当前 statistical uncertainty

请按当前 nominal 重新核对并交付：

- resampling unit、固定 seed/attempt 集合、replacement policy 和 estimator；
- requested/completed/successful/failed replicas 与 failure categories；
- calibration、yield-only fit、PP cell fit 的完整 QA；
- nominal、ensemble mean、sample SD、median、quantiles、range 和 mean shift；
- finite-ensemble precision 的解释，以及是否进入物理误差；
- 当前 uncertainty 覆盖哪些 statistical sources，哪些不再单列，哪些仍缺失；
- producer 与用户当前是否已冻结该 SD 为全部 `f_DPS` statistical uncertainty；
- 与 H011 500/529 successful-only spread 的 superseded relationship。

所有数值同时提供 machine precision 与推荐展示精度。若当前 handoff 中的结论与实际
metadata/ensemble 不一致，以实际输出为准并列出差异。

## D. 当前 method/systematic uncertainty

请提供 source-level breakdown，而不是只给总 quadrature。至少覆盖：

- control-region definition/purity；
- single-J category/model dependence；
- pure-DPS MC full-workflow closure；
- 2D binning 及其他 backup/diagnostic variations；
- acceptance、efficiency、corrections、fit model/shape、factorization、MC/feeddown、
  covariance 等 included、excluded 或 deferred sources。

每一项记录 nominal/variation、signed shifts、envelope 或映射规则、相关性/组合假设、审核
状态、artifact evidence 和可安全使用的 wording。明确区分 `statistical uncertainty`、
`method systematic`、`partial systematic`、`diagnostic` 和 `deferred`；不得将未覆盖来源
静默视为零。

请给出当前 asymmetric combined result、完整计算式/机器可读分解及推荐舍入，并明确它
是否已经过用户 physics gate、是否可称为当前完整 data-driven method systematic。

## E. Figures 与 reader-facing summary

请列出现有、最适合解释以下内容的 presentation candidates：

- data-driven 方法在 JJ SPS/DPS separation 中的作用；
- 当前 nominal workflow；
- single-J extraction、event mixing、PP/CR decomposition 的关键验证；
- bootstrap ensemble 与 QA；
- 各 method-systematic source 及组合；
- 当前结果、覆盖范围和限制。

每张图记录 exact path/format/SHA256、selection、normalization、生成版本、支持的结论、
caveat、推荐级别和 machine-readable source。若没有 presentation-ready 图，只报告缺口，
不要自动新画。

另提供一份不含 request/handoff/internal ID 的 reader-facing summary，供 slides 侧后续改写；
不得把 summary 本身当作 artifact evidence。

## 预期交付

请在 producer answer workspace 中提供：

1. `request.md`：与 requester active copy 内容一致；
2. `answer.md`：直接结论、与 baseline 的差异、限制和 human gates；
3. `delta_summary.md`：符合 L0 上限的分层摘要；
4. `nominal_definition.json` 或等价 machine-readable definition；
5. `statistical_uncertainty.json/csv` 与完整 QA summary；
6. `systematic_breakdown.csv/json`，含 source status、signed shifts 和组合；
7. `artifact_index.csv/md` 与 `figure_manifest.csv/md`；
8. 精确 code/config/metadata paths、Git branch/HEAD、dirty-file ownership 和复现入口；
9. `reader_facing_summary.md`；
10. 若需要新增工作，单列 `proposed_followups.md`，不执行。

交付状态先设为 `ready`，等待 pre-updates consumer review 和用户 physics gate，不得由
producer 直接设为 `accepted`。

## Consumer acceptance criteria

- baseline 和 producer version 明确，request/answer 可追溯；
- nominal definition 与当前代码、metadata 和实际输出一致；
- statistical ensemble、failure accounting 和 QA 可复核；
- systematic source-level coverage、组合与缺失项完整披露；
- figures/artifacts 的路径、hash、selection 和 claim 对应无误；
- 不把 data-driven internal nominal 误称为 CMS nominal；
- selection、fit、nominal、stat/systematic labels 和最终数值经用户确认；
- 只有转为 `accepted` 的 artifacts 才能写入新 slides。
