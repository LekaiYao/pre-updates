# 项目规则

## 共享状态规则

- 开始跨项目任务前读取 `../docs/progress.md` 和 `../docs/roadmap.md`。
- Slides 的输入只能来自状态为 `accepted` 的 artifact；`planned`、`ready` 或其他状态的 artifact 只能用于验收，不能写入 slides。
- 完成重要节点后，只更新本项目产生的状态和 handoff。
- 已有 artifact 的交付不新建 request；需要对方新增工作才建立 request。
- 不修改其他项目的业务文件或由其他项目负责的物理结论。
- selection、fit、nominal、systematics 和最终数值必须经过用户确认。
- 共享摘要与代码或 artifact 冲突时，以代码、metadata、Git commit 和实际输出为准，并修正摘要。


## 文档生命周期

- `../docs/progress.md` 是跨项目日常状态、活跃 handoff 和 open request 的唯一总入口；本项目文档不复制这些实时状态。
- open request 必须在共享 `progress.md` 有索引；完成后立即移入本项目 `completed/` 或 `archive/`，answer 随同归档。
- 已收口的阶段性 implementation plan 和 accepted artifact manifest 归档保存，不继续充当当前状态。
- 本项目 handoff 只保留接手 slides 所需的当前实现或写作事实；历史证据保留在 archive，不删除。
