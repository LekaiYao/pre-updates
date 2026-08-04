> Lifecycle: historical QA/implementation evidence, archived on 2026-08-02.

# H006 current slides：逐页理解与问题记录

- 基准文件：`build/main.pdf`，27 页版本
- 记录日期：2026-07-31
- 状态：问答进行中
- 当前约束：本轮只记录问题、回答和待核查点；在逐页问答完全结束前，不据此建立
  新 request，也不修改 slides。

## 第三轮 QA：ATLAS 背景扣除与系统误差对齐

### 1A. 追加追问：一次拟合如何保留逐事件PP weight？是否只能使用sPlot？

“一次拟合后只剩PP总数”并不准确。maximum-likelihood fit除了component yields/fractions，还给出各component在discriminating variables上的PDF和fitted parameters。原始事件的 `(Lxy1,Lxy2)` 坐标仍然保留，因此可逐事件计算

```text
q_PP(e) = f_PP P_PP(x_e) / [f_PP P_PP(x_e)+(1-f_PP)P_NP(x_e)].
```

ATLAS原文明确说用“PP PDF除以total PDF”得到事件为PP的likelihood，并作为signal weight。fit相当于给出二维Lxy空间中的PP-likelihood函数，再对每个事件求值；事件信息没有丢失。

这属于posterior-like probability weighting，不是标准sPlot。posterior weight通常在0到1之间，表示模型下事件在Lxy空间更像哪个component，权重和可近似yield；但若目标变量z与Lxy在component内部相关，或 `f_PP` 随z改变，用全局平均 `f_PP` 的weight重建z分布会有bias。

sPlot则利用extended-likelihood yield covariance构造sWeights；在control variable与discriminating variables对每个component内部独立时，可无偏恢复control-variable distribution。sWeights可以为负，也不是事件真实属于component的概率。sPlot同样需要factorisation条件，并非对任意相关性自动无偏。因此它是可选方案，不是唯一可行方案。

ATLAS明确识别了posterior PP weight的differential bias：weight只按四个rapidity categories中的二维Lxy和平均 `f_PP` 定义，但真实 `f_PP` 会随 `pT`、`Delta y`、`Delta phi`、`m(JJ)` 等变化。ATLAS用PP、P-NP、NP-NP三类MC，在不同input fractions下比较 `input f_PP/reconstructed f_PP`，对各目标变量建立bias-correction function，分central/forward区域应用，做MC closure，并通过变化correction fit及其covariance评估differential `f_PP` correction systematic。

随后ATLAS还在目标变量每个bin内，对PP-weighted `m(Jpsi1)x m(Jpsi2)` distribution重新做二维mass fit以提取PP signal，并非把全局PP weights简单相加作为最终分布。

完整逻辑为：较粗rapidity categories中的Lxy fit -> 逐事件posterior-like PP likelihood -> MC differential-bias correction -> 目标变量逐bin PP-weighted mass fit -> PP differential yield。用户指出不能无限细分Lxy fit是正确的；ATLAS正是用连续event likelihood保留Lxy信息，再用MC校正平均fraction bias。

因此ATLAS方案技术上可行，但posterior weight本身不是严格无偏，MC differential correction及其systematic不可缺少。当前CMS H006没有复现逐事件PP likelihood和differential-bias correction，不能称为严格对齐ATLAS的background-subtracted source construction。


### 1. ATLAS 如何得到 background-subtracted data？是 sPlot 吗？为什么当前没有严格复现？

ATLAS描述的是 sequential extraction/event-weight procedure，论文没有把它称为标准sPlot/sWeight；不能仅因存在event probability weight就断言使用sPlot。

ATLAS顺序为：先施加acceptance、trigger、reconstruction和selection corrections；对 `m(Jpsi1) x m(Jpsi2)` 做unbinned 2D mass fit，以两个Crystal-Ball乘积描述signal、二维常数描述non-Jpsi background，提取真实di-Jpsi signal；再对 `Lxy1 x Lxy2` 做prompt/nonprompt fit，以resolution-convolved delta和exponential描述prompt/nonprompt，为事件构造PP probability/event weight；用PP weight得到目标变量中的PP distributions；另行拟合并扣除来自两个不同pp collisions的pile-up；最后用background-subtracted、bias-corrected data及其di-Jpsi sample重采样构造mixed template。

所以ATLAS的background subtraction至少覆盖non-Jpsi、nonprompt、pile-up以及differential PP bias correction。

当前CMS H006则在每个二维cell用现有 `pdf_all` 对 `(m1,m2,ctau1,ctau2)` 做simultaneous 4D fit，统计提取Data `N_PP`。这能净化Data yield，但没有先给每个source candidate建立与ATLAS等价的background-subtracted/PP event weight；mixed pool直接来自2492 selected candidates。当前也没有复现ATLAS单独的pile-up fit/subtraction、differential `f_PP` bias correction，以及相同的顺序mass/lifetime models。

没有严格复现的根本原因是本研究选择了“在CMS既有4D fit框架上测试ATLAS核心的cross-event mixing、CR normalization、SPS subtraction和weights”，而不是逐项复制ATLAS全部background-extraction chain。不同实验的selection、detector和fit基础也不能机械复制参数。

