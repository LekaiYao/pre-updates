> Lifecycle: completed and archived on 2026-08-07. The metadata-only correction passed consumer validation and enabled H011 acceptance; live cross-project status is tracked only in shared `../../../../docs/progress.md`.

# H012 request：修正 H011 provenance metadata

## Request metadata

- Request ID：H012
- Requester / consumer：pre-updates
- Producer / fact owner：JPsiJPsi
- 状态：requested
- 日期：2026-08-07
- Requester 文件：`pre-updates/docs/requests/active/H012_JPsiJPsi_H011_provenance_metadata_correction.md`
- Producer answer workspace：`JPsiJPsi/docs/answers/H012_preupdates_H011_provenance_metadata_correction/`
- 关联交付：`JPsiJPsi/docs/answers/H011_preupdates_data_driven_optimization_update/`
- Consumer review：`pre-updates/docs/qa/H011_consumer_review_2026-08-07.md`

## 背景与授权边界

H011 的文件、hash、数值、bootstrap summary 和 PDF visual checks 已通过 consumer
核对，但 central 与三组 control-region template metadata 仍继承旧 provenance，故
H011 保持 `needs-fix`。本 request 只授权修正 generator、metadata 和交付文档中的
provenance；不授权新增或改变 analysis、selection、fit、bootstrap、ROOT、plot、
estimator 或物理定义。预计不需要重跑数值生产；若实际必须重跑，请先停止并说明原因。

## Required correction

1. 修正 `tests/atlas_data_driven_sps/build_2d_templates_adaptive.cpp` 中用于当前输出的
   陈旧硬编码字段，包括不适用的
   `artifact=H007_fixed_H006_2D_maps` 和
   `joint_statistical_propagation=handled_by_H006_E1_source_event_bootstrap`。
2. 同步修正 current central 及三组 CR template metadata；保留实际输入路径、配置、
   selection、binning、normalization 和数值，不因本 request 改变物理输出。
3. 无歧义地区分：PP Data selection 保持不变；data-derived DPS construction 已升级为
   slot-specific prompt sPlot、cross-slot category all-pairs，并拒绝 same-source pairs。
4. Statistical provenance 应准确指向当前 full-chain source-event bootstrap，并记录
   500 个成功 replicas、529 次 attempts 和 29 次条件性拟合失败；slides consumer 已
   决定将成功样本的 sample SD 称为 `stat`，producer 不需据此修改数值。
5. 复核 H011 的 `answer.md`、manifest、definition、summary 和相关 metadata，修正其中
   同类陈旧 provenance 引用；不要重写已核对通过的物理结论。

## 已冻结的 consumer physics decisions

- Data-driven internal central：`abs(y)=1.2` category cross-slot all-pairs，
  `f_DPS=0.169980427756`。
- Bootstrap sample SD `0.056796474528` 在本轮 slides 中称为 `stat`，同时披露
  500/529 和失败分类。
- Category 与 CR 作为两个来源分别解释，并暂按独立 group envelopes quadrature
  合并为 provisional `syst`：`+0.007382225292/-0.010590504745`。
- Slides 主体为 data-driven；只在结尾比较当前 AN 的 CMS MC-template nominal。

这些是 consumer/user wording 与组合决定，不授权 producer 修改 central、variation、
bootstrap 或 CMS nominal。

## 预期交付

请在 producer answer workspace 中提供：

1. `answer.md`：逐项说明修改内容、未修改内容及是否发生任何重跑；
2. 修正后的 generator 与 central/三组 CR metadata 的精确路径和 SHA256；
3. 更新后的 H011 source/metadata manifest 或等价 machine-readable 清单；
4. H011 现有 PDF 的前后 SHA256 对照，并明确是否全部 byte-identical；
5. 精确 Git branch、HEAD、工作区状态及被忽略 artifacts 的 provenance context；
6. 对 H011 文档中陈旧引用的复核结果；
7. 状态设为 `ready`，等待 pre-updates consumer 复核，不得自行设为 `accepted`。

## Consumer acceptance criteria

- 上述陈旧字符串在当前 generator/metadata 中不再被不恰当地使用；
- PP Data selection 与升级后的 DPS construction 被清楚区分；
- full-chain bootstrap provenance 与实际 H011 production 一致；
- 实际输入路径、配置及 H011 数值保持不变；若任何内容变化，须逐项解释；
- PDF 应保持 byte-identical；若不一致，H012 不自动通过并需重新验收；
- consumer 对实际文件和 hash 复核通过后，才可将 H011/H012 转为 `accepted` 并开始
  正式 slides 制作。
