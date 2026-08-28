# 2026-08-27 总结 slides 暂停归档

## 状态与用途

本目录保存尚未完成的 X(3872) 总结 slides，供紧急的 2026-08-27 update 完成后继续制作。
它不是正式报告归档，不得发布为 `pbpb_updates/X_update_260827.pdf`。

- 内容范围：截至 2026-08-20，不包含其后结果；
- P1--P4：已完成人工审核；
- P5--P9：已完成快速编译与视觉检查，仍为待人工审核 draft；
- 尚未制作：nominal reweighting、weighted ML、fit、两年份扩展、总结和 thanks 部分；
- 未运行完整 `latexmk` 或正式 `archive_slides.sh`。

## 文件

- `main.tex`：暂停时的完整主稿快照；
- `project_setup.tex`：对应项目设置快照；
- `sections/`：P2--P9 的 section 源码；
- `previews/p2-p4.pdf`：已审核的 P2--P4；
- `previews/p5-p9-draft.pdf`：待审核的 P5--P9；
- 计划：`docs/archive/2026-08/slides_summary_20260827_paused.md`。

## 后续恢复

1. 先读取本文件和暂停计划；
2. 将 `sections/` 中需要继续编辑的文件复制回 `slides/sections/`；
3. 以本目录 `main.tex` 为内容基线，但保留届时 active `main` 的通用 workflow 更新；
4. P2--P4 可作为已审核内容恢复；P5--P9 必须重新快速编译并经人工确认后才能纳入主稿；
5. 继续使用固定目录 `tmp/p2_background_dataset_selection/` 和
   `tmp/p5_reweighting_motivation/`，不得创建轮次目录。

## 快照校验

```text
main.tex                                      fdd62dbf556d9b5e4715248189677d12396ce967cbad91e11c9f92d9200ac161
sections/p2_dataset.tex                       c53d94fb378c508ccacf8b31227a0038273a42a0c96082009a2bbfd3095e395c
sections/p3_presel_ppref.tex                  705d47e4325c822933f70cfdb990b516c9544dca3ab8f7a836854c69cb7bce39
sections/p4_presel_pbpb.tex                   f924af63a01a618450a1dd3237d8e3de9d61e0d6fbd0b26e97c1dd2331d47afa
sections/p5_p9_reweighting_motivation.tex     410168eede7bb34e10aa5ffe425496ef06a0750cfff52afa42bd80bea2811e54
previews/p2-p4.pdf                            6fcdf59900ea32a77667f989ef04083f466ce7ba549b7958fe6f2096d58648d4
previews/p5-p9-draft.pdf                      bc5e844be1715bbbfebf5f8f1bc5c3ceb765c844a25668960f780a8028c3b892
```