但这项差别具有物理后果：Data normalization使用PP fitted yields，而mixed shape来自未PP-purified selected pool，并不严格等价于ATLAS background-subtracted mixing。若要声称严格复现，至少需建立CMS等价的background-subtracted/prompt-weighted source pool、处理pile-up，并验证其对mixed shape和fraction的影响。当前只能称ATLAS-style cross-check。

### 2. 当前系统误差是否与ATLAS对齐？

结论：只在control-region/DPS-model variation上部分对齐，整体没有对齐ATLAS的 `f_DPS` systematic prescription。

ATLAS对data-driven `f_DPS`列出：trigger 0.7%、muon reconstruction 0.1%、mass model 0.01%、mass bias 0.02%、prompt-prompt model 0.1%、differential `f_PP` correction 0.1%、pile-up 0.8%、DPS model 5.6%，总计5.7%。

ATLAS的DPS-model测试把 `Delta phi` CR边界上下移动一个bin，即 `±pi/9`，并把 `|Delta y|` threshold从1.8收紧到2.4。当前CMS使用 `7pi/18, pi/2, 11pi/18`，正是 `pi/2±pi/9`，并测试 `|Delta y|>=2.4`；这一核心CR variation在定义上高度对应。CMS还增加了mixing seed、coarse10和nominal SPS leakage tests。

但差异包括：ATLAS binning cross-check在SPS peak/CR附近使用更细bin，当前是global coarse10；当前fraction envelope没有传播trigger、muon reconstruction、mass-model/background-shape、mass bias、prompt-prompt lifetime model、differential PP bias和pile-up variations；mixed pool的background treatment也不等价；mixing seed只检验随机重采样稳定性，不能替代DPS-model uncertainty；单一nominal leakage correction也不是完整model uncertainty。

当前method uncertainty的绝对值约0.0038，相对 `f_DPS=0.19247` 约2.0%，明显小于ATLAS的5.6% DPS-model和5.7% total。不能据此声称CMS更精确，更合理的解释是当前variation集合更窄且若干ATLAS来源未传播。

E4加入的CMS pair cross-section systematic和ATLAS single-Jpsi/luminosity uncertainties属于 `sigma_DPS/sigma_eff` 的截面输入误差，不能替代缺失的data-driven `f_DPS` method systematics。

准确表述：CR boundary variation与ATLAS核心DPS-model测试基本对齐；完整background treatment、binning test和 `f_DPS` systematic source list尚未对齐。当前约2%的relative envelope只是现有测试集合的结果，不是ATLAS-aligned total systematic。


## 第二轮 QA：核心假设、weights、toys 与 validation

### 1. Event mixing template 与 PP control region

`N_PP` 是 Data 中经 mass-lifetime fit 提取的 prompt-prompt yield；mixed template 则从 selected candidate pool 重组得到。`alpha=sum_CR(N_PP)/sum_CR(N_mix)` 只确定 mixed shape 的整体 scale，不能把受 nonprompt/background 污染的错误 shape 自动变成 prompt-prompt DPS shape。

因此当前方法确实依赖额外假设：selected-candidate pool 经 correction 后可近似两个独立 prompt J/psi 的 factorized kinematics；pool 中 nonprompt/combinatorial composition 不显著扭曲 `(|Delta y|,|Delta phi|)` shape；control region 的 PP component 由 DPS 主导；真 DPS 没有重要的残余 pair correlation。

ATLAS 原方法使用 background-subtracted data 重采样 J/psi，并明确假设两只 J/psi 独立产生、control region 由 DPS 主导。当前 CMS mixed pool 不是逐事例 PP-purified/background-subtracted pool，这是需要单独验证的差别。single-J/psi marginals、mixing seed、CR boundary 和 nominal leakage variations 只能提供部分支持；PP control-region 归一化不会消除 mixed-shape 假设。

当前准确表述：mixed sample 是在“独立产生且候选组成不引入显著偏差”假设下构造的 DPS shape estimator，而不是已经被证明为 prompt-prompt DPS 的样本。

### 2. P9：为什么 weights 没有误差？

`w_DPS=N_DPS/N_PP`、`w_SPS=1-w_DPS`。它们不能使用独立分子/分母误差公式，因为 `alpha` 来自 CR 的 `N_PP`，`N_SPS=N_PP-N_DPS`，所有 cells 共享 `alpha`，mixed cells 复用2492 source events，Data PP与mixed pool又共享source data。逐格 uncertainty 实际是带强相关性的14-cell covariance问题。

H007修正版删除了错误的ROOT `sqrt(content)`，但没有输出完整 `Cov(w_i,w_j)`。P16 toys在每个toy中重算weights并传播到最终fraction；这不等于已经得到可逐格标注的独立误差。

