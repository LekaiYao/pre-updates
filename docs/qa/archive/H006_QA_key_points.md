> Lifecycle: historical QA/implementation evidence, archived on 2026-08-02.

# H006 slides QA 重点梳理

- 基准：当前 27 页 `build/main.pdf`
- 来源：`H006_current_slides_page_by_page_QA.md`
- 用途：合并多轮追问，区分“尚未完全理清”与“已经理清但必须保留”的问题
- 当前状态：只整理认识；逐页 QA 全部结束前，不据此自动创建 request 或修改 slides

# 一、尚未完全理清的 QA

## 1. ATLAS 的逐事件 PP 权重、背景扣除及其与 sPlot 的关系

### 已经明确的 ATLAS 流程

ATLAS 不是在一次拟合后只保留 PP 总数。maximum-likelihood fit 同时给出：

- component yields/fractions；
- prompt、nonprompt 等 components 在 discriminating variables 上的 PDFs；
- fitted PDF parameters。

因此原始事件的 \((L_{xy1},L_{xy2})\) 坐标仍然存在，可以逐事件计算

\[
q_{\rm PP}(e)=
\frac{f_{\rm PP}P_{\rm PP}(x_e)}
{f_{\rm PP}P_{\rm PP}(x_e)+(1-f_{\rm PP})P_{\rm NP}(x_e)}.
\]

ATLAS 将 “PP PDF / total PDF” 称为事件为 PP 的 likelihood，并作为 PP signal
weight。其完整顺序大致是：

1. 施加 acceptance、trigger、reconstruction 和 selection corrections；
2. 对 \(m(J/\psi_1)\times m(J/\psi_2)\) 做二维质量拟合，扣除 non-\(J/\psi\)
   background；
3. 对 \(L_{xy1}\times L_{xy2}\) 做 prompt/nonprompt fit；
4. 根据拟合 PDFs 为每个事件计算 posterior-like PP likelihood；
5. 用 MC 修正全局平均 \(f_{\rm PP}\) 对 differential distributions 造成的 bias；
6. 在目标变量的每个 bin 中，对 PP-weighted 二维质量分布重新拟合；
7. 另外拟合并扣除 pile-up background；
8. 最终得到 background-subtracted、bias-corrected PP differential distributions。

### 它不是标准 sPlot

ATLAS 论文没有把这一步称为 sPlot。posterior-like weight 与 sWeight 的区别是：

- posterior weight 通常在 0 到 1 之间，表示模型下事件在 discriminant space 中更像
  哪个 component；
- sWeight 使用 extended-likelihood 的 yield covariance 构造，可以为负；
- posterior weight 在 \(f_{\rm PP}\) 随目标变量变化，或目标变量与 \(L_{xy}\)
  在 component 内相关时会产生 differential bias；
- sPlot 也不是无条件无偏，它要求 control variable 与 discriminating variables
  在每个 component 内满足 factorisation/independence。

因此 sPlot 是一种可能方案，但不是唯一可行方案。

### ATLAS 如何处理 posterior-weight bias

ATLAS 明确承认：只在四个 rapidity categories 中使用平均 \(f_{\rm PP}\) 计算 PP
weight，会使 \(p_T\)、\(\Delta y\)、\(\Delta\phi\)、\(m(JJ)\) 等 differential
distributions 产生 bias。

其处理方式是：

- 生成 PP、P-NP、NP-NP 三类 MC；
- 改变输入 PP fraction；
- 比较 `input f_PP / reconstructed f_PP`；
- 对不同目标变量建立 differential bias-correction function；
- 分 central/forward rapidity区域应用修正；
- 做 MC closure；
- 变化 correction fit 及其 covariance，得到 differential \(f_{\rm PP}\)
  correction systematic。

### 尚未完全理清的部分

公开论文足以说明逻辑，但尚不足以完全重建所有实现细节，例如：

