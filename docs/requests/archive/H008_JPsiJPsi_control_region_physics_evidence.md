> Lifecycle: completed and archived on 2026-08-02. The delivered artifact was accepted; current cross-project status is tracked only in shared `../../../../docs/progress.md`.

# H008 request：为 H006 control region 提供可解释的物理证据

## Request metadata

- Requester：`pre-updates`
- 明确接收对象：`JPsiJPsi` H006 control-region、theory/Data comparison维护者
- 执行仓库：`../JPsiJPsi`
- producer建议投递：`../JPsiJPsi/docs/requests/H008_preupdates_control_region_physics_evidence.md`
- producer回复：`../JPsiJPsi/docs/answers/H008_preupdates_control_region_physics_evidence_response.md`
- 结果目录：由JPsiJPsi在`tests/atlas_data_driven_sps/results/`下建立并回复精确路径

- Request ID：`H008`
- Producer：`JPsiJPsi`
- Consumer：`pre-updates`
- 关联：H006 ATLAS-style data-driven SPS/DPS cross-check
- 状态：`requested`
- 日期：2026-07-31

## 背景

slides 计划在 normalized mixed-DPS map 前增加一页，用于说明为什么

```text
|Delta y| >= 1.8 && |Delta phi| <= pi/2
```

被视为 DPS-dominated control region。

现有何老师 SPS theory comparison 是单位面积 shape，且 theory fiducial、单位和
normalization 定义尚未全部确认。单位面积 SPS shape 与 data-driven SPS shape 的比较
不能证明 total Data 在高 `|Delta y|` 区域由 DPS 主导。

## 请求目标

请提供可以支持或限制“高 `|Delta y|`、低 `|Delta phi|` 为 DPS dominated”的
accepted physics artifact。优先目标是：

- measured total prompt-prompt differential cross section
  `d sigma_PP / d|Delta y|`；
- SPS theory absolute differential prediction
  `d sigma_SPS / d|Delta y|`；
- 使用相同 fiducial region、binning、branching-fraction 和单位；
- 图中标出 nominal control-region 的 `|Delta y| >= 1.8` 部分，并明确一维投影没有
  包含 `|Delta phi| <= pi/2` 时不能等价为完整二维 CR purity。

## 必须先解决的定义

在制作 absolute comparison 前，请冻结并记录：

1. theory fiducial region；
2. prediction 是否包含 prompt feed-down；
3. differential values 是 bin integral 还是 density；
4. 单位及 branching-fraction convention；
5. theory central/upper/lower 的定义；
6. Data PP cross section 的 correction、binning 和 covariance；
7. theory 与 Data 是否确实处于同一 collision energy 和 phase space。

若以上条件不能满足，不得把两个绝对量画在同一图中，也不得用当前单位面积 shape
comparison 声称 CR 为 DPS dominated。

## 替代交付

若 absolute theory/Data comparison 当前不可定义，请改为交付一份明确的
control-region validation package，至少包含：

- Data PP 与 mixed-DPS 在多个互斥 `|Delta y|`/`|Delta phi|` regions 的 yields；
- nominal及替代CR的归一化比例；
-现有SPS leakage estimate及其来源；
- 当前能声称和不能声称的内容；
- 推荐 slides 只作定性说明的图或表。

## 预期输出

- 一张 presentation-ready PDF，或说明为何不能制作的 physics note；
- machine-readable values；
- metadata：定义、输入路径、生成脚本、Git commit；
- CR shading/selection 的精确定义；
- artifact 状态先登记为 `ready`，不得直接设为 `accepted`。

## Consumer 验收

- 核对绝对单位、fiducial、binning和BR convention；
- 核对 Data/theory不是仅由各自单位面积归一化得到；
- 确认一维 `|Delta y|` 图不会被表述为完整二维CR purity measurement；
- 用户确认物理口径后才可 `accepted` 并用于 slides。

## 职责边界

该request不授权改变 nominal CR、selection、theory definition 或最终 fraction。
如比较显示当前CR假设需要改变，必须另行提交用户 physics gate。
