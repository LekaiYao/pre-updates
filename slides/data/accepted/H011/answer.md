# Data-driven optimization update package

状态：`ready`，用户 physics gate 已完成，等待 consumer provenance 复核。本文只汇总
现有运行，未新增 run、fit、bootstrap、plot 或物理定义。

2026-08-07 provenance 复核后，generator 及 central/三组 CR metadata 已完成
metadata-only 修正：PP Data selection 与 upgraded DPS construction 被分开记录，
statistical provenance 指向当前 full-chain source-event bootstrap。所有数值和 23 张
PDF 均未重建且 byte-identical；新 hashes 见 `source_manifest.csv` 和相邻修正 workspace。

## 直接结论

当前 data-driven central scheme 的 provisional 选择是：对 2492 个 selected source
events 的 Jpsi1/Jpsi2 分别按 `abs(y)<1.2` 与 `abs(y)>=1.2` 做未加权 mass--ctau
sPlot，使用不同 source events 的 `Jpsi1(A) x Jpsi2(B)` 全笛卡尔组合构造 signed
DPS template，在 adaptive 14-cell `abs(delta_y) x abs(delta_phi)` 平面用
`abs(delta_y)>=1.8 && abs(delta_phi)<=pi/2` control region 归一化。二维 direct
estimator 给出 `f_DPS=0.169980427756`。

这个选择已由用户批准为本轮 slides 的 data-driven internal central，不替代 CMS
MC-template nominal。用户批准将成功 bootstrap 样本的 SD 标为 `stat` 并披露失败，
category/CR 独立 group envelopes 的 quadrature 标为 provisional `syst`；它仍不是完整
systematic uncertainty。

500 个成功 full-chain source-event bootstrap replicas 的 sample SD 为 `0.0567965`，
但 529 次 attempts 中有 29 次失败，而且失败条件与拟合/稀疏 cell 相关；用户已决定
本轮 slides 将其标为 `stat`，同时必须披露 500/529 和失败分类。已完成的 tested method
groups 是 category sensitivity `+0.007264/-0` 和 control-region sensitivity
`+0.001319/-0.010591`；用户批准暂按独立 groups quadrature 合成为 provisional
`syst=+0.007382/-0.010591`，不能称为完整 systematic uncertainty。

## 主要进展排序

1. **Single-J prompt purification、cross-slot mixing 与 all-pairs central chain。**
   这是最重要的方法升级：避免把 event-level sWeight 拆给单个 J/psi，分别处理两个
   slots，并用 6,061,749 个 accepted all-cross-event pairs 消除随机 mixing seed 和
   固定 pool 上的 pair-sampling variance。
2. **Data-driven kinematic category treatment。** `pT=15 GeV` 与
   `abs(y)=1.2` category fits 直接检验 mass/ctau response 的动力学依赖；所有
   calibration、yield-only sPlot 和 156/156 component fits 通过。明显的 forward
   mass-resolution change 是暂选 `abs(y)=1.2` 的物理依据。
3. **Full source-event bootstrap。** 500 个成功 replicas 已同时重做两个 category
   sPlots、all-pairs mixing、Data PP cell fits 和 CR normalization，传播了 source-event
   statistics 与 Data--template covariance；当前主要缺口是 29 个条件性失败可能造成
   selection bias。
4. **同一 central scheme 下的 CR variations。** 234/234 component fits 通过，给出
   当前可单独报告的 tested CR envelope。
5. **DPS MC direct-template benchmark。** 它验证 alternative scheme 和 Asimov
   closure，但依赖 generator，不是 data-driven nominal gate，也不定义 event-mixing
   uncertainty。

完整路线与保留/降级判断见 `progress_inventory.csv`。

## 当前 central scheme 的证据

- Jpsi1/Jpsi2 的四个 category calibration fits 和四个 yield-only fits 均为
  `status=0,covQual=3`，prompt sWeight sums 回到 fitted prompt yields。
- signed candidate/pair weights 均保留；same-source pairs 明确排除；重新施加
  `m(Jpsi Jpsi)>=7.5 GeV` 和 nominal pair correction。
- 6,118,202 个笛卡尔 pairs 中接受 6,061,749 个；correction rejection 为 0。
- nominal 78/78 component fits 和三组 CR 的 234/234 fits 通过。
- 四个 projected `f_DPS` 为 `0.168262--0.169247`，接近 direct 值；这只是实现与
  decomposition consistency，不是四个独立测量。
- 二维 cell algebraic closure 精确；一个 SPS cell 为负，来自 signed subtraction，
  不能裁剪为零。

精确定义见 `nominal_definition.json`，代码和 metadata 哈希见
`source_manifest.csv`。

## 当前误差可报告边界

- **可报告：** provisional central `0.169980`；500-success-replica bootstrap
  distribution 的 mean、SD、median、quantiles；category 与 CR 的逐项 signed shifts。
- **用户批准的本轮口径：** bootstrap SD 标为 `stat`。失败率为 `29/529=5.482%`，其中 Jpsi1 category
  calibration 14 次、Jpsi2 calibration 7 次、PP cell fit 8 次。8 次 PP 失败都在
  `abs(delta_y)=2.4--4, abs(delta_phi)=0--pi/2` cell，只有 6 或 9 个 fit entries，
  低于代码的 10-entry 门槛；这不是已证明的随机缺失。
- **用户批准的暂定组合：** 将 category 与 CR 视为独立 groups，quadrature 得到
  provisional `syst=+0.007382/-0.010591`；没有直接 covariance estimate，因此必须
  同时拆分展示两组来源，不能称为完整 systematic uncertainty。
- **尚未覆盖：** alternative single-J functional forms、fixed-shape parameter
  uncertainty、acceptance/efficiency/pair-trigger corrections、alternative 2D binning、
  downstream fit-model dependence、CR SPS leakage/purity、prompt SPS/DPS marginal
  factorization bias，以及 bootstrap coverage。

机器可读明细见 `uncertainty_breakdown.csv`。

## 图片审核与缺口

`figure_manifest.csv` 登记了当前 central maps、四变量 component fits、DPS-MC
benchmark 和仍有解释价值的 accepted historical artifacts。2026-08-07 已用 Poppler
渲染并视觉核对 16 张新 central/benchmark PDFs：未发现裁切、重叠或不可读 glyph。

当前没有 presentation-ready 的 category comparison 图或 bootstrap distribution 图；
request 不授权作图，因此只登记为 follow-up。旧 data-driven maps/component fits 已被
新 cross-slot `abs(y)` category all-pairs scheme 取代；它们仍是 accepted historical
baseline，不应与新中心值混用。旧 nominal-comparison PDF 显示 stale `1.59 mb`，禁止
进入新 slides。

## Consumer 验收状态

用户已确认 `abs(y)=1.2` central、bootstrap SD 的 `stat` 标签、category/CR 独立-group
quadrature 的 provisional `syst` 以及仅在结尾比较 CMS nominal。当前只等待
pre-updates 对 provenance correction、文件和 hashes 的 consumer 复核。

建议后续工作列于 `proposed_followups.md`；本次没有执行这些工作。
