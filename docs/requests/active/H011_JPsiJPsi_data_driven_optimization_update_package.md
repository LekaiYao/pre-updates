# H011 request：data-driven 优化进展、当前方案与部分误差的 presentation package

## Request metadata

- Request ID：H011
- Requester / consumer：pre-updates
- Producer / fact owner：JPsiJPsi
- 状态：requested
- 日期：2026-08-07
- Requester 文件：pre-updates/docs/requests/active/H011_JPsiJPsi_data_driven_optimization_update_package.md
- Producer answer workspace：JPsiJPsi/docs/answers/H011_preupdates_data_driven_optimization_update/
- 关联基线：上一轮已验收的 ATLAS-style data-driven SPS/DPS cross-check
- Human gate：selection、fit、data-driven nominal、systematics 和最终数值仍须用户确认

## 背景与职责边界

pre-updates 将制作一轮新的 JJ 内部 update。当前阶段不预设 slides 页数、主要进展
或页面顺序；codes 先基于当前代码、metadata、Git commit 和实际输出提供完整进展
package，slides 再判断叙事和图片覆盖。

这里的 data-driven nominal 指 data-driven 方法内部当前选择的 central scheme。
除非后续经过新的用户 physics gate，不得将其表述为替代 CMS MC-template nominal。

本 request 授权 codes 汇总、核对和组织现有事实与 artifacts，不授权新增 analysis run、
fit、bootstrap production、plot 或物理定义修改。发现缺口时只提交建议和必要性，
等待单独人工批准。

## A. 完整盘点上一轮后的优化尝试

请从上一轮 accepted data-driven cross-check 的代码/输出基线开始，完整列出之后所有
相关优化和研究路线，不按 slides 需求预先筛选。至少为每项记录：

- 要解决的物理或方法问题；
- 相对上一轮改变的代码、配置或 estimator；
- 实际运行范围和 completion status；
- central value、closure、fit success、stability 或其他直接 evidence；
- 当前限制、失败模式和未完成验证；
- 保留、放弃、降级为 diagnostic 或继续研究的判断；
- 精确代码、metadata、结果路径和 Git commit。

请由 codes 判断哪些属于主要进展，并给出排序及判断依据。slides 侧不会预先指定
哪些路线必须成为主文内容。

## B. 冻结当前 data-driven nominal 的事实定义

请明确当前 codes 推荐或暂定使用的 data-driven central scheme，并逐项记录：

- candidate construction 和 event-mixing 定义；
- source-event/slot/category treatment；
- all-pairs 或 sampling 规则；
- selection、control region 和二维 binning；
- PP fit、SPS/DPS decomposition 和 normalization；
- reported estimator 及一维 projection treatment；
- central value；
- 相对上一轮方案和其他候选方案的差异；
- 推荐该方案的证据；
- 当前状态是 provisional、pre-freeze 还是可提交用户冻结。

当前 handoff 中记录过 global、pT category、abs(y) category、all-cross-event pairs、
control-region variations 和 source-event bootstrap 等工作。请不要直接复制摘要；
须以实际代码、metadata、Git commit 和输出重新核对，并修正任何过时描述。

## C. 当前已计算的统计和部分系统误差

请提供 machine-readable breakdown，并明确可报告范围：

- statistical inputs、resampling unit、toy/bootstrap procedure 和 estimator；
- successful/failed attempts、failure categories 及其对选择偏差的风险；
- central value、mean、sample SD、quantiles 和任何 bias diagnostic；
- codes 当前是否认为 statistical uncertainty 可冻结；若不可，能安全报告什么；
- 已完成的 category、control-region、model 或其他 tested variations；
- 每项 signed/absolute shift 与 envelope treatment；
- included、excluded 和尚未评估的 uncertainty sources；
- covariance/correlation assumptions 和组合规则；
- 哪些只能称为 provisional statistical spread、tested-method variation 或 partial
  systematic，不能称为 final/complete systematic uncertainty。

不得为满足 request 自动恢复失败 replica、增加新 variation 或重新运行 production；
如 codes 判断这些工作是冻结误差的必要条件，请列出独立后续建议。

## D. 重要图片与可复用 artifact inventory

请提供所有 codes 认为对理解主要进展重要的现有图片，而不是只给一张摘要图。
每张候选图至少记录：

- 精确路径、文件格式和 SHA256；
- 生成代码、配置、commit 和日期；
- 图中物理量、selection、单位与 normalization；
- 它支持的结论、可安全使用的 wording 和必须保留的 caveat；
- 推荐级别：主要进展必须展示、重要支持、仅 backup/diagnostic；
- 是否已有 machine-readable source。

最终主文/backup 分配和页数由 pre-updates 在收到完整 package 后决定。若现有重要结果
没有 presentation-ready 图，只列出缺口和建议，不自动制作新图。

优先复用上一轮 accepted maps、component fits、control-region validation、statistical
propagation、tested-variation breakdown 和 nominal-comparison artifacts；若它们已被
新结果取代，请明确 superseded relationship，不覆盖或删除历史产物。

## E. Producer 推荐内容

请提供一份不含内部 request/handoff/task 编号的 reader-facing 内容摘要：

- 上一轮之后最重要的进展；
- 当前 data-driven central scheme；
- 当前可以报告的统计和部分系统误差；
- 仍未解决的限制和下一步。

该摘要是 codes 的推荐材料，不是最终 slides wording，也不替代用户 physics gate。

## 预期交付

在 producer answer workspace 中提供：

1. answer.md：直接结论、主要进展判断及限制；
2. progress_inventory.csv 或等价 machine-readable 表；
3. nominal_definition.txt/json；
4. uncertainty_breakdown.csv/json；
5. figure_manifest.csv/md，覆盖所有重要现有图片；
6. 精确 source paths、metadata、Git branch/commit 和复现入口；
7. 若需要新增工作，单独列出 proposed follow-ups，不执行；
8. artifact/handoff 状态先设为 ready，不得直接设为 accepted。

若全部内容可由现有 metadata/CSV/PDF 直接组成，可用 manifest 引用原文件，不复制或
重新生成相同 artifact。

## Consumer 验收条件

pre-updates 将在 codes 交付后：

- 对照代码、metadata 和实际输出核对进展清单；
- 核对 codes 的主要进展判断与直接 evidence；
- 核对 data-driven nominal 的完整定义和 provisional/frozen 状态；
- 核对统计与部分系统误差的 included/missing 范围；
- 检查所有重要图片均进入候选 inventory；
- 将 nominal、systematics 和最终数值提交用户确认；
- 仅在 artifact 转为 accepted 后制定真正的两层 slides 页面计划并消费内容。