- posterior likelihood 的精确归一化和事件权重组合顺序；
- mass-fit signal weight 与 PP likelihood 是否以及如何相乘；
- pile-up subtraction 在最终 event weights 中的精确实现；
- bias-correction function 在每个 differential bin 的应用细节；
- 这些权重之间的完整 covariance；
- 若改用 CMS 的 simultaneous 4D fit，怎样构造严格等价的逐事件 PP weights。

所以现阶段可以理解 ATLAS 的方法原理，但尚不能仅凭论文完整重写其 event-weight
implementation。

## 2. 当前 CMS H006 为什么不是严格 ATLAS reproduction

当前 H006 的 Data PP map 在每个二维 cell 内使用 CMS `pdf_all`，对

\[
(m_1,m_2,c\tau_1,c\tau_2)
\]

做 simultaneous 4D fit，统计提取 \(N_{\rm PP}^i\)。

这可以得到每格 PP yield，但与 ATLAS 有重要差别：

- mixed pool 直接来自 2492 selected pair candidates；
- source candidates 在 mixing 前没有通过逐事件 PP likelihood 净化；
- 没有 ATLAS 等价的 differential \(f_{\rm PP}\) bias correction；
- 没有单独复现 ATLAS pile-up fit/subtraction；
- mass、lifetime 和 background models 使用 CMS 既有框架；
- Data normalization 使用 PP fitted yields，但 mixed shape 来自未 PP-purified pool。

因此当前工作实际是：

> 在 CMS 既有 4D fit 框架上测试 ATLAS 的核心 mixing、control-region normalization、
> subtraction 和 component-weight 思路。

它是 ATLAS-style cross-check，不是严格复现 ATLAS background-extraction chain。

### 尚未完全理清的核心问题

需要进一步判断：

- CMS 是否应建立逐事件 PP likelihood 或 sWeights 后再进行 mixing；
- 应使用“两个 PP-weighted \(J/\psi\)”还是“background-subtracted single-\(J/\psi\)
  pool”构造 DPS template；
- 现有 simultaneous 4D fit 能否自然产生适合 mixing 的 event-level PP weights；
- prompt/nonprompt/combinatorial weights 与 cross-event pair weight 应如何组合；
- 如何传播负权重、event reuse 和 fit covariance；
- pile-up、same-PV selection 与 DPS mixing 之间应如何处理。

在这些问题解决前，不能把 current mixed sample 称为已经验证的 prompt-prompt DPS
template。

## 3. 用 PP control region 归一化未净化 mixed template 的额外假设

当前归一化为

\[
\alpha=
\frac{\sum_{\rm CR}N_{\rm PP}}
{\sum_{\rm CR}N_{\rm mix}},
\qquad
N_{\rm DPS}^i=\alpha N_{\rm mix}^i.
\]

这只固定 mixed template 的整体 scale。它不能消除 mixed shape 中可能存在的
nonprompt/combinatorial bias。

当前方法实际依赖：

1. selected-candidate pool 经 correction 后近似 prompt-DPS single-\(J/\psi\)
   kinematics；
2. pool composition 不显著扭曲二维 mixed shape；
3. 两次散射中的两个 \(J/\psi\) 可近似独立抽样；
4. control region 中 PP yield 由 DPS 主导；
5. SPS leakage 足够小，或其不确定度已被 variations 覆盖。

已有 single-\(J/\psi\) marginal validation 只支持第一项的一部分；它不能证明
candidate composition 正确，也不能验证 pair-level DPS correlations。

所以“PP yield 用于归一化”与“mixed template 是 PP DPS shape”是两个独立问题。
前者不能证明后者。

## 4. 当前系统误差是否对齐 ATLAS

### 对齐的部分

ATLAS 的 DPS-model variation 包括：

- \(\Delta\phi\) CR boundary 改变 \(\pm\pi/9\)；
- \(|\Delta y|\) threshold 从 1.8 收紧到 2.4。

当前 H006 使用：

- \(7\pi/18,\ \pi/2,\ 11\pi/18\)；
- \(|\Delta y|\ge1.8\) 与 \(\ge2.4\)。

