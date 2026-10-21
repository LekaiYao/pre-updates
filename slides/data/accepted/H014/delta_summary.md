# H014 L0 delta summary

## 1. Dataset、candidate/sample与mixing source / unchanged
Change from 2026-08-07 accepted baseline: 无；仍为119个Data ntuples、6132 source
entries中选出2492 events，Jpsi1/Jpsi2 cross-slot且排除same-source。
Current conclusion: 6118202个Cartesian pairs中接受6061749个；all-pairs，无随机抽样。
Evidence and producer version: `selection_audit.txt`、`build_mixing.log`，sync/chensh-20260730@24823a5d476c18aee1f3134e86da645063965ef1。
Artifact status and path: ready；见`artifact_index.csv`。
Limitations / human gate: mixing依赖single-J prompt sWeights和nominal pair correction。

## 2. Selection、acceptance、efficiency与corrections / unchanged
Change from baseline: fiducial selection不变；`10<=pT(Jpsi)<=40 GeV`、
`abs(y)<2`、same PV、trigger/matching、`m(JJ)>=7.5 GeV`。
Current conclusion: nominal corrections继续施加；本轮没有重算其variation。
Evidence and producer version: unified input audit与mixing log，sync/chensh-20260730@24823a5d476c18aee1f3134e86da645063965ef1。
Artifact status and path: ready。
Limitations / human gate: acceptance/efficiency/correction variations为deferred/backup。

## 3. Single-J extraction与DPS construction / changed
Change from baseline: `abs(y)=1.2`两category nominal改为每slot一个calibrated global fit。
Current conclusion: 两阶段fit先校准resolution scales，再冻结scales做yield-only sPlot；
all-cross-event DPS construction不变。
Evidence and producer version: 两个global sPlot summaries，sync/chensh-20260730@24823a5d476c18aee1f3134e86da645063965ef1。
Artifact status and path: ready。
Limitations / human gate: base PDF functional forms仍固定；category dependence作为正式syst。

## 4. PP fit、CR和二维geometry / changed
Change from baseline: adaptive 14-cell改为单一CR的12-cell merged-dy geometry。
Current conclusion: 12/12 PP fits通过；CR为`abs(delta_y)>=1.8`且
`abs(delta_phi)<=pi/2`的一个cell，nominal DPS-only。
Evidence and producer version: PP summary、baseline cells/summary，sync/chensh-20260730@24823a5d476c18aee1f3134e86da645063965ef1。
Artifact status and path: ready。
Limitations / human gate: 2D alternative binning只作backup；旧metadata中的14-cell标签过时。

## 5. Internal nominal / changed
Change from baseline: `0.169980427756`改为`0.170423232645`。
Current conclusion: calibrated global被用户冻结为data-driven internal nominal；
`pT=15`和`abs(y)=1.2`为category variations。
Evidence and producer version: global summary/variations，sync/chensh-20260730@24823a5d476c18aee1f3134e86da645063965ef1。
Artifact status and path: producer-ready，用户physics gate已通过。
Limitations / human gate: 不替代CMS MC-template nominal；仍需consumer acceptance。

## 6. Statistical treatment / changed
Change from baseline: 废止500/529 successful-only spread和29次失败披露口径。
Current conclusion: 固定500个预定seeds、500/500成功、0失败、无replacement；
`SD=0.059331299623`已冻结为当前`f_DPS`全部statistical uncertainty。
Evidence and producer version: bootstrap summary/QA/submission metadata，sync/chensh-20260730@24823a5d476c18aee1f3134e86da645063965ef1。
Artifact status and path: ready。
Limitations / human gate: 500次对SD的MC精度0.001878不另加；下游covariance仍缺失。

## 7. Method systematic / changed
Change from baseline: provisional category+CR两组改为审核通过的category、CR/purity、
pure-DPS full-workflow closure三组。
Current conclusion: quadrature为`+0.010177290968/-0.011083850610`。
Evidence and producer version: variations.csv与closure metadata，sync/chensh-20260730@24823a5d476c18aee1f3134e86da645063965ef1。
Artifact status and path: user-frozen producer result，ready for consumer review。
Limitations / human gate: 是当前冻结scope的method systematic，不是所有detector/fit
uncertainties的穷尽清单；excluded/deferred见`systematic_breakdown.csv`。

## 8. Figures、projections与final values / changed
Change from baseline: 新增当前global maps和四个一维projection/template fits。
Current conclusion: 一维`f_DPS`为0.171939、0.171264、0.163517、0.170609；
只作formal cross-check，不进入systematic。正式结果见本页第5--7项。
Evidence and producer version: projection summary与12张PDF，sync/chensh-20260730@24823a5d476c18aee1f3134e86da645063965ef1。
Artifact status and path: ready；见`figure_manifest.csv`。
Limitations / human gate: 当前无bootstrap distribution或single-J fit presentation PDF；
H014不授权补画。