用户的展示质疑成立：若P9被理解为定量测量，只画中心值会造成过度确定的印象；即使给每格marginal error而不显示correlation也不完整。当前map只能解释为构造component-weighted samples的nominal中心权重，不是逐事件SPS/DPS概率或带完整误差的独立测量。整轮QA结束后可选择输出完整weight covariance、改成方法示意，或把中心值map移到backup。

### 3. P16：pseudoexperiments/toys 在做什么？

一个toy模拟相同真实条件下重复实验时输入量的一次统计波动。P16不是重新生成完整mass/ctau events，也不重新做RooFit，而是estimator-level Gaussian propagation。

输入包括：14个Data `N_PP`及其当前仅对角的fit covariance；14个`N_mix`及按2492 source events的Poisson-bootstrap响应构造的相关covariance。每个toy抽取一组14维fluctuated `N_PP`和一组相关的fluctuated `N_mix`，然后依次重算 `alpha`、`N_DPS/N_SPS`、weights、2D primary `f_SPS`和`|Delta y|` reported `f_SPS`。reported estimator使用nominal component fits得到的response factors，并未在每个toy重跑18个component fits。

重复50,000次后，输出分布标准差定义statistical uncertainty，联合分布给出estimator correlation，data-only/mix-only toys区分来源。50,000不会增加真实Data统计量，只让非线性相关误差传播的数值估计稳定。它不能验证mixing是否是真DPS、CR是否DPS dominated、fit model是否正确或系统误差是否完整。

### 4. P18：30组、注入点与closure的内生性

同一 `f_SPS` 下30组使用不同random seeds，所以各组的cell event counts、`(m1,m2,ctau1,ctau2)`、cell内运动学和fit统计涨落不同；它们共享truth fraction、nominal shapes、生成PDF和背景模型。

增加同一注入点的ensemble数，改善固定truth下bias、spread、pull、coverage和failure probability的估计；增加更多不同 `f_SPS` 点，改善response线性、适用范围和failure boundary的扫描。两者不能替代。当前30组下coverage不确定度约0.08、pull-width不确定度约0.13，只适合发现严重failure，不是精确校准。

用户对closure内生性的理解基本正确。pseudo-data使用nominal data-driven SPS shape、nominal mixed-DPS shape、nominal mass-lifetime model和background yields；恢复时又使用同一分析结构。因此它是internal parametric closure：假定nominal shapes/model正确，改变总比例并加入统计涨落，检查完整实现能否无明显bias地回收输入。

它仍重做14-cell PP fits、subtraction、signed weights、18个component fits和uncertainty evaluation，所以能发现实现和低fraction不稳定性，0.2 failure说明输出并非无条件等于输入。但generator与fitter同源且0.8接近nominal，确实更容易通过；它不能验证 `event mixing=true prompt-prompt DPS` 或 `control region=DPS dominated`。

更强closure应使用不同源truth：独立DPS MC、prompt-purified替代mixing、注入DPS correlations/SPS leakage、替代mass-lifetime models，以及不同era/kinematic/pool definitions。当前应称为full-chain parametric implementation closure，不能称为两项核心物理假设已闭合。

### 5. P20：两项核心假设的现有与缺失 validation/systematics

#### A. `event mixing = DPS`

已做：single-J/psi `pT`/`|y|` marginals；independent mixing seed；source-event bootstrap covariance（统计处理，不是model validation）；nominal/coarse binning稳定性。

尚缺或未证明：prompt-purified/background-subtracted pool mixing；selected-pool nonprompt/combinatorial composition影响；真DPS残余correlation、event activity和factorization；era/pileup/vertex/kinematic-matched pool variations；independent DPS MC truth closure；注入DPS shape distortion后的fraction bias；correction/trigger/efficiency uncertainties；Data PP与mixed pool共享source的cross-covariance。mixing seed只检验随机采样稳定性，不能替代mixing-model systematic。

#### B. `control region dominated by DPS`

已做：`Delta phi`边界 `7pi/18, pi/2, 11pi/18`；`|Delta y|>=1.8/2.4`；nominal SPS leakage correction；CR内部Data/mixing shape fraction比较；每种CR定义重跑component fits。最大integrated shift约0.0039，只说明已测试的相邻边界和当前leakage model下fraction稳定。

尚缺或未证明：SPS leakage绝对大小及model/scale/PDF/shape uncertainty；多个独立SPS models；CR purity的absolute-yield estimate而非单位面积shape；互斥CR或二维sideband closure；连续CR scan与plateau test；注入不同leakage后的bias；alternative CR/二维likelihood；CR中PP fit/background-model variations。

当前 `+0.003750/-0.003867` 是有限variation集合的method envelope，不是已证明完整覆盖mixing model和CR purity的最终systematic。后续slides若修改，至少应区分implementation/statistical validation、已完成variations、两项核心物理假设、尚缺关键validation，以及tested-variation envelope的范围。是否新增产物、建立request和修改slides，继续等逐页QA结束后统一决定。


## 总体术语

- **selected candidate**：通过事件级 selection 的重建候选，不等于已经知道是
  prompt-prompt。
- **PP yield**：使用两个 J/psi 的质量和 pseudo-proper decay length 做四维
  mass-lifetime fit 后，统计提取的 prompt-prompt yield。