因此 CR boundary variation 的数值定义与 ATLAS 核心 DPS-model test 基本对齐。

### 没有对齐的部分

ATLAS 对 \(f_{\rm DPS}\) 列出：

| source | relative uncertainty |
|---|---:|
| Trigger | 0.7% |
| Muon reconstruction | 0.1% |
| Mass model | 0.01% |
| Mass bias | 0.02% |
| Prompt-prompt model | 0.1% |
| Differential \(f_{\rm PP}\) correction | 0.1% |
| Pile-up | 0.8% |
| DPS model | 5.6% |
| Total | 5.7% |

当前 H006 fraction envelope 没有完整传播：

- trigger、muon reconstruction；
- acceptance/efficiency corrections；
- mass-model parameters/background shapes；
- mass bias；
- prompt-prompt lifetime model；
- differential \(f_{\rm PP}\) bias correction；
- pile-up model/subtraction。

此外：

- ATLAS 使用更细 binning 检查 SPS peak/CR；当前 variation 是 global coarse10；
- mixing seed 只检查随机重采样稳定性，不是 mixing-model systematic；
- 单一 nominal SPS leakage correction 不是完整 leakage-model uncertainty；
- mixed pool 的背景处理与 ATLAS 不等价。

当前 absolute method envelope 约 0.0038，相对
\(f_{\rm DPS}=0.19247\) 约为 2.0%，明显小于 ATLAS 的 5.6% DPS-model 和 5.7%
total。这更可能说明当前 variation 集合较窄，而不能证明 CMS 方法更精确。

E4 中的 CMS pair cross-section systematic 和 ATLAS single-\(J/\psi\)/luminosity
uncertainties 属于截面输入，不能代替缺失的 \(f_{\rm DPS}\) method systematics。

## 5. P9 weights 为什么不展示误差

\[
w_{\rm DPS}^i=\frac{N_{\rm DPS}^i}{N_{\rm PP}^i},
\qquad
w_{\rm SPS}^i=1-w_{\rm DPS}^i.
\]

逐格误差不能按独立分子/分母传播，因为：

- \(N_{\rm DPS}\) 的 \(\alpha\) 来自 control-region \(N_{\rm PP}\)；
- \(N_{\rm SPS}=N_{\rm PP}-N_{\rm DPS}\)；
- 所有 cells 共享同一个 \(\alpha\)；
- mixed cells 复用 2492 source events；
- Data PP 与 mixed pool 来自同一批 source data。

因此需要的是完整的

\[
\mathrm{Cov}(w_i,w_j),
\]

而不是 14 个互相独立的误差条。H007 只删除了错误的 ROOT
`\(\sqrt{\text{content}}\)`，没有生成完整 weight covariance。

P16 toys 会重新计算 weights 并将其不确定度传播至最终 fraction，但这不等于 P9
已经有可逐格展示的完整误差。

当前尚需决定：

- 是否要求代码侧输出 weight covariance；
- 是否只把 P9 作为方法示意；
- 是否把精确中心值 map 移到 backup。

# 二、已经理清但非常重要的 QA

## 1. P4：2492 candidates 与 event mixing

### 2492 是什么

2492 是通过以下事件级 selection 的 reconstructed pair candidates：

```text
passHLT && matchTrg
&& 10 <= pT(Jpsi1,Jpsi2) <= 40 GeV
&& samePV
&& m(JJ) >= 7.5 GeV
```

它们不是 2492 个已经确定的 prompt-prompt events。prompt-prompt component 是随后在
二维 cells 中通过四维 mass-lifetime fit 统计提取的。

### mixing 改变什么

从两个不同 source events 各随机取一个 \(J/\psi\)，重新组成 pair：

- 单个 \(J/\psi\) 的 \(p_T,\eta,y,\phi,m\) 不修改；
- 重新计算 \(m(JJ)\)、\(|y(JJ)|\)、\(|\Delta y|\)、\(|\Delta\phi|\)；
- 重新计算 pair correction weight；
- mixed pair 仍要求 \(m(JJ)\ge7.5\) GeV。

