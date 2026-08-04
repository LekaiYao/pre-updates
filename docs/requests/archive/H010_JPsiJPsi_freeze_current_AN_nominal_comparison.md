> Lifecycle: completed and archived on 2026-08-02. The delivered artifact was accepted; current cross-project status is tracked only in shared `../../../../docs/progress.md`.

# H010 request：冻结用于 slides 对比的当前 CMS AN nominal 结果

## Request metadata

- Requester：`pre-updates`
- 明确接收对象：`JPsiJPsi` nominal SPS/DPS与sigma_eff事实源维护者
- 执行仓库：`../JPsiJPsi`
- producer建议投递：`../JPsiJPsi/docs/requests/H010_preupdates_freeze_current_AN_nominal_comparison.md`
- producer回复：`../JPsiJPsi/docs/answers/H010_preupdates_freeze_current_AN_nominal_comparison_response.md`
- 说明：若代码重算值与AN当前值冲突，必须保留冲突并提交用户确认

- Request ID：`H010`
- Producer：`JPsiJPsi`
- Consumer：`pre-updates`
- 状态：`requested`
- 日期：2026-07-31

## 背景

用户要求在最终结果页将 H006 data-driven cross-check 与 CMS AN nominal 结果并列。
现有文档明确记录：

- AN 中 `sigma_eff = 1.59 mb` 是未更新的 stale value；
-代码侧曾按当前输入重算
  `1.26191 +/- 0.37057 (stat.) +0.64148/-0.11309 (syst.) mb`；
- 该重算值是否已经成为“当前 AN nominal”需要 producer 明确冻结，slides不能自行选择。

## 请求目标

请提供一份用户可验收的 current nominal comparison artifact，明确：

1. nominal 方法：two-template或three-template，使用哪个variable/fit；
2. nominal `f_SPS/f_DPS`；
3. nominal `sigma_SPS/sigma_DPS`；
4. nominal `sigma_eff`；
5. statistical和systematic uncertainties；
6. pair/single-Jpsi inputs、fiducial、BR和luminosity conventions；
7. 对应AN位置、代码输出、Git commit；
8. 哪些历史数字已经stale、不得引用。

## 预期输出

- 一张 machine-readable comparison table；
- 一段 producer-approved slides wording；
- 明确 status：是 current AN nominal、仅代码重算、还是尚未进入AN；
- artifact先登记 `ready`，不得直接标记 `accepted`。

## Consumer 验收

- 不将 stale 1.59 mb 作为 current nominal；
- 确认与 H006 的 fiducial 和 `sigma_eff` convention可比较；
- 若方法或相空间不一致，表格必须明确标注；
- 用户确认 nominal/final 数值后才可 `accepted` 并写入最终结果页。