- **event mixing**：从两个不同真实事件中各随机取一个重建 J/psi，重新组成一个
  人工 J/psi pair。
- **primary estimator**：14-cell 二维分解积分得到的 `f_SPS`。
- **reported estimator**：用二维 component weights 构造一维 `|Delta y|`
  component samples、逐 bin 重做 mass-lifetime fit 后得到的 `f_SPS`。

---

## P4：Event mixing

### Q1：2492 个 selected data pair candidates 是什么？经过所有筛选、但未拟合过的事例吗？如何保证是 prompt+prompt？

基本理解正确：2492 是通过当前统一事件级 selection 的候选事例，还没有在
event-mixing 这一步逐事例判定为 prompt-prompt。

代码中的 selection 为：

```text
passHLT && matchTrg
&& 10 <= pT(Jpsi1,Jpsi2) <= 40 GeV
&& samePV
&& m(JJ) >= 7.5 GeV
```

pool 由 119 个 2016 Data 文件构造。每个入选事件保存两个 reconstructed J/psi
的四动量信息。这里的 `samePV`、触发和运动学选择只能提高候选质量，不能保证两个
J/psi 都是 prompt，也不能完全排除 nonprompt 或 combinatorial background。

prompt-prompt 不是逐事例标签，而是在后续每个二维 cell 中，通过

```text
(m1, m2, ctau1, ctau2)
```

四维 extended mass-lifetime fit 统计提取 `N_PP`。模型同时包含 PP、P-NP、
NP-NP、signal-combinatorial 和 combinatorial-combinatorial components。

因此当前 slides 中 “2492 selected data pair candidates” 是准确说法；
不能写成 “2492 prompt-prompt events”。

需要注意的物理问题是：当前 mixed pool 本身来自 selected candidates，而不是
逐事例 PP-purified J/psi pool。现有实现依赖后续 PP fits 和 control-region
normalization 处理目标 PP yield，但“mixed shape 对候选组成是否足够稳健”应被视为
方法假设，而不是由 selection 自动保证。

### Q2：这个 combination 在做什么？有修改动力学变量吗？

它不是在原事件内重新排列两个 J/psi，而是：

1. 随机选择两个不同 source events A、B；
2. 从 A 的两个 J/psi 中随机取一个；
3. 从 B 的两个 J/psi 中随机取一个；
4. 将两者的 reconstructed four-vectors 相加，形成新的 mixed pair；
5. 对新 pair 重新计算：
   - `m(JJ)`；
   - `|y(JJ)|`；
   - `|Delta y|`；
   - `|Delta phi|`；
   - pair acceptance/efficiency correction weight。

单个 J/psi 的 `pT`、`eta`、`y`、`phi` 和 mass 没有被随机修改；但所有 pair-level
变量都会因为配对对象改变而重新计算。新 pair 还需满足 `m(JJ) >= 7.5 GeV`。

这样做的目的，是保留 single-J/psi kinematics，同时消除原来同一事件中两个
J/psi 的 SPS correlation。由两个独立硬散射产生的 DPS，在这一近似下应更接近
这种 cross-event factorized shape。

---

## P5：Single-J/psi marginal validation

### Q1：这里的 Mixing 指什么？

指 P4 的 cross-event recombination：从不同 selected source events 各取一个
J/psi 组成 mixed pair。当前样本生成 5,000,000 个 mixed pairs，但它们复用同一组
2492 source events，因此不能当作 500 万个统计独立事例。

### Q2：single Jpsi marginals 是什么意思？

“Marginal distribution” 是把 pair 中另一个 J/psi 以及所有 pair correlation
积分掉后，只看一个 J/psi 的单变量分布。

本页展示：

- inclusive single-J/psi `pT` shape；
- inclusive single-J/psi `|y|` shape。

每个 selected pair 向 inclusive distribution 贡献两个 J/psi。Data 和 mixing
都归一到单位面积，所以只比较 shape。

### Q3：CDF distances 是什么意思？

对归一化的一维分布构造 cumulative distribution function：

```text
F(x) = P(X <= x)
```

然后计算 Data 与 mixed sample 两条 CDF 的最大绝对距离：

```text
D = max_x |F_Data(x) - F_mix(x)|.
```

当前结果：

```text
D(pT)  = 0.017
D(|y|) = 0.0046
```

它表示两套累计 shape 最大相差约 1.7% 和 0.46%。这里把它作为 shape-distance
diagnostic，不应直接解读成带有标准显著性的 KS p-value。

### Q4：为什么展示这两个图？

因为 event mixing 的核心假设是：

- 应破坏原事件内的 pair correlation；
- 不应人为扭曲组成 pair 的 single-J/psi kinematics。

`pT` 和 `|y|` 又直接控制 fiducial selection、acceptance 和 efficiency correction，
所以它们是最基本的 closure/sanity check。如果这两者明显不一致，mixed DPS shape
很可能是由抽样或权重实现造成的，而不是真实的独立散射近似。

这两张图只验证 marginal preservation，不足以证明 mixed sample 就是正确的 DPS
pair-correlation model。

