# H016 producer answer：data-driven 最终结果传播与汇报图片

Package status：`ready`，等待 pre-updates consumer review；不得直接视为
`accepted`。

## 与 request/shared baseline 的差异

1. 当前 accepted `f_DPS` 与 H016 baseline 一致；当前 preliminary
   `sigma_DPS(mJJ>7.5)=6.339744254394 pb` 也复核一致。
2. H013 使用旧 `f_DPS=0.169980427756`，没有被复用。
3. 当前 AN 和 H013-style `sigma_eff` 传播没有处理 pair-specific `m(JJ)>7.5 GeV` cut。H016
   新增 DPS GEN-only factorized event-mixing 效率 `epsilon_m=0.987338870402`，先把
   `sigma_DPS` 外推到无 pair-mass cut，再计算 `sigma_eff`。
4. 当前仍没有 replica-matched `Cov(f_DPS,sigma_pair_total)`。因此 `rho=0` 只能作为用户已允许
   本轮展示的 preliminary reference；package 同时提供 `rho=-1,0,+1` sensitivity，未把未知
   covariance 静默设为零或包装为 final。

## 直接结果与推荐 slides 口径

当前 accepted fraction 为：

`f_DPS = 0.170423 +/-0.059331 (stat.) +0.010177/-0.011084 (method syst.)`。

适合 slides：

`f_DPS = 0.170 +/-0.059 (stat.) +0.010/-0.011 (method syst.)`。

带测量 pair-mass cut 的结果为：

`sigma_DPS(mJJ>7.5) = 6.339744 +/-2.209492 (stat., rho=0) +0.574668/-0.597425 (syst.) pb`。

适合 slides，并保持 preliminary 标签：

`sigma_DPS = 6.34 +/-2.21 (stat.) +0.57/-0.60 (syst.) pb`。

DPS GEN-only event mixing 给出：

`epsilon_m = 30256975/30644975 = 0.987338870402`，`1/epsilon_m = 1.012823489460`。

因此用于有效截面的无 pair-mass cut DPS 截面为：

`sigma_DPS(no mJJ cut) = 6.421042 +/-2.237825 (stat., rho=0) +0.582037/-0.605086 (syst.) pb`。

最终的当前 preliminary 有效截面为：

`sigma_eff = 2.476240 +/-0.863018 (stat., rho=0) +0.253003/-0.223538 (syst.) mb`。

适合 slides，并保持 preliminary 标签：

`sigma_eff = 2.48 +/-0.86 (stat.) +0.25/-0.22 (syst.) mb`。

`epsilon_m` 的不确定度按用户当前指示不加入；这不代表其为零。

## 当前 data-driven 分析链

- Data/selection：119 个 Data ntuples；2492 个 selected source events；trigger、same-PV、每个
  J/psi `10<=pT<=40 GeV`、`abs(y)<2.0`，pair `m(JJ)>=7.5 GeV`。事实源：
  `docs/answers/H014_preupdates_data_driven_latest_nominal_uncertainty/nominal_definition.json`。
- Single-J extraction：Jpsi1/Jpsi2 分开做 calibrated global 两阶段 mass--ctau fit；冻结 resolution
  scales 后做 yield-only sPlot，保留 signed prompt sWeights。状态：accepted H014 input。
- Event mixing：deterministic Jpsi1(A) x Jpsi2(B) all-cross-event pairs；拒绝 same source 和
  `m(JJ)<7.5 GeV`，接受 6,061,749 pairs；应用 nominal pair correction。
- PP extraction：当前 12-cell `abs(delta_y)`--`abs(delta_phi)` geometry；每 cell 做 4D PP fit，
  12/12 accepted。
- CR normalization：单一 CR 为 `1.8<=abs(delta_y)<=4`、`abs(delta_phi)<=pi/2`；nominal 假设
  zero SPS leakage；`f_DPS=sum(N_DPS)/sum(N_PP)`。
- Statistical uncertainty：固定 500/500 full source-event bootstrap，0 failures、0 replacement；
  取 500 个 `f_DPS` 的 sample SD `0.059331299623`。
- Method systematic：single-J category、CR definition/purity、pure-DPS full-workflow closure 三组
  分别取 envelope/closure mapping 后，向上和向下独立 quadrature。

Producer branch/HEAD：`sync/chensh-20260730` /
`b89508566a2096bf40e3a99addac7d09fd901e2b`。冻结分析 runtime：CMSSW_10_6_20 / ROOT
6.14/09 / cmssw-el7。本 request 未重跑 selection、fit、bootstrap 或 systematics。

