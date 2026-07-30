# Slides 内容治理与人工审核

本文件规定分析进展 slides 的内容治理方式。它与 Beamer 模板、编译和视觉检查
并列：模板保证“如何展示”，本文件约束“可以怎样表述”。任何分析结论仍由
分析人员负责，Codex 只负责起草和一致性检查。

## 1. 阶段性结论与人工门禁

- 每个完整叙事单元后加入一个简短的 `Interim conclusion`。通常每 4--6 页
  检查一次；如果 dataset、method、validation 或 fit 等阶段提前结束，则以
  阶段边界为准，不机械凑页数。
- Codex 起草的 conclusion 必须标记为
  `DRAFT -- needs physics approval`，未经人工审核不得视为正式物理结论。
- 每个 conclusion 最多 1--3 条，并依次回答：
  1. 前述页面已经建立了什么；
  2. 当前证据的限制或尚未完成的验证是什么；
  3. 由此得到的下一步问题或决定是什么。
- 每条结论必须能追溯到紧邻的前述页面及其权威数据来源。不得把相关性、模型
  表现、拟合变化或描述性指标自动提升为物理解释。
- 人工审核状态采用 `draft`、`approved` 或 `revise`。只有 `approved` 内容
  才能移除 draft 标记并进入正式报告。

## 2. CMS Analysis Note 用语

- CMS 分析用语以本分析的 Analysis Note（AN）及其人工审核结果为权威来源；
  Codex 不凭通用英文写作习惯创造物理术语或结论强度。
- 需要向 AN 维护方提出独立 request，提炼可复用的 CMS wording guide。建议
  至少覆盖：
  - observation、validation、interpretation 和 conclusion 的边界；
  - `agreement`、`closure`、`sensitivity`、`significance`、`performance`
    和 `preliminary` 等词的适用条件；
  - fit、data/MC comparison、systematic limitation 的常用句式；
  - AN 中的正面示例、应避免的表达及原因。
- wording guide 在人工审核后才可作为 slides 的语言依据。通用模板只规定
  “必须指定权威术语来源”，不自行固化某个分析的 CMS 表述。
- 在 guide 完成前，使用保守且可证实的措辞，如 `is consistent with`、
  `suggests` 和 `motivates further validation`；不得用 `proves` 等措辞替代
  尚未完成的物理验证。

## 3. 通用定义与内部标签

所有标签按读者可理解程度分为三级：

| 类型 | 示例 | Slides 中的处理 |
|---|---|---|
| 通用物理概念 | 标准 observable、selection、fit quantity | 可以使用；首次出现时按需定义 |
| 分析局部但可解释的标签 | 某个 reweighting configuration | 仅在首次出现时同时给出简短定义 |
| 内部协作标签 | request ID、handoff ID、task 编号、原始 train tag、文件路径 | 主体 slides 中禁止出现 |

- 判断标准是：第一次参加报告的物理分析人员能否仅凭当前页面理解，而不是
  项目成员是否熟悉该标签。
- 自解释的局部标签仍需在首次出现时说明，例如
  `R5: five-variable reweighting configuration`。
- 复现所必需的内部标识优先保存在源码注释或 provenance 记录；确需展示时只
  放在 backup，并解释其物理或技术含义。
- 交付前检查内部编号、request/task ID、原始路径和未解释的配置标签。具体
  denylist 由每个分析项目维护，不写死在通用模板中。

## 每版 Slides 的内容审核清单

- [ ] 每个主要叙事单元后都有 conclusion，或明确说明为何不需要。
- [ ] 所有 Codex 起草的 conclusion 已由分析人员标记为 `approved`。
- [ ] 每条结论均能追溯到已展示证据，没有超出当前分析成熟度。
- [ ] CMS 术语与 AN 或已审核 wording guide 一致。
- [ ] 主体 slides 中没有内部协作标签。
- [ ] 所有保留的分析局部标签在首次出现时都有读者可理解的定义。