---

## P7、P8：DPS normalization 与 SPS subtraction

### Q1：图中的误差来源是什么？

当前修正版 P7/P8 图使用 `cells.csv` 中的逐格误差：

#### P7：normalized DPS

```text
N_DPS^i = alpha * N_mix^i
alpha = sum_CR(N_PP) / sum_CR(N_mix)
```

`dps_error` 的 cell-level analytic propagation 包含：

- control-region Data PP fit errors；
- mixed histogram 的 pair-level `sum(w^2)`；
- 因同一个 `alpha` 归一化所有 cells 而产生的 control-region normalization
  correlation。

#### P8：subtracted SPS

```text
N_SPS^i = N_PP^i - N_DPS^i
```

`sps_error` 传播：

- 当前 cell 的 Data PP fit error；
- control-region Data 对 `alpha` 的贡献；
- mixed template pair-level error及归一化相关项。

但必须区分：

- P7/P8 图内误差是为了展示 cell-level subtraction 的局部误差；
- 最终 `f_SPS` 的统计误差不用这些格子误差简单独立相加，而是由 P16 的 50,000
  joint toys传播。

当前 joint propagation 使用 source-event covariance，而不是把 5M mixed pairs
看作独立；不过 metadata 也明确记录了两个限制：

- Data PP covariance 当前只有逐格对角项，没有非对角 fit covariance；
- PP Data 与 mixed pool 来自同一批 source data，但二者之间的 cross-covariance
  尚未包含。

因此 P7/P8 误差比旧图正确，但不能把它们称为已包含所有相关性的最终误差模型。

### Q2：为了说明 control region，是否应展示理论 SPS 与实际测量总截面在 `Delta y` 上的一维对比？

这个建议有一定说明力，但作用有限，而且当前材料不能直接完成这个论证。

可支持的逻辑是：

- control region 选在大 `|Delta y|`、小 `|Delta phi|`；
- 如果 SPS prediction 在该区域相对较小，而 Data 仍有明显 yield，会支持
  “DPS-enriched”的定性说法。

但当前已有 theory/Data 图比较的是：

- theory SPS 与 **data-driven SPS component**；
- 单位面积 normalized differential shape；
- 不是理论 SPS absolute cross section 与 measured total PP cross section；
- theory fiducial、单位和 envelope 定义仍有待确认。

因此现有 theory comparison 不能定量证明 control region 的 SPS contamination
很小。即使展示，也只能作为定性 shape intuition，并需同时说明：

- 不能用单位面积 shape 比较推导 SPS purity；
- total Data 包含 SPS、DPS 和拟合背景处理；
- control region 的关键假设最终应由 SPS leakage estimate/variation 或绝对归一化
  prediction 验证。

是否需要新增这类图，留到整轮问答结束后统一决定。

---

## P9：SPS/DPS component weights

### Q1：图中的权重为什么没有误差？

当前两张图明确只画 central values：

```text
w_SPS^i = N_SPS^i / N_PP^i
w_DPS^i = N_DPS^i / N_PP^i
w_SPS^i + w_DPS^i = 1
```

旧图曾错误显示 ROOT 默认的 `sqrt(bin content)`，它不是 weight uncertainty，
所以修正版删除了 `±`。

真正的 weight uncertainty 不能只对分子分母做无相关误差传播，因为：

- `N_SPS = N_PP - N_DPS`，分子与分母共享 `N_PP`；
- 所有 cells 共享 control-region normalization `alpha`；
- mixed cells 通过复用2492 source events相互相关；
- Data PP 与 mixed sample 还共享 source data。

当前分析没有输出逐格 weight 的完整 covariance，所以 P9 只展示中心值。最终 fraction
不把这些 weights 当作无误差常数做简单公式传播，而是在 P16 joint toys 中重新计算
normalization、subtraction、weights 和 estimators。

---

## P12：reported `|Delta y|` fraction

### Q1：为什么不展示其他一维图？

代码实际对四个变量都执行了 component-weighted mass-lifetime fits：

- `|Delta y|`；
- `|Delta phi|`；
- `m(JJ)`；
- `|y(JJ)|`。

nominal component fractions 分别约为：

```text
|Delta y|   0.807527
|Delta phi| 0.806958
m(JJ)       0.807969
|y(JJ)|     0.807464
```

当前只展示 `|Delta y|`，因为这是 ATLAS-style reported estimator；其余三个来自
同一个二维 decomposition，不是四次独立测量。它们主要是 consistency views。

不展示其他图的代价是：听众看不到四个投影的拟合质量、低统计 bins 和 component
closure。是否应放入正文或 backup，应在完成整轮问答后决定。

### Q2：这里的系统误差如何计算？是否考虑不同一维投影？

P12 本身展示的是 nominal fraction，不在这一页计算系统误差。E3 对每一种 method
variation 都重新执行完整链：

1. 改变 control region、binning、mixing seed 或 SPS leakage treatment；
2. 重新构造二维 DPS/SPS templates 和 weights；
3. 对四个目标变量的每个 bin 重新做 total/SPS/DPS mass-lifetime fits；
4. 重新计算各变量的 component fraction；
5. 对 normalized component shape，逐 bin 取所有 variations 中最大绝对偏移作为
   envelope。