这样保留 single-\(J/\psi\) kinematics，同时破坏原事件内 SPS correlations。

## 2. P5：single-\(J/\psi\) marginals 的含义和用途

Marginal distribution 是把另一个 \(J/\psi\) 和 pair correlations 积分掉，只看
单个 \(J/\psi\) 的一维 distribution。

P5 比较 Data 与 mixing 的：

- inclusive single-\(J/\psi\) \(p_T\)；
- inclusive single-\(J/\psi\) \(|y|\)。

两者均归一到单位面积。展示目的是检查 mixing 是否在破坏 pair correlation 的同时，
保持决定 fiducial selection 和 corrections 的 single-particle kinematics。

该检查是必要的 sanity check，但不是 `event mixing = true DPS` 的充分证明。

## 3. P7、P8：P7 normalized DPS 的误差

\[
N_{\rm DPS}^i=\alpha N_{\rm mix}^i.
\]

修正版 P7 的 cell-level analytic error 包含：

- control-region Data PP fit errors；
- mixed histogram pair-level \(\sum w^2\)；
- 所有 cells 共享 \(\alpha\) 带来的 normalization correlation。

但它不是最终 fraction 的完整统计误差：

- source-event reuse 的完整传播在 P16 joint toys 中处理；
- Data PP covariance 当前只有对角项；
- Data PP 与 mixed pool 的 shared-source cross-covariance 未包含。

所以 P7 图内误差用于理解局部 template/subtraction，不应替代 P16 的 estimator-level
uncertainty。

## 4. P16：pseudoexperiments 的定义和作用

P16 使用 50,000 个 estimator-level Gaussian toys，不生成新的完整 mass/ctau
events，也不在每个 toy 中重跑 RooFit。

每个 toy：

1. 根据 Data fit covariance 抽取 14 个 fluctuated \(N_{\rm PP}\)；
2. 根据 source-event bootstrap covariance 抽取 14 个 correlated
   \(N_{\rm mix}\)；
3. 重算 \(\alpha\)；
4. 重算 SPS/DPS yields 和 weights；
5. 重算 primary 与 reported \(f_{\rm SPS}\)。

50,000 次输出的标准差作为 statistical uncertainty。其作用是数值传播非线性且相关的
统计误差，不会增加真实数据量，也不检验物理模型系统误差。

## 5. P18：parametric closure 和 30 ensembles

### closure 如何做

对 \(f_{\rm SPS}^{\rm true}=0.2,0.5,0.8\)：

1. 使用 nominal SPS/DPS cell shapes 设置每格 PP yield；
2. 使用 nominal `pdf_all` 生成 mass/ctau pseudo-data；
3. 保留 nominal background yields；
4. 重跑 14-cell PP fits；
5. 重做 CR normalization、subtraction、weights；
6. 重跑 18 个 \(|\Delta y|\) total/SPS/DPS component fits；
7. 比较 fitted fraction 与 truth。

这是 full-chain parametric implementation closure。

### 30 ensembles 的意义

同一 truth 下 30 组使用不同 random seeds，产生不同 event counts、mass/ctau
observations 和 fit fluctuations。重复组数用于估计：

- bias；
- empirical spread；
- pull mean/width；
- coverage；
- failure probability。

增加更多 truth points 则用于扫描 linearity 和适用范围。重复数与 truth-point 数量
解决不同问题，不能互相替代。

30 组只够初步诊断：

- coverage uncertainty 约 0.08；
- pull-width uncertainty 约 0.13。

### closure 的能力边界

generator 和 fitter 使用同源 nominal shapes 与 mass-lifetime model，因此该 closure
较容易通过，尤其是 0.8 接近 nominal。它可以发现：

- implementation error；
- fit bias；
- uncertainty propagation failure；
- signed-weight/低 fraction 不稳定。

它不能验证：

- mixed template 是否是真实 prompt-prompt DPS；
- control region 是否确实 DPS dominated；
- nominal SPS/DPS shapes 是否正确；
- fit-model misspecification。

