# Slides 制作与跨项目协作能力测试归档

状态：`completed`

归档日期：2026-07-30

## 测试目标

- 验证 `pre-updates` 能作为独立 slides consumer 接入共享协作流程；
- 验证 slides 只消费状态为 `accepted` 的 artifact；
- 验证 `ready -> consumer 验收 -> accepted -> slides 引用` 的 handoff 闭环；
- 验证 Beamer 制作、编译、PDF 逐页视觉检查和人工 physics gate。

## 已完成

- 建立项目级 `AGENTS.md` 和 accepted-only 输入规则；
- 验收 H005 SPS/DPS event-level total acceptance-times-efficiency central-value maps；
- 建立 H005 artifact manifest，并复制哈希一致的 accepted PDF；
- 在 `slides/main.tex` 中制作标题页和 5 页首批内容；
- 通过 fastcheck、完整 `latexmk` 编译和 6 页 PDF 视觉检查；
- conclusion 保留 `DRAFT -- needs physics approval`；
- 未将 integrated efficiency、未接受的 uncertainty maps 或未确认物理结论写入 slides。

## 验证结论

Slides 制作能力和 JJ 分析内部子项目间的 artifact/handoff 协作机制已经完成基本
验证。本测试到此收口，不继续扩展为完整 8--12 页分析报告。

## 保留边界

- 两张 uncertainty maps 未纳入本次 accepted artifact；这不再是本测试的阻塞项。
- 当前 slides 是能力验证产物，不代表完整分析报告或最终物理结论。
- 后续真实报告任务应重新读取共享状态，仅消费当时有效的 accepted artifacts，
  并重新经过用户 physics gate。

## 归档产物

- `docs/artifacts/archive/H005_total_efficiency_maps.md`
- `slides/main.tex`
- `slides/project_setup.tex`
- `slides/figures/accepted/H005/`
- `build/main.pdf`（本地编译产物，不提交 Git）
