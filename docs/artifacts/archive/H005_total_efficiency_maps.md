> Lifecycle: accepted historical manifest, archived on 2026-08-02. It is evidence, not current handoff status; use shared `../../../../docs/progress.md` for live state.

# H005：JJ total-efficiency maps

## 验收结论

状态：`accepted`

本次验收仅覆盖以下两张 central-value map：

1. SPS event-level total acceptance-times-efficiency map；
2. DPS event-level total acceptance-times-efficiency map。

两张 absolute statistical uncertainty map 未通过本次 slides 验收，不属于本
artifact。

## Accepted files

### SPS

- Producer path:
  `../JPsiJPsi/SKIM_tightfilter/SPS/ULPythia2016/CMSSW_10_2_5/src/4mu_acc_eff/AccEffMaps_out/Effevt_2016/recoeff2d_total_SPS_JJto4mu.pdf`
- SHA256:
  `2ad88b2758e508a8c63380b147d1448781193a716e7216e3b0f4d2151827f874`

### DPS

- Producer path:
  `../JPsiJPsi/SKIM_tightfilter/SPS/ULPythia2016/CMSSW_10_2_5/src/4mu_acc_eff/AccEffMaps_out/Effevt_2016/recoeff2d_total_DPS_JJto4mu.pdf`
- SHA256:
  `cc6364e169e7f62f5c77d48df45bdde246a74d8427f015bd3817dad3a55d666d`

AN 中的副本与 producer path 的 SHA256 一致，并由 AN commit `6345aed`
（`AccEff: add total efficiency maps`）纳入版本控制。

## 物理定义与标签

图中 quantity 是 event-level total acceptance times efficiency：

```text
[A_eta A_pT epsilon_RECO epsilon_ID epsilon_mumu]_1
* [A_eta A_pT epsilon_RECO epsilon_ID epsilon_mumu]_2
* epsilon_HLT * epsilon_evt
```

- 坐标轴：
  `pT(J/psi_1)` 与 `pT(J/psi_2)`，范围均为 10--40 GeV；
- 样本标签：
  `SPS` 或 `DPS`；
- 图面状态：
  `CMS Simulation Preliminary`，13 TeV；
- 色标：
  `Total efficiency`。

由于各 factor 不总是来自同一 generator sample，slides 不得把嵌入的 `SPS`
或 `DPS` 标签自行扩展成单一 generator 名称。

## Slides 使用边界

- 可以把两张 map 用于说明完整 acceptance-times-efficiency correction 的二维
  结构。
- 不从图中自行提取、四舍五入或发布 integrated efficiency。
- `11.7%`（SPS）和 `10.9%`（DPS）等总结数值只有经过用户确认后才可写入
  slides。
- 不将 conditional single-J/psi reconstruction efficiency 与本 artifact 的
  total event efficiency 混用。
- 不把逐 bin 波动解释为物理效应。

## 验收证据

- JPsiJPsi handoff：
  `../JPsiJPsi/docs/requests/archive/C005_AN_total_efficiency_update_request.md`
- JPsiJPsi response：
  `../JPsiJPsi/comments/preapproval/C005_total_efficiency/response.md`
- AN 引用位置：
  `../AN/ApxB_Acc_Eff_Maps.tex`
- AN provenance commit：
  `6345aed`

## 未接受内容

以下文件不属于本 artifact：

- `drecoeff2d_total_SPS_JJto4mu.pdf`
- `drecoeff2d_total_DPS_JJto4mu.pdf`

原因：当前渲染在顶部或左侧存在裁切，且逐 bin uncertainty 数字在 slides
尺寸下不可可靠阅读。如后续需要展示，须由 producer 提供修正版并重新验收。