四个投影都被处理，并各自有 variation shifts。但最终 reported `f_SPS` 的 systematic
使用 `|Delta y|` estimator 在 variations 下的最大上下偏移：

```text
-0.003867 : lower Delta-phi CR boundary
+0.003750 : SPS leakage correction
```

不同一维投影之间的中心值 spread 没有额外作为独立 systematic。这是因为四者共享
同一二维 decomposition，且相互高度相关；但“高度相关”并不自动证明其 spread
完全不应计入。当前做法需要被理解为现有 method-systematic prescription，而不是
由四个投影提供四个独立 systematic estimates。

---

## P16：joint statistical propagation

### Q1：具体如何计算统计误差？

执行 50,000 个 multivariate Gaussian pseudoexperiments。每个 toy 同时波动两个
原始信息源：

1. **14 个 Data PP fitted yields**
   - nominal covariance 为 `pp_error^2` 的对角矩阵；
   - 当前没有逐 cell 之间的非对角 fit covariance。
2. **mixed-DPS source-event covariance**
   - 以2492个原始 source events 为独立 Poisson-bootstrap units；
   - 根据每个 source event 对各二维 cell 的加权贡献，以及 source-event pairs
     的共同贡献，构造14x14 covariance；
   - 不把500万个重复 mixed pairs当成独立统计量。

每个 toy 中重新计算：

```text
alpha
-> N_DPS
-> N_SPS
-> cell weights
-> 2D primary estimator
-> |Delta y| reported estimator
```

50,000 toys 的 estimator standard deviation 定义为统计误差：

```text
primary  sigma_stat = 0.020619
reported sigma_stat = 0.018829
```

结果还给出两者相关系数 `rho = 0.992661`。

分解来看：

```text
reported data-only sigma ~= 0.01844
reported mix-only  sigma ~= 0.00379
```

所以统计误差主要来自 Data PP fitted yields，而不是5M mixed-pair sample size。

现有统计模型的已知限制：

- Data fit covariance 仅对角；
- Data PP 与 mixed pool 的 shared-source cross-covariance 未包含；
- E1 是 estimator-level Gaussian propagation，不替代 P18 的完整 RooFit closure。

---

## P17：Joint propagation results

### Q1：这一页是否是 closure test？如何做？系统误差如何估计？

按当前27页 PDF，P17 不是完整 closure test，而是 P16 joint statistical toys 的结果页。
它回答的是：“在 nominal estimator 周围传播当前统计模型，得到多大的 statistical
uncertainty，以及 primary/reported 两个 estimator 有多相关？”

其中 `toy bias = -0.001250` 是这些 Gaussian propagation toys 的 mean minus nominal，
不能单独当作完整 reconstruction closure。完整 closure 从 P18 开始。

P17 不估计 systematics。systematics 在 P20–P21 的 method variations 中处理。

---

## P18：Parametric closure method

### Q1：closure test 怎么做？系统误差如何估计？

对每个注入真值 `f_SPS = 0.2, 0.5, 0.8`：

1. 使用 nominal 14-cell SPS/DPS shapes，按注入 fraction 设定每格 PP yield：

   ```text
   N_PP^i = N_PP,total *
            [f_true * S_i/sum(S) + (1-f_true) * D_i/sum(D)]
   ```

2. 在每个 cell 中使用主分析同一 `pdf_all` 四维模型，生成
   `(m1,m2,ctau1,ctau2)` extended parametric pseudo-data；
3. nonprompt 和 combinatorial background yields 使用 nominal cell fits；
4. `Delta y`、`Delta phi` 在 cell 内均匀生成，用于把 pseudo-data 放回对应 cell；
5. 从头重复：
   - 14-cell PP fits；
   - control-region normalization；
   - SPS subtraction；
   - component-tree construction；
   - 18 个 `|Delta y|` total/SPS/DPS fits；
   - fraction 和单-toy uncertainty 计算；
6. 比较 fitted fraction 与 injected truth。

这个 closure 检查 bias、pull width 和 coverage，是验证 statistical estimator 和
fit chain。它本身不产生 P20 的 method systematic。系统误差来自对真实分析选择做
variations 后，观察结果相对 nominal 的偏移。

需要注意的非闭合独立性问题：pseudo-data 使用 nominal fitted model 和 nominal
SPS/DPS shapes生成，因此主要是 implementation/fit closure，不是对未知真实 shape
或 model misspecification 的完全验证。

### Q2：为什么需要30组？

每个 ensemble 都要重复很多 RooFit fits，计算代价高。30组是一个初始 diagnostic：

- 可以估计平均 bias；
- 可以粗略检查 pull width 是否约为1；
- 可以粗略检查68% coverage。

但30组不是高精度 calibration。仅由二项统计估算，若真实 coverage 约0.68，
30 toys 的 coverage 标准误差约为：

```text
sqrt(0.68*0.32/30) ~= 0.085
```

