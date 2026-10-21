# H014 producer answer：最新 data-driven internal nominal 与误差

状态：`ready`。本 package 只整理已经完成且由用户冻结的分析结果；没有新增或重跑
fit、bootstrap、systematic variation 或 plot。pre-updates consumer review 尚未完成，
所以 `ready` 不等于 slides `accepted`。

## 直接结论

当前 data-driven 方法内部的用户冻结结果是：

`f_DPS = 0.170423232645 +/- 0.059331299623 (stat.) +0.010177290968/-0.011083850610 (method syst.)`

slides 推荐写为：

`f_DPS = 0.170 +/- 0.059 (stat.) +0.010/-0.011 (method syst.)`

它是正式的 data-driven cross-check/internal nominal，不替代 CMS MC-template nominal
`f_DPS=0.34 +/-0.10 (stat.) +0.02/-0.17 (syst.)`。

相对2026-08-07 H011 baseline，central从按`abs(y)=1.2`分category的
`0.169980427756`改为同构的calibrated global single-J fit；二维几何从adaptive
14-cell改为单一CR的12-cell；bootstrap从500/529 successful-only改为固定500个
预定seeds、500/500成功且0 replacement；method systematic从category+CR的
provisional两组扩展为category、CR definition/purity和pure-DPS full-workflow closure
三组，经用户审核后quadrature。

## 当前状态和边界

- dataset、fiducial selection、2492个selected source events、cross-slot all-pairs
  mixing及6061749个accepted mixed pairs不变。
- single-J nominal改为每个slot各自做一个calibrated global两阶段fit：先校准
  mass/ctau resolution scales，再冻结scales做yield-only sPlot。
- 12-cell平面中的CR为`1.8<=abs(delta_y)<=4`且
  `0<=abs(delta_phi)<=pi/2`的单一cell；CR nominal假设为DPS-only。
- 正式method systematic只组合三组：single-J category、CR definition/purity、
  pure-DPS MC full-workflow closure。2D binning和四个一维投影均不纳入。
- acceptance/efficiency/correction和原4D fitter的逐bin variations保持
  deferred/backup；BR、luminosity和global normalization不属于`f_DPS`专属误差。
- pure-DPS closure在当前workflow中按用户决定假设现有DPS MC可用；feeddown/generator
  composition的独立研究仍冻结。
- `f_DPS`统计误差已完整冻结；但把结果传播到`sigma_DPS`时，和pair-total
  estimator的replica-matched covariance仍缺失。

## QA

固定bootstrap为500/500成功、0失败、0 replacement；1000/1000 single-J
calibrations、1000/1000 frozen-scale yield fits和6000/6000 PP cells通过。
四个一维projection cross-check另有78/78 component fits和4/4 template fits通过。

## Provenance差异

实际结果以`tests/atlas_data_driven_sps/results/fdps_systematics_global_nominal_v1/summary.txt`、`cells.csv`和bootstrap metadata为准。
两个旧metadata字段已过时但未回写：`tests/atlas_data_driven_sps/results/fdps_systematics_final_v1/category/global_calibrated/metadata.txt`仍记录
`nominal_changed=false`，而用户随后已经冻结global nominal；
`tests/atlas_data_driven_sps/results/fdps_systematics_final_v1/category/global_calibrated/templates_2d/metadata.txt`仍写`adaptive_14_cells`，实际当前输入和
输出明确为12 cells。这两处不改变数值，consumer不得据此回退定义。

## 下游数值

旧H013的`sigma_DPS=6.3233 pb`和`sigma_eff=2.5145 mb`使用已废止的H011 central，
不应直接进入新slides。仅替换central后，算术中心为
`sigma_DPS=6.339744254394 pb`和`sigma_eff=2.507994333641 mb`；它们尚未完成
新的下游statistical covariance和完整uncertainty gate，只能作为central-only
reference，不应包装成新的最终下游测量。

## Consumer gate

用户已完成producer-side physics gate，接受当前central、stat、三组method systematic
以及一维投影只作cross-check的定位。pre-updates仍须核对本package的hash、路径和
wording，并将所选artifacts转为accepted后才能写入新deck。
