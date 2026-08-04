> Lifecycle: completed and archived on 2026-08-02. The delivered artifact was accepted; current cross-project status is tracked only in shared `../../../../docs/progress.md`.

# H009 request：提供 H006 weights、method systematics 与截面误差的可审计 breakdown

## Request metadata

- Requester：`pre-updates`
- 明确接收对象：`JPsiJPsi` H006 weights、statistics、closure、systematics、E4维护者
- 执行仓库：`../JPsiJPsi`
- producer建议投递：`../JPsiJPsi/docs/requests/H009_preupdates_H006_uncertainty_validation_breakdown.md`
- producer回复：`../JPsiJPsi/docs/answers/H009_preupdates_H006_uncertainty_validation_breakdown_response.md`
- 结果目录：由JPsiJPsi在`tests/atlas_data_driven_sps/results/`下建立并提供manifest

- Request ID：`H009`
- Producer：`JPsiJPsi`
- Consumer：`pre-updates`
- 关联：H006
- 状态：`requested`
- 日期：2026-07-31

## 目标

为 slides 中 P9、P16--P22、P24 提供可以逐项解释和验收的 machine-readable
uncertainty/validation package。不得把现有 tested-variation envelope 表述为完整
ATLAS-aligned systematic。

## A. Component weights

当前 P9 只有中心值。请提供以下二者之一：

1. 推荐：14-cell `w_SPS/w_DPS` 的 marginal uncertainties 与完整 covariance/
   correlation matrix，明确包含和未包含：
   - Data PP fit covariance；
   - control-region normalization correlation；
   - source-event mixing covariance；
   - Data/mixed shared-source cross-covariance；
   - numerator/denominator correlation；
2. 若当前无法得到完整 covariance：提供 producer-approved 展示建议，明确 P9 只能
   作为 nominal construction schematic，不能作为无误差的定量测量图。

不得恢复 ROOT 默认 `sqrt(content)`。

## B. Statistical pseudoexperiments

请提供一份简洁 metadata/table，明确：

- toy input vectors和covariance；
- 每个toy实际波动什么；
- 每个toy重算哪些步骤；
- 哪些 nominal response/fits 被固定；
- 50,000 toys的输出量和statistical-error定义；
- Data-only与mix-only贡献；
- 当前未包含的covariance。

## C. Parametric closure

请明确记录：

- truth shapes来自 nominal SPS/DPS decomposition；
- mass-lifetime generator与fit model的关系；
- 同一truth下30 ensembles仅random seed/statistical fluctuations不同；
- bias、pull、coverage定义；
- `f_SPS=0.2` failure gate和9/30结果不可作无偏coverage估计；
- 该测试是implementation closure，不验证mixing shape或CR purity。

## D. Method variations 和 envelope

请交付一张 machine-readable breakdown table，每一行至少包含：

- category；
- nominal definition；
- alternative definition；
- 是否重跑2D PP fits；
- 是否重建mixing/templates/weights；
- 是否重跑四个1D component fits；
- reported `f_SPS/f_DPS`；
- signed/absolute shift；
- 是否被选作up/down envelope；
- 对应输出路径和commit。

必须详细列出：

- CR `Delta phi = 7pi/18, pi/2, 11pi/18`；
- CR `|Delta y| >= 1.8/2.4`；
- adaptive14/coarse10；
- mixing seeds；
- SPS leakage treatment。

并提供一张 ATLAS alignment matrix，区分：

- 已对齐/已评估；
- 部分对齐；
- 尚未评估。

至少覆盖 trigger、muon reconstruction、acceptance/efficiency、mass model、mass bias、
PP lifetime model、differential PP bias、pile-up、DPS model和binning。

当前 envelope 必须标为 `tested-variation method envelope`，除非新增分析完成并经用户
确认，不得称为 complete/final systematic。

## E. `sigma_DPS` 和 `sigma_eff` uncertainty breakdown

提供适合 slides 表格的逐项误差贡献，至少包括：

- `f_DPS` statistical；
- `f_DPS` tested-method up/down；
- CMS pair cross-section statistical；
- CMS pair non-BR systematic；
- 被移除的 correlated BF contribution；
- ATLAS single-J/psi statistical；
- ATLAS bin systematic；
- ATLAS luminosity；
- BR cancellation；
- 每项对 `sigma_DPS` 和 `sigma_eff` 的绝对/相对贡献；
- 组合公式及 correlation assumptions。

## 预期输出和状态

- CSV/JSON/TXT machine-readable breakdown；
-必要的PDF/table预览；
- metadata、生成脚本和Git commit；
- artifact先登记 `ready`；
- selection、fit、nominal、systematics和最终数字如有变化，必须提交用户确认。

## Consumer 验收

- 数值重算与代码一致；
- up/down方向和 `sigma_eff` 分母导致的交换正确；
- included/missing sources清楚；
- slides不会把当前systematic表述为完整评估；
- 用户确认后才可 `accepted`。
