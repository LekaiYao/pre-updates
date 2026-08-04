> Lifecycle: completed initial implementation plan, archived on 2026-08-02.

# JJ Slides：从 Clone 到第一版分析总结

本文件交给 JJ 侧 Codex CLI 使用。目标是优先生成一套能够与分析人员讨论的
初版 Beamer 报告，再从真实使用中提炼通用模板改进；不要在第一轮投入大量时间
重构框架或追求最终视觉效果。

## 目标产物

- 工作 branch：`analysis/jj`
- Beamer 源码：`slides/main.tex`
- 编译产物：`build/main.pdf`（不提交 Git）
- 建议规模：第一版约 8--12 页，以已有、可验证材料为限
- 内容状态：允许不完整，但不得使用猜测数字或伪造占位结果
- conclusion：Codex 可以起草，必须保留
  `DRAFT -- needs physics approval`，等待人工审核

## 1. Clone 与环境确认

```bash
git clone https://github.com/LekaiYao/pre-updates.git
cd pre-updates
git switch analysis/jj
git status --short --branch
```

开始编辑前阅读：

1. `README.md`
2. `SLIDES_GUIDE.md`
3. `REPOSITORY_WORKFLOW.md`
4. 本文件

确认以下命令可用：

```bash
pdflatex --version
latexmk --version
bash fastcheck_slides.sh
latexmk -pdf -outdir=build slides/main.tex
```

clone 后的所有制作、核查、编译和提交工作由 JJ 侧 Codex CLI 完成。

## 2. 先盘点 JJ 权威材料

在改 slides 前，对用户指定的 JJ 分析目录做只读盘点，至少确认：

- Analysis Note、内部说明或最新进展文档；
- 当前使用的 signal/background process 和 dataset；
- generation、simulation、reconstruction、selection 的实际状态；
- 已经完成且可引用的 plots、tables、logs 和数值；
- 当前仍未完成或存在争议的事项；
- 内部 task/tag 与报告中应使用的通用定义之间的映射。

信息优先级：

1. 用户确认的物理理解；
2. 当前 Analysis Note 或正式文档；
3. 可复现的代码、配置和输出；
4. 日志和内部进展记录。

如来源之间冲突，先记录差异并向用户说明；不要自行选择一个数字写入 slides。
未经用户对当次任务明确授权，不修改 JJ 分析源项目，只在 slides repo 中工作。

建议先生成一份短 inventory，包含：

| 内容 | 权威来源 | 可否进入首版 | 缺口 |
|---|---|---|---|
| Physics goal | AN/用户确认 | Yes/No | |
| Samples/datasets | config/bookkeeping | Yes/No | |
| Production status | logs/output | Yes/No | |
| Selection/reconstruction | code/AN | Yes/No | |
| Current plots/results | verified output | Yes/No | |

## 3. 形成第一版结构

根据实际材料选择页面，不为了满足模板而虚构内容。建议起点：

1. **Title and scope**：本次报告覆盖到哪一步；
2. **Physics motivation**：要回答的物理问题；
3. **Process definition**：signal、background 和关键 final state；
4. **Dataset / MC samples**：已确认的数据和模拟样本；
5. **Production chain**：generation 到 analysis ntuple 的当前状态；
6. **Selection or reconstruction**：已有的主要定义；
7. **Current validation/results**：每页一项主要图或结果；
8. **Interim conclusion**：已经建立什么、限制是什么、下一步是什么；
9. **Immediate next steps**；
10. **Backup**：配置细节、额外诊断或 bookkeeping。

如果当前只有 production 和 AN 内容，可以先制作“analysis setup + production
status”报告，不必等待最终拟合或物理结果。

## 4. 内容与语言规则

- 每个数字、状态和物理判断都要能指回 inventory 中的权威来源。
- CMS 用语优先复用 JJ Analysis Note 已有表述；避免把技术观察提升为物理结论。
- 内部 request ID、job tag、handoff ID 和目录名不得直接作为 slide 定义。
- 确需保留的局部标签，首次出现时给出读者可理解的说明。
- 每 4--6 页或每个分析阶段结束时检查是否需要 `Interim conclusion`。
- Codex 起草的 conclusion 不得自行移除人工审核标记。
- 第一版优先可读性：一页一个主要信息，复杂多 panel 图拆页展示。

## 5. 制作与 QA

按小批次修改 `slides/main.tex`：

```text
盘点来源
  -> 拟定 8--12 页 outline
  -> 用户确认主要叙事
  -> 制作首批 4--6 页
  -> fastcheck + 完整编译
  -> 补齐剩余页面
  -> PDF 逐页视觉检查
  -> 人工审核 conclusion
```

构建命令：

```bash
bash fastcheck_slides.sh
latexmk -C -outdir=build slides/main.tex
latexmk -pdf -outdir=build slides/main.tex
```

最终检查：

- 无 LaTeX error、undefined control 或缺图；
- PDF 页数、页脚和 16:9 比例正确；
- 无裁切、重叠、过小文字或不可读图例；
- 没有内部协作标签泄漏到主体 slides；
- draft conclusion 明确等待人工审核；
- Git 中不包含 `build/`。

## 6. Git 提交与通用能力回流

JJ 内容直接提交到 `analysis/jj`：

```bash
git add <明确的 slides 文件>
git commit -m "生成 JJ 分析首版进展报告"
git push
```

第一版完成前不要把 JJ-specific 内容 merge 到 `main`。

如果制作过程中发现真正通用的改进，例如：

- 新的通用 layout helper；
- 更可靠的 fastcheck；
- conclusion 审核组件；
- 与分析无关的视觉修复；

先在 `analysis/jj` 中将其整理为不包含 JJ 数字、路径和术语的独立 commit，
记录 commit SHA；首版报告完成后再决定是否 cherry-pick 到 `main`。

## 给 JJ Codex CLI 的启动 Prompt

```text
你正在初始化 JJ 分析的 slides 项目。

请先阅读 README.md、SLIDES_GUIDE.md、REPOSITORY_WORKFLOW.md 和
JJ_FIRST_REPORT_PLAN.md，并确认当前 branch 为 analysis/jj。

目标是基于用户指定的 JJ Analysis Note、代码输出和进展文档，尽快制作一套
8--12 页的初步分析总结。先只读盘点权威材料并给出简短 inventory 和 slide
outline；不要猜测数字，不要把内部 task/tag 直接写进 slides，也不要修改
slides repo 之外的文件。outline 经用户确认后，再修改 slides/main.tex，
运行 fastcheck、完整 latexmk 编译，并逐页检查 PDF。

每个阶段性 conclusion 可以由你起草，但必须标记
DRAFT -- needs physics approval，等待人工审核。优先完成可讨论的第一版，
暂不做大规模模板重构；发现通用改进时将其与 JJ-specific 内容分开记录。
```
