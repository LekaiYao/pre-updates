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
- 可通过 `.tex-internal-ids.json` 配置编号前缀，并启用 `.githooks/pre-commit`；
  检查暂存新增的 TeX 正文，命中时须将句子重写为面向听众的表述。
  此检查对扫描到的 backup 文字同样生效；需保留的复现编号放在注释或 provenance 中。
  新启用或变更前缀后运行 `--all` 检查既有内容，使用方法和局限见 README。

## 4. Update 计划与内容复用

- 修改既有 deck 前先建立两层实施计划，并在本轮更新完成前持续维护：
  1. 主要框架：叙事顺序、各单元目的和大致页数；
  2. 每约五页的细分：逐页目的、证据来源、图表、过渡和人工结论门禁。
- 两层计划均写入项目指定的计划文档；session 默认只输出主要框架，详细细分留在
  文档中供核对。本轮更新正式完成后按项目文档生命周期归档计划。
- 在没有明确增量更新要求时，新一轮 update 默认从零搭建：保留已批准的封面格式，
  删除旧版主体和 backup 叙事，再选择性复用经过核实的图、宏和布局组件。
- 确认 slides 内容或向代码项目提出需求前，先清点既有 figures、results、manifests
  和 accepted handoffs。已有产物足以支撑表述时直接复用，不重复生成。
- 新增 plot、analysis result、validation、training、fit、optimization、interface 或
  code-side run 必须先经人工判断；slide plan 或缺少展示材料本身不构成运行授权。

## 5. 单页排版迭代

- 人工逐页评审时，为目标 frame 设置稳定 `label`，使用 `fastcompile_frame.sh <label>`
  只编译该页，并检查 `tmp/<label>/` 中的 PDF 和 PNG。
- 布局修改严格限制在用户指定范围；若只要求移动或缩放图片，不主动重排相邻文字。
- overlay 或 `remember picture` 页面至少编译两次后再判断坐标；同时检查标题栏、页脚、
  图注和结论是否重叠，不能只依赖 LaTeX warning。
- 页面获得人工确认后再运行完整 fastcheck 和 `latexmk`。本轮更新正式收尾后清理 `tmp/`。

## 6. 人工批准的封面与结束页

- 已获人工批准的封面或结束页视为项目局部模板；后续 update 保留其标题层级、作者排序、
  reporter 标记、logo 尺寸与间距以及结束页信息框结构，不回退为通用默认布局。
- 通用 `main` 只保存格式、匿名占位符和 `figures/logos/` 通用资产库，不预选具体项目的
  人名、机构、日期或 logo 组合。每个分析在 `slides/project_setup.tex` 中填写
  `\analysisparticipants`、`\analysisreporter`、`\analysisdate` 和 `\analysislogos`。
- 多作者封面可采用以下匿名格式；姓名之间使用逗号加一个空格，只给 reporter 加下划线：

```tex
\author{%
  COLLABORATOR 1, \underline{REPORTER NAME}, COLLABORATOR 3\\[0.45em]
  YYYY.M.D%
}
\institute{}
\date{%
  \analysislogos
}
```

- logo 只按参与者 affiliation 选取，不因资产库中存在而全部展示。五个 logo 的 16:9
  起始几何为等高 `1.653cm`、间距 `0.30cm`；数量或长宽比变化后必须单页编译并检查
  总宽度、视觉重心和清晰度。封面只保留 `\titlepage`，不附加进度标签或第二副标题。
- logo 官方文件名与机构映射以 `figures/logos/README.md` 为准；不要恢复含义错误的
  `LU.png` 或 `TAU.png`。

- 结束页保留正常模板的顶栏和页脚，用全页宽度的 `makebox` 居中信息框；reporter 与日期
  使用相同字号：

```tex
\analysisclosing{closing}
```

`\analysisclosing` 固定保留正常模板顶栏、页脚、`0.68\textwidth` 居中信息框以及
reporter/date 同字号关系；内容自动读取 `slides/project_setup.tex`，不在结束页重复维护。

## 每版 Slides 的内容审核清单

- [ ] 每个主要叙事单元后都有 conclusion，或明确说明为何不需要。
- [ ] 所有 Codex 起草的 conclusion 已由分析人员标记为 `approved`。
- [ ] 每条结论均能追溯到已展示证据，没有超出当前分析成熟度。
- [ ] CMS 术语与 AN 或已审核 wording guide 一致。
- [ ] 主体 slides 中没有内部协作标签。
- [ ] 所有保留的分析局部标签在首次出现时都有读者可理解的定义。
- [ ] 两层 update 计划已维护，并在本轮完成后归档。
- [ ] 新增分析运行均有明确人工授权；可复用 artifacts 未被重复生成。
- [ ] 单页排版迭代已在确认后完成一次完整构建，并清理临时输出。
- [ ] 已批准的封面和结束页格式得到保留，通用模板中没有具体人员信息。