即约8.5个百分点；pull width 的误差也仍较大。因此30组足以发现明显失败，不能支持
对小偏差或轻微 under/over-coverage 的精确结论。

---

## P19：Closure results

### Q1：`f_SPS=0.2` 遇到了什么问题？如何解释？

只完成9/30。失败发生在完整 component-fit chain：

- 在低 SPS fraction 下，control-region normalization 后逐格 subtraction 更容易得到
  较大的负 SPS component；
- SPS-weighted samples 含显著 signed/negative weights；
- 某些目标 bins 的 weighted PP yield 非正或 RooFit component fit 无法满足接受条件；
- 因而不能完成全部18个 `|Delta y|` component fits和后续 uncertainty evaluation。

这说明当前 estimator/implementation 在低-SPS、高-DPS regime 存在适用边界。
它不是证明 `f_SPS=0.2` 的真实物理情形不可能，而是说明当前逐格 subtraction +
weighted RooFit 链在该 regime 不稳定。

另外，表中0.2行的 bias、pull和coverage只来自成功的9组，存在 success-selection
bias，不能与0.5/0.8的30组结果等价比较。

### Q2：表格每一列是什么意思？

- `f_SPS true`：生成 pseudo-data 时注入的真值。
- `Complete`：完整通过全部 fit、component 和 uncertainty 链的 ensembles 数量。
- `Bias`：

  ```text
  mean(f_fit - f_true)
  ```

- `Pull width`：每个成功 toy 定义

  ```text
  pull = (f_fit - f_true) / sigma_fit
  ```

  再取 pull distribution 的标准差。理想值约为1：
  - `<1` 通常表示 fitted uncertainties 相对 ensemble spread 偏大；
  - `>1` 通常表示 fitted uncertainties偏小或存在额外波动。
- `1 sigma coverage`：真值落在 `f_fit ± sigma_fit` 内的成功 toys 比例。理想高斯值
  约为68.3%。

在30-toy精度下，0.5和0.8的 bias 很小；pull/coverage 未出现明确显著 failure，
但精度不足以声称完成高精度 coverage calibration。

---

## P20：Method variations

### Q1：这一页的 closure/systematic 是怎么做的？

P20 不是 pseudo-data closure，而是 real-data method variations。nominal 完整链与
以下替代链比较：

- control-region `Delta phi` 边界：`7pi/18`、`11pi/18`；
- control-region `|Delta y| >= 2.4`；
- 10-cell coarse binning；
- 独立 mixing seed/sample；
- SPS leakage correction。

每条链都重新构造 templates、weights，并对四个一维变量执行全部 component fits。
所有链共546/546 component fits以及38/38 varied 2D PP fits通过。

对 reported `|Delta y| f_SPS`，每个 variation 的 signed shift 与 nominal 比较；
上下最大偏移作为当前 fraction method systematic：

```text
f_SPS syst = +0.003750 / -0.003867
```

对一维 normalized component shapes，则在每个 bin 对所有 variations 取最大绝对
偏移形成 envelope。

### Q2：control region 是最大系统误差来源之一，为什么这里看起来很小？

当前确实是 control-region variation 给出最大的负向 fraction shift，但绝对值只有
约0.00387。出现“小 integrated shift”的原因包括：

1. control region 只决定 DPS normalization，而总体 `f_DPS` 约0.192；
2. 测试的相邻 CR choices 得到相近的 Data/mixed normalization ratio；
3. 大的逐 bin relative shape changes主要出现在component占比较小的 bins，积分后
   会抵消或被低权重抑制；
4. `f_SPS` 是总积分比率，对局部 shape distortion 不敏感。

但这不能自动证明 control-region systematic 已完整且很小。当前 variation 集只测试
了三种附近边界和一个 leakage correction，尚不能排除：

- control region 中 SPS contamination 的理论/model uncertainty被低估；
- mixed DPS factorization/kinematic dependence；
- PP fit model与CR选择的相关变化；
- selection、efficiency/acceptance weights及其systematics；
- Data PP 与mixed source共享导致的相关性；
- 更广泛CR定义或二维shape mismatch。

因此 P20 的正确表述应是“在当前测试的 variations 内，integrated fraction 稳定”，
而不是“control-region systematic 已被完整证明很小”。

---

## P22：Phase-space matching

### Q1：这一页在做什么？

计算 `sigma_eff` 需要：

```text
sigma_eff = (1/2) * sigma(single J/psi)^2 / sigma_DPS(pair)
```

分子使用 ATLAS 13 TeV prompt single-J/psi cross section，分母使用 CMS
prompt-prompt J/psi-pair 的 DPS 部分。如果两者的 single-J/psi fiducial definition
不同，就必须做模型外推，结果会引入额外不确定度。

P22 核对两边每个 J/psi 都采用：

- prompt；
- `10 < pT < 40 GeV`；
- `|y| < 2.0`；
- nominal unpolarized acceptance。

所以不需要对 single-J/psi kinematics 做模型外推。CMS pair 特有的
`m(JJ)>7.5 GeV` 不适用于 inclusive single-J/psi cross section。

