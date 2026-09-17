# Repository Workflow

本仓库定位为个人维护的分析 slides 项目：`main` 保存可复用框架，每个具体分析
使用一个长期 branch。该模型允许在真实分析工作中发现并提炼通用能力，不要求
另开一个脱离分析背景的模板维护 session。

## Branch 模型

```text
main
├── 通用 Beamer 框架和最小示例
├── 通用宏、主题和构建命令
├── PDF/视觉检查入口
└── 通用内容治理规则

analysis/x
└── X-specific slides、图片引用、术语、数据来源和审核结论

analysis/jj
└── JJ-specific slides、图片引用、术语、数据来源和审核结论
```

后续分析使用 `analysis/<name>` 命名。branch 表示长期并存的分析实例，不用于
替代短期 feature branch。

## Main 与分析 Branch 的协作

### 从 main 同步通用更新

通用能力先作为独立 commit 进入 `main`，再 merge 到需要它的分析 branch：

```bash
git switch analysis/jj
git merge main
```

稳定的通用框架可以使用 `template-vX.Y` tag 标记，便于记录各分析采用的基础
版本。

### 从具体分析提炼通用能力

在分析 branch 中发现可复用改进时：

1. 区分通用实现与分析业务内容；
2. 将通用实现整理成单独 commit；
3. 将该 commit cherry-pick 到 `main`；
4. 在 `main` 上验证最小示例仍可独立构建；
5. 再由 `main` merge 到其他分析 branch。

不得把整个 `analysis/<name>` merge 回 `main`。这会把分析数字、图片路径、
局部术语和内部标签带入通用框架。

## 内容归属

属于 `main`：

- Beamer 主题、布局和通用宏；
- `latexmk`、fastcheck 和 PDF 视觉检查流程；
- `SLIDES_GUIDE.md` 等通用内容治理规则；
- 不依赖具体分析数据、可独立编译的最小示例。

属于 `analysis/<name>`：

- 分析叙事、物理数字、图和外部路径；
- Analysis Note 及其他权威数据来源的连接规则；
- 分析局部术语和 internal-label denylist；
- conclusion 的人工审核状态和报告版本。

## Worktree 建议

多个 Codex session 并行工作时，不在同一目录频繁切换 branch。为长期 branch
建立独立 worktree：

```text
pre-updates-main/  -> main
pre-updates-x/     -> analysis/x
pre-updates-jj/    -> analysis/jj
```

这样每个 session 固定在一个分析上下文中，同时共享同一 Git object database。

## 历史初始化步骤（已完成）

以下步骤记录仓库初始化过程，现已完成，不应作为当前待办重新执行。

### 第一步：建立可回退的 X 基线

当前工作区包含已经可用的 X slides，而 `main` 尚无 commit。首先应完整盘点拟
纳入版本控制的文件，排除编译产物和临时文件，然后把当前状态保存为一个明确的
X 基线。此步骤的目标是确保后续提取通用 `main` 时，现有 slides 不会丢失且
能够随时恢复。

第一步只解决“保存现状”，暂不同时重构目录、连接 remote 或初始化 JJ。

### 第二步：形成通用 main

- 从已保存的 X 基线识别通用文件；
- 在 `main` 中保留通用框架、治理规则和最小可编译示例；
- 移除 X-specific 数字、路径、术语和图片依赖；
- 完成 fastcheck、完整编译和 PDF 视觉检查。

### 第三步：建立分析 branches

- 从通用 `main` 创建 `analysis/x`；
- 恢复 X-specific slides 并验证最终 PDF；
- 从同一个 `main` 创建 `analysis/jj`；
- 在 JJ branch 中加入 JJ-specific 配置和第一套 slides。

### 第四步：连接 GitHub

- 确认目标 GitHub repository；
- 配置 `origin`；
- 先推送 `main`，再推送分析 branches 和稳定 tag；
- 核对 GitHub 默认 branch 和 branch 列表。

连接远端不应与历史重组混在同一步，以便在推送前本地检查最终结构。

### 第五步：运行一次双向提炼

- 在 JJ 制作首套 slides；
- 将经验证的通用改进以独立 commit 回收到 `main`；
- 将新的 `main` merge 到 X；
- 记录冲突和重复操作，再决定是否增加自动检查或辅助脚本。

## 每次通用改进的检查

- [ ] commit 不包含任何分析数字或图；
- [ ] 不包含分析专用路径、AN 章节或内部标签；
- [ ] `main` 的最小示例能够独立 fastcheck 和完整编译；
- [ ] 修改同步到分析 branch 后没有覆盖分析局部配置；
- [ ] 如有行为变化，README 和 `SLIDES_GUIDE.md` 已同步更新。
