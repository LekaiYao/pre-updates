> Lifecycle: archived on 2026-08-02. All indexed requests H008--H010 are completed and accepted; this file is historical routing evidence.

# H006 slides revision：跨项目 request 投递索引

## 请求发起方与对象

- 发起方：`pre-updates` slides consumer。
- 唯一外部请求对象：`../JPsiJPsi` 分析代码侧。
- 这些request不是让slides项目自行计算，也不是直接要求AN项目修改正文。

## 投递给 JPsiJPsi 的三个请求

### H008：control-region physics evidence

- requester正文：`pre-updates/docs/requests/archive/H008_JPsiJPsi_control_region_physics_evidence.md`
- JPsiJPsi接收职责：H006 control-region、SPS theory/Data comparison维护者
- producer目标路径：
  `JPsiJPsi/docs/requests/H008_preupdates_control_region_physics_evidence.md`
- producer回复：
  `JPsiJPsi/docs/answers/H008_preupdates_control_region_physics_evidence_response.md`

### H009：uncertainty and validation breakdown

- requester正文：`pre-updates/docs/requests/archive/H009_JPsiJPsi_H006_uncertainty_and_validation_breakdown.md`
- JPsiJPsi接收职责：H006 weights、statistics、closure、systematics、E4传播维护者
- producer目标路径：
  `JPsiJPsi/docs/requests/H009_preupdates_H006_uncertainty_validation_breakdown.md`
- producer回复：
  `JPsiJPsi/docs/answers/H009_preupdates_H006_uncertainty_validation_breakdown_response.md`

### H010：current AN nominal comparison

- requester正文：`pre-updates/docs/requests/archive/H010_JPsiJPsi_freeze_current_AN_nominal_comparison.md`
- JPsiJPsi接收职责：nominal SPS/DPS与sigma_eff事实源维护者
- producer目标路径：
  `JPsiJPsi/docs/requests/H010_preupdates_freeze_current_AN_nominal_comparison.md`
- producer回复：
  `JPsiJPsi/docs/answers/H010_preupdates_freeze_current_AN_nominal_comparison_response.md`

## 不创建request的内容

- 标题、讲解、页面重排：由 `pre-updates` 在依赖全部accepted后修改。
- 已存在的三个额外1D component-fit PDFs：走artifact handoff和验收，不重复request。
- AN文本更新：H010只要求JPsiJPsi冻结事实和冲突，未经用户确认不要求AN修改。

## 完成协议

```text
JPsiJPsi接收request
-> 在JPsiJPsi代码/输出中完成
-> JPsiJPsi/docs/answers回复精确路径、metadata、commit
-> progress登记ready
-> pre-updates验收
-> 用户physics gate
-> accepted
-> 一次性更新slides、编译和视觉QA
```