这一页还说明使用 visible quantities：

```text
X = B * sigma(single)
Y = B^2 * sigma_DPS(pair)
```

在 `X^2/Y` 中 dimuon branching fraction严格相消。

---

## P24：From fraction to `sigma_eff`

### Q1：什么叫 include ATLAS luminosity uncertainty？是否包含 CMS luminosity uncertainty？

ATLAS给出的 single-J/psi differential-bin systematic合并值为0.09 nb，但另外有
1.13% ATLAS integrated-luminosity uncertainty。代码将其加入：

```text
single_lumi = 10.63 nb * 1.13% = 0.1201 nb
single_total_syst = sqrt(0.09^2 + 0.1201^2) = 0.1501 nb
```

因为 `sigma_eff` 对 single cross section 是平方依赖，该项的相对影响约为两倍。

CMS luminosity uncertainty没有作为一个单独的新输入再次添加；它应已包含在
CMS pair total cross-section 的总 systematic：

```text
sigma_pair = 37.2 ± 0.6 (stat) ± 2.5 (syst) pb.
```

代码从这2.5 pb中只移除了0.78%的 branching-fraction相关项，因为BR在visible
single/pair比值中相消；其余CMS pair systematic（原则上包括CMS luminosity）保留在
`pair_nonbr_syst = 2.483 pb` 中。

这一结论依赖“2.5 pb确实已经包含CMS luminosity”这一主线输入定义；当前E4代码没有
把CMS lumi从2.5 pb中单独拆出验证。

---

## P25：Final cross sections

### Q1：为什么最后结果变成统计误差主导？

对 `f_DPS`：

```text
f_DPS = 0.19247
stat  = 0.01883  -> 约9.8%相对误差
method syst ~= 0.0038 -> 约2.0%
```

统计误差大，是因为真正的独立Data信息只有2492 selected candidates，PP yields还需
逐cell mass-lifetime fits；500万 mixed pairs不会创造500万独立Data事件。

对 `sigma_DPS`，CMS pair cross-section systematic仍贡献约6.7%相对误差，但与
`f_DPS` method systematic合并后仍小于约9.9%的统计项。

对 `sigma_eff`，系统项还包含：

- CMS pair non-BR systematic；
- ATLAS single-J/psi bin systematic；
- ATLAS luminosity；
- 当前 `f_DPS` method envelope。

组合后约：

```text
stat ~ 0.220 / 2.221 = 9.9%
syst ~ 0.167 / 2.221 = 7.5%
```

所以只是“统计略大于当前合并系统误差”，不是系统误差可以忽略。

### Q2：系统误差是否得到了完整、正确评估？

基于当前代码和metadata，不能声称已经完成“完整的系统误差评估”。

当前已经包含：

- 三类 control-region boundary changes；
- coarse binning；
- independent mixing seed；
-一个 SPS leakage correction；
- 四个一维 component shapes/fractions 在这些 variations 下的重算；
- CMS pair total cross-section systematic（移除相关BR项后）；
- ATLAS single-J/psi bin systematic和luminosity。

当前没有看到完整覆盖或尚需进一步论证的项目包括：

- PP mass-lifetime fit model/parameter variations；
- acceptance和efficiency correction uncertainties在data-driven chain中的传播；
- trigger、vertex、selection variations；
- mixed-pool candidate composition及nonprompt/background contamination；
- event-mixing factorization及source-event reuse的model uncertainty；
-更完整的 SPS leakage prediction uncertainty；
- Data PP fit cells之间的non-diagonal covariance；
- Data PP与mixed pool共享source data的cross-covariance；
- ATLAS differential-bin systematic covariance未知；
- closure pseudo-data由nominal模型生成，不能覆盖model misspecification；
- 30-toy closure只具有初步诊断精度。

与主线 MC-template analysis 相比，data-driven方法可能消除或减小某些 SPS MC-shape
modeling systematics，但同时引入 control-region、event-mixing、subtraction和
signed-weight component fits等新假设。不能因为当前E3 envelope小，就推断总系统误差
必然比主线小。

因此当前结果最稳妥的判断是：

> 已完成一组有价值的 ATLAS-style method variations 和初步 closure；现有 systematic
> 数字是“当前测试集合下的 envelope”，尚不足以证明完整、最终的 data-driven
> systematic uncertainty。

这也是为什么在整轮问答结束前，不应据此直接修改 nominal/final 结论。

---

## 本轮结束后再统一判断的潜在事项

以下仅登记为待决问题，不等于已决定建立 request 或修改 slides：

1. 是否需要更明确说明2492是selected candidates，PP由后续fit统计提取；
2. 是否需要补充其他三个一维 component-fit图，正文或backup待定；
3. 是否需要增加 control-region 的定性SPS/DPS composition证据；
4. 是否需要把 P7/P8 图内局部误差与 P16 joint statistical uncertainty明确区分；
5. 是否需要扩展 statistical covariance 与systematic variation集合；
6. 是否需要弱化“系统误差已完整评估”或“结果统计主导”的结论措辞。
