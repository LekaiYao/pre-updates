# JJ data-driven optimization update：active slide plan

状态：页面计划和主要 physics wording 已于 2026-08-07 获用户批准。Codes package
H012 metadata-only 修正已于 2026-08-07 通过 consumer 复核，H011 artifacts 已转为
`accepted`。正式 slides 制作可以进入下一阶段；本次验收尚未归档旧 deck、复制新
artifacts 或修改 `slides/main.tex`。

规划假设：JJ analysis-group internal update，约 25--30 分钟；主文约 23 页，
backup 约 7 页。报告时长和受众需由用户确认，页数随后可等比例压缩或扩展。

## 第一层：主要框架

1. **Title（1 页）**：复用已批准的标题页格式与作者/logo 几何，只更新经确认的
   日期和 update 标题。
2. **Recap：问题、旧方法和未决假设（4 页）**：用 accepted 历史 artifacts 回顾
   data-driven cross-check 的目标、旧 event-mixing 链、二维分解和主要局限；不重复
   旧 deck 的逐页叙事。
3. **主要方法升级（5 页）**：single-J prompt purification、slot-specific fits、
   cross-slot mixing、deterministic all-pairs 和 kinematic category treatment。内容等待
   H011 accepted 后写入。
4. **当前 central decomposition 与投影（6 页）**：逐张展示 PP、mixed-DPS、
   data-driven SPS central maps，并展示全部六张 codes 标为 important-support 的
   component figures。页面结论明确 central status 和 signed subtraction caveat。
5. **统计与暂定 systematic（4 页）**：category comparison、CR boundary sensitivity、
   bootstrap distribution summary 和 uncertainty coverage matrix；500-success bootstrap
   SD 称为 `stat`，category/CR group envelopes 组合为暂定 `syst` 并拆分解释。只使用
   已有 CSV/metadata 制作原生表格，不补造 distribution plot。
6. **Status、takeaways 与 next steps（2 页）**：区分 validated、provisional、missing，
   重申不替代 CMS MC-template nominal，并列出进入 freeze 所需决策。
7. **Thanks（1 页）**：复用已批准的 thanks 格式。
8. **Backup（约 7 页）**：central diagnostic maps、yield projections、DPS-MC benchmark、
   必要的 accepted historical validation 和 bootstrap technical definition；stale nominal
   comparison 永不展示。

## 第二层：每五页详细拆分

### P1--P5：标题与 recap

- **P1 Title**：批准的 title pattern；证据为当前 `slides/project_setup.tex`；结论 gate：
  日期和标题由用户确认。
- **P2 Physics question**：为何需要 data-driven SPS/DPS cross-check；用 CMS nominal
  与 data-driven role 的已 accepted 文字边界，不引入新数值。
- **P3 Previous construction**：selected candidates → event mixing → CR normalization →
  SPS subtraction 的紧凑流程图；证据为 accepted H006 method definition。
- **P4 Previous input validation**：accepted weighted marginals；说明旧 source pool
  未 prompt-purified，是本轮升级的动机。
- **P5 Previous validated status**：accepted central result/closure 和主要未决假设的
  一页 recap；过渡到“先改造 source candidates，再讨论新 central”。

### P6--P10：主要方法升级

- **P6 Prompt single-J purification**：两个 slot 分别做 mass--ctau sPlot；用方法框图
  和 fit-quality 表，不展示内部协作编号。
- **P7 Cross-slot construction**：`Jpsi1(A) x Jpsi2(B)`、same-source rejection、signed
  pair weights；用流程图和 pair-count table。
- **P8 Deterministic all-pairs**：random sampling 与 all-pairs 的方法差异及消除的
  numerical variance；只陈述 H011 accepted 后的 verified counts。
- **P9 Kinematic category treatment**：global、pT split、rapidity split 的目的和
  fit-quality evidence；不在用户 freeze 前称任一方案 final nominal。
- **P10 Current scheme definition**：selection、14-cell binning、CR、normalization、
  estimator 的单页定义；结论 gate：central scheme 必须已由用户确认。

### P11--P15：二维 central maps 与主要投影

- **P11 Prompt--prompt Data map**：整页 central PP map；takeaway 是 decomposition 的
  fitted Data input，而不是独立 `f_DPS` 测量。
- **P12 Data-derived DPS map**：整页 CR-normalized mixed-DPS map；明确 CR equality
  由 normalization imposed，不是 purity proof。