## 6. P19：低 fraction failure 与表格

### \(f_{\rm SPS}=0.2\) 的问题

只完成 9/30。低 SPS fraction 下，subtraction 更容易产生多个负 SPS cells；
某些 \(|\Delta y|\) bins 的 SPS weighted total yield 变为非正，导致 extended
component fit 无法定义或不能通过接受条件。

这说明当前 subtraction + signed-weight component-fit chain 在低-SPS regime 存在
适用边界，不说明物理上 \(f_{\rm SPS}=0.2\) 不可能。

0.2 行的 bias/pull/coverage 只来自成功的 9 组，存在 success-selection bias，不能
与完整 30 组等价比较。

### 表格各列

- `true`：注入的 \(f_{\rm SPS}\)；
- `Complete`：完整通过全部分析链的 ensembles 数；
- `Bias`：\(\langle f_{\rm fit}-f_{\rm true}\rangle\)；
- `Pull width`：\((f_{\rm fit}-f_{\rm true})/\sigma_{\rm fit}\) 分布的标准差；
- `1 sigma coverage`：\(f_{\rm fit}\pm\sigma_{\rm fit}\) 覆盖 truth 的比例。

## 7. P20：method variations、已有验证和缺失项

### 已经做的 variations

- CR \(\Delta\phi\) boundaries；
- CR \(|\Delta y|\) threshold；
- coarse10 binning；
- independent mixing seed；
- nominal SPS leakage correction；
- 每条链重跑四个一维 variables 的 component fits。

reported \(|\Delta y|\) fraction 的最大上下偏移形成当前 method envelope。

### 为什么 integrated shift 看起来小

- 总 \(f_{\rm DPS}\) 约 0.192；
- 相邻 CR choices 的 Data/mixed normalization ratio 接近；
- 大 relative shape changes 多位于低-population bins；
- integrated fraction 对局部 shape distortions 不敏感。

所以当前结果只能说明：

> 在已经测试的 variations 内，integrated fraction 稳定。

不能说明两项核心假设已经被完整验证。

### 两项核心假设

#### A. `event mixing = DPS`

已经做：

- single-particle marginals；
- mixing seed；
- binning；
- source-event statistical covariance。

仍缺：

- prompt-purified/background-subtracted pool；
- pool composition variations；
- independent DPS truth closure；
- era/pile-up/event-activity/kinematic splits；
- injected DPS shape distortions；
- correction uncertainties；
- shared-source cross-covariance。

#### B. `control region dominated by DPS`

已经做：

- \(\Delta\phi\) 和 \(|\Delta y|\) boundary variations；
- nominal leakage correction；
- CR shape-fraction comparison。

仍缺：

- multiple SPS leakage models及其 theory uncertainties；
- absolute CR purity estimate；
- continuous CR scan/plateau；
- mutually exclusive control regions；
- injected leakage closure；
- CR 中 PP/background-model variations。

## 8. P25：当前 systematic 是否完整

不能声称完整。

当前包含：

- 有限 CR/binning/mixing/leakage method variations；
- CMS pair cross-section systematic；
- ATLAS single-\(J/\psi\) bin systematic 和 luminosity。

尚未完整覆盖：

- PP mass-lifetime fit-model variations；
- acceptance、efficiency、trigger、selection uncertainties在新链中的传播；
- mixed-pool background composition；
- event-mixing model dependence；
-完整 SPS leakage uncertainty；
- Data cell non-diagonal fit covariance；
- Data/mixing shared-source covariance；
- pile-up；
- differential PP-weight bias；
- independent-truth closure；
- 高精度 coverage calibration。

data-driven 方法可能减少 SPS MC-template modeling uncertainty，但会引入 mixing、
control-region、subtraction 和 signed-weight assumptions。当前约 2% relative
\(f_{\rm DPS}\) method envelope 只是 tested-variation envelope，不能被解释为
complete/final systematic uncertainty。