## Cross-section convention 与 uncertainty propagation

Pair 输入为 physical prompt-prompt cross section，已除去 `B(J/psi->mumu)^2`，相空间包含
`m(JJ)>7.5 GeV`。Single-J 输入为 ATLAS HEPData 积分得到的 visible quantity
`X=B*sigma(prompt J/psi)=10.63 +/-0.01 (stat.) +/-0.09 (bin syst.) nb`，另加 1.13% ATLAS
luminosity；J/psi-level phase space 为 `10<pT<40 GeV`、`abs(y)<2.0`，无 pair-mass cut。

有效截面采用：

`sigma_eff[mb] = 0.001 * 0.5 * X[nb]^2 / [B^2 * sigma_DPS(no mJJ cut)[pb]]`。

AN 的五项 pair systematic 百分数 `1.1%, 1.2%, 6.1%, 0.3%, 2.56%` 直接作为输入，
不为恢复展示值 `2.5 pb` 做任何归一化或缩放。五项平方和为 `6.8193548%`，对应
`2.53679999 pb`；AN 的 `2.5 pb` 只作为一位小数展示值，不作为精确传播输入。

对 `sigma_DPS`，三项 `f_DPS` method groups 与上述五项 AN sources 分别传播后按方向平方和。
对 `sigma_eff`，共同 BR 在 `X^2/Y` 中严格消去；其余四项 AN sources、三项 `f_DPS`
method groups 以及两项 ATLAS sources 均逐独立 source 做精确 endpoint，再分别合并 up/down。
ATLAS 和 CMS luminosity 来自不同实验，按独立处理。Acceptance/efficiency、lifetime 和
fitter 与 `f_DPS` workflow 的相关性没有 matched variations，当前数值只采用明确标注的
conditional independence。完整数值见 `uncertainty_source_map.csv`。

统计相关性 sensitivity 为：

- `sigma_DPS(mJJ>7.5)` stat：rho=-1/0/+1 分别为 `2.10487/2.20949/2.30938 pb`；
- `sigma_eff` stat：rho=-1/0/+1 分别为 `0.82215/0.86302/0.90203 mb`。

在建立 replica-matched pair-total estimator 前，rho 不能由当前 artifacts 决定。

## SPS MC leakage 的实际纳入方式

SPS MC 用于估计不同 CR 定义下的 `r_SPS^CR`；MC-leakage variant 在 DPS normalization 前
扣除相应 SPS contribution。Zero-leakage、MC-leakage 与 CR boundary variations 共同形成一个
CR definition/purity envelope，不再作为独立第四项重复平方和。当前负向 endpoint
`-0.006494652437` 来自 `abs(Delta phi)<=110 deg` 的 MC-leakage treatment，因此当前 accepted
method systematic 确实包含对 SPS MC leakage estimate 的依赖。

后续可考虑用数据约束、替代 generator/model 或更直接的 leakage validation 降低/替代该依赖；
本 request 没有改变已接受的 central 或 systematic definition。

## Presentation figures

- `H016-F01`：当前 accepted `f_DPS` 与三组 method systematic；新图，状态 `ready`。
- `H016-F02`：`sigma_DPS` 计算与 source-level breakdown；新图，preliminary。
- `H016-F03`：质量外推后的 `sigma_eff` 与 source-level breakdown；新图，preliminary。
- `H016-F04`：结论页并列 summary；新图，cross sections 标注 preliminary。
- `H016-F05`：精确复用 accepted H015 F07，展示 zero/MC-leakage variants 已进入同一 CR
  envelope；未复制图片。

精确路径、hash、尺寸、machine sources 和 caveat 见 `figure_manifest.csv` 与
`figure_manifest.md`。

## Dirty files、ownership 与 human gates

H016 intake 时 tracked dirty files、Git-visible untracked files 和 staged files 均为 0。H016
只拥有本 request copy 和 answer workspace；没有覆盖 frozen H014/H015 或 bootstrap outputs。

当前已由用户明确冻结：AN 五项百分数直接计算、不做归一化缩放；`sigma_eff systematic`
逐独立 source endpoint；`epsilon_m` 本轮作为固定 correction、暂不加入误差。

用户已明确批准本轮以统计独立近似 `rho=0` 展示 preliminary `sigma_DPS` 和 `sigma_eff`，并批准
AN 五项百分数直接传播、`sigma_eff` 逐源 endpoint 以及固定 `epsilon_m` correction。当前唯一流程
卡点是 pre-updates consumer re-review；真实 covariance 仍是后续优化项，但不阻塞本轮展示。
