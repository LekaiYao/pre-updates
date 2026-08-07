# H011 consumer review

状态：`needs-fix`。H011 package 可作为经过核对的 `ready` 审阅材料，但在 producer
修正 provenance 且用户完成 physics gate 前，不得转为 `accepted` 或写入 slides。

2026-08-07：用户已批准基于本 package inventory 制定的两层页面计划；该批准不等于
接受 H011 physics content，也不解除 `accepted`-artifact gate。Consumer 修复意见已
写入 producer 的同一 answer workspace，未新建 request。

## 用户 physics decisions（2026-08-07）

- 接受 `abs(y)=1.2` category cross-slot all-pairs 作为 data-driven internal central
  scheme，central `f_DPS=0.169980427756`。
- 500 个成功 full-chain bootstrap replicas 的 sample SD `0.056796474528` 在本轮
  slides 中称为 `stat`；同时保留 500/529 attempts 和 29 个失败的事实说明。
- Category 与 control-region groups 合并称为暂定 `syst`，并分别解释每个来源。
  当前计划采用独立 group envelope 的 quadrature：
  `+sqrt(0.007263523592^2+0.001318512530^2)=+0.007382225292`，
  `-sqrt(0^2+0.010590504745^2)=-0.010590504745`。该数学组合规则尚需用户明确确认。
- Slides 主体聚焦 data-driven 方法；只在结尾将当前结果与 AN 的 CMS MC-template
  nominal 比较。CMS nominal 身份不变。

这些决定完成 physics wording gate，但不自动修复 producer metadata。H011 在
provenance 修正或用户明确接受 known-defect waiver 前仍保持 `needs-fix`。

## 已核对通过

- Codes 仓库为 `sync/chensh-20260730@24823a5`，普通 Git 视图 clean；测试代码和
  artifacts 按 producer 规则由 Git 忽略，文件身份使用 manifest SHA256。
- `figure_manifest.csv` 的 23 项 PDF 全部存在，页数和 SHA256 匹配；
  `source_manifest.csv` 的 16 项 source 全部存在且 SHA256 匹配。
- 23 项 PDF 共 25 页已用 Poppler 渲染检查；新 central maps 和 component figures
  未发现裁切、重叠、损坏或不可读 glyph。
- 从 14-cell `cells.csv` 独立复算：`f_DPS=0.169980427756`，SPS+DPS 与 PP
  algebraic closure 成立，并保留一个 signed negative SPS cell。
- 从 category/CR CSV 独立复算 category shifts `+0.006322094151`、
  `+0.007263523592`，以及 CR shifts `+0.001318512530`、
  `-0.002547539913`、`-0.010590504745`。
- 从 100 个 job summary 和 529 个 attempt metadata 独立复算：100/100 jobs
  complete、500 successes、29 failures；bootstrap mean、sample SD、median、
  16%/84% quantiles、min/max 均与 package 一致。
- 失败阶段独立归类为 Jpsi1 category calibration 14、Jpsi2 category calibration 7、
  PP sparse-cell fit 8；成功样本 SD 仍只能称 provisional bootstrap statistical spread。
- 关键实现抽查与 package 一致：`abs(y)=1.2` category、slot-specific sPlot、
  cross-slot all-pairs、same-source rejection、14-cell PP fit、CR normalization 和
  full source-event bootstrap policy。

## 阻塞接收的问题

1. 新 central template metadata 的 `artifact` 仍硬编码为旧
   `H007_fixed_H006_2D_maps`；同一陈旧值也出现在三组 CR template metadata。
2. Metadata 仍写 `joint_statistical_propagation=handled_by_H006_E1_source_event_bootstrap`，
   与当前 full-chain bootstrap 交付冲突。
3. `selection=unchanged_H006_E0_nominal` 没有区分“PP Data selection 未改变”和
   “DPS construction 已升级为 cross-slot category all-pairs”，容易造成 provenance
   误读。
4. 上述字段来自 `build_2d_templates_adaptive.cpp` 的硬编码，不是单个输出文件的
   偶然笔误；producer 应同时修正 generator 与 central/CR metadata。
5. `abs(y)=1.2` central scheme、bootstrap failure treatment、category/CR 分组及组合
   规则、systematics/final-number wording 尚未完成用户 physics gate。

## 接收条件

- Producer 修正 generator 和 central/CR metadata；不要求重跑 fit 或重新生成数值，
  但须重新提供变更后 source/metadata SHA256，并说明 PDF 是否保持 byte-identical。
- Consumer 复核修正后的 provenance，不得仅以 answer 摘要替代实际 metadata。
- 用户确认 central scheme、statistical treatment、partial systematic wording 和可报告
  数值；之后才将 H011 标为 `accepted`。

## Slides 消费边界

- H011 当前只可用于计划和验收，不得复制 PDF、转录新数值或写入 TeX 正文。
- 已 accepted 的历史 data-driven artifacts 可用于 recap，但必须保留“validated
  cross-check，不替代 CMS MC-template nominal”的边界。
- Stale nominal-comparison PDF 继续禁止使用。
