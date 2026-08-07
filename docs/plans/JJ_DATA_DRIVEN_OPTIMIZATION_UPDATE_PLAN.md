# JJ data-driven optimization update：active workflow plan

状态：用户于 2026-08-07 批准 request-first 流程；页面级 slides 计划等待 codes
交付后制定。本文件在本轮 update 完成前保持 active，完成后移入 archive/plans/。

## 第一层：主要框架

1. 向 JPsiJPsi/codes 投递正式 request，由 codes 完整盘点上一轮 data-driven
   cross-check 后的优化、判断主要进展、核定当前 data-driven central scheme，
   并汇总已经计算的统计和部分系统误差。
2. Codes 优先复用已有代码输出、metadata、CSV 和 PDF；缺少必要产物时只提出
   follow-up，不自动运行新分析或制作新图。
3. Codes 交付 ready package 后，pre-updates 验收全部进展、nominal 定义、误差
   范围和重要图片，并提交用户 physics gate。
4. 只有 accepted artifacts 确定后，pre-updates 才制定真正的两层页面计划。
   重要图片原则上全部展示；主文与 backup 分配由证据和叙事决定。
5. 页面计划经用户批准后，完整构建并归档当前 deck。新 deck 只复用标题页和
   thanks 页格式、主题及宏，其余正文和 backup 从零开始。
6. 新 deck 使用单页迭代、内部编号 hook、完整 fastcheck/latexmk 和逐页视觉 QA。

## 第二层：工作批次

### 批次 1：request 与共享状态

- 创建 pre-updates active request；
- 在 codes 的 answer workspace 保存收到的 request；
- 在共享 progress.md 登记唯一 open request；
- 不修改 slides/main.tex，不归档当前 deck。

### 批次 2：codes 内容交付

- Codes 提供完整优化 inventory 和主要进展判断；
- Codes 冻结或明确标注 provisional data-driven central scheme；
- Codes 提供统计和部分系统误差的 machine-readable breakdown；
- Codes 列出所有重要现有图片、metadata、commit 和推荐用途。

### 批次 3：slides consumer 验收

- 核对代码、metadata、输出和 figure manifest；
- 检查是否优先复用已有 artifacts；
- 区分 validated result、provisional spread、tested variation 和 missing source；
- 将 nominal、systematics 和最终数值提交用户确认。

### 批次 4：真正的两层页面计划

- 根据 accepted package 决定 narrative、总页数和 recap 深度；
- 为全部重要图片安排主文或有充分理由的 backup；
- 逐页记录目的、证据、图片、takeaway 和 conclusion gate；
- 向用户提交页面计划，未批准前不创建新正文。

### 批次 5：归档与从零制作

- 先构建并归档旧 main.tex、project_setup.tex 和 PDF；
- 保留批准的标题与 thanks 格式；
- 清空旧主体和 backup，从零创建新 update；
- 单页确认后运行全量构建、warning 审计、内部编号检查和视觉 QA；
- 完成后归档本计划与 request/answer，并更新本项目 handoff。

## Human gates

- Codes 的主要进展排序是 producer recommendation，slides 侧仍需验收。
- data-driven nominal、selection、control region、fit、systematics 和最终数值
  必须由用户确认。
- 新 plot、analysis run、fit、bootstrap、variation 或 production 必须另行获得
  人工授权。
- Codes 返回前不推测页面结构；artifact accepted 前不写入 slides。