- **P13 Data-driven SPS map**：整页 SPS subtraction map；保留一个 negative signed cell，
  不裁零、不解释为 probability。
- **P14 Separation projections**：`abs(delta_y)` shape+yields 两图并排；说明 projection
  是 consistency/decomposition view，不是独立 integrated measurement。
- **P15 Azimuthal projections**：`abs(delta_phi)` shape+yields 两图并排；同样保留
  correlated-error caveat。

### P16--P20：剩余投影与 uncertainty evidence

- **P16 Pair-kinematic projections**：`m(JJ)` shape 与 `abs(y(JJ))` shape 并排；两张
  codes 标为 important-support 的图片均进入主文。
- **P17 Category comparison**：从 accepted `comparison.csv` 制作原生表格，显示三种
  scheme、central values、signed shifts 与 fit status；不新作 plot。
- **P18 Control-region sensitivity**：从 accepted `primary_fractions.csv` 制作原生表格，
  显示三项 boundary variations 和 separate tested envelope；不称 purity test。
- **P19 Full-chain bootstrap**：用 summary table 展示 successes/attempts、mean、SD、
  quantiles 和失败分类；sample SD 按用户决定称为 `stat`。没有 approved distribution
  figure 时不伪造图形。
- **P20 Provisional systematic**：分别展示 category 与 CR envelopes，再给出暂定组合；
  当前按独立 groups quadrature 计算为 `+0.007382/-0.010591`，并列出仍缺失的来源。

### P21--P25：结论、thanks 与第一组 backup

- **P21 Method status**：validated improvements、provisional outputs、missing validation
  三栏对照；重申 data-driven internal central 不替代 CMS nominal。
- **P22 Takeaways and decisions**：三条主要进展、两项数值边界、下一步 physics gates；
  不使用内部 request/task 编号。
- **P23 Thanks**：复用批准的 closing geometry。
- **P24 Backup -- central weights**：DPS/SPS weight maps 并排，central-value-only caveat。
- **P25 Backup -- cell diagnostic**：SPS significance map；说明不是 global significance。

### P26--P30：其余 evidence-driven backup

- **P26 Backup -- yield projections**：`m(JJ)` 与 `abs(y(JJ))` yields 并排，保留
  correlation 和 closure caveat。
- **P27 Backup -- DPS-MC benchmark**：benchmark map 与 `abs(delta_y)` shape；明确
  generator-dependent、不是 event-mixing uncertainty 或 nominal gate。
- **P28 Backup -- historical validation**：accepted previous marginals 与 CR validation；
  只回答方法演进问题，不与新 central 数值混用。
- **P29 Backup -- previous uncertainty machinery**：accepted historical uncertainty
  summary 中仍有解释价值的页面；逐页标注 superseded numerical definitions。
- **P30 Backup -- bootstrap definition**：resampling unit、full-chain stages、success policy
  和 selection-bias risk 的技术表/流程；只用 accepted metadata。

## Figure coverage decision

- **主文全部展示：** H011 manifest 的 3 张 `must_show_major_progress` 和 6 张
  `important_support` PDFs。
- **Backup 展示：** 5 张 central diagnostic/yield PDFs、2 张 DPS-MC benchmark PDFs，
  以及能够回答方法演进问题的少量 accepted historical artifacts。
- **不展示：** stale nominal-comparison PDF；被新 central 数值取代且无独立教学价值的
  historical pages。
- **当前缺图不补画：** category comparison 与 bootstrap distribution；初稿使用已有
  machine-readable summary table。若用户认为 plot 必需，另行授权 codes 新作图。

## Gate 与执行顺序

1. 页面结构已获用户批准；当前沿用 25--30 分钟 JJ internal update 的规划假设，
   若报告时长或受众变化再等比例调整。
2. H012 provenance 修正与 consumer 复核已完成；H011 已 accepted。
3. 用户已确认 central、bootstrap `stat`、暂定 `syst` 和最终 nominal comparison
   口径，并已批准 category/CR 独立 group envelopes 的 quadrature combination。
4. 构建并归档当前 `main.tex`、`project_setup.tex` 和 PDF；冻结 archive 不覆盖。
5. 只复用 title/thanks 格式、主题和宏，其余正文与 backup 从零创建。
6. 以单页/小批次编译迭代；完成后运行 fastcheck、latexmk、warning audit、内部编号
   checker 和逐页 PDF visual QA。
