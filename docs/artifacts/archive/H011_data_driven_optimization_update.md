> Lifecycle: accepted artifact manifest, archived on 2026-08-07. It records the
> consumer acceptance evidence; live cross-project status is tracked only in
> shared `../../../../docs/progress.md`.

# H011 accepted artifact manifest

## Identity and status

- Producer：`JPsiJPsi`
- Consumer：`pre-updates`
- Consumer status：`accepted`（2026-08-07）
- Producer package：`../JPsiJPsi/docs/answers/H011_preupdates_data_driven_optimization_update/`
- Provenance correction：`../JPsiJPsi/docs/answers/H012_preupdates_H011_provenance_metadata_correction/`
- Codes context：`sync/chensh-20260730@24823a5d476c18aee1f3134e86da645063965ef1`
- Git note：ordinary codes worktree clean；`tests/`、`docs/` 和 artifacts 被忽略，
  因而身份由精确路径和 SHA256 冻结，不把修正虚构为 Git commit。

## Accepted physics wording

- Data-driven internal central：`abs(y)=1.2` category、slot-specific prompt sPlot、
  cross-slot all-pairs、same-source rejection，`f_DPS=0.169980427756`。
- 500 个成功 full-chain source-event bootstrap replicas 的 sample SD
  `0.056796474528` 在本轮 slides 中称为 `stat`；必须同时披露 500/529 attempts、
  29 次失败、失败分类和 conditional-selection caveat。
- Category 与 CR groups 分别解释，并按用户批准的独立 group-envelope quadrature
  合并为 provisional `syst=+0.007382225292/-0.010590504745`。
- 该 systematic 不完整；data-driven 结果不替代 CMS MC-template nominal。仅在结尾
  与当前 AN nominal 比较，禁止使用含 stale `1.59 mb` 的 comparison PDF。

## Consumer verification

- H012 request 的 requester/producer copies SHA256 均为
  `3124140b8f9c5732f8544daeb853a784d8703bfca8cc120dbb70257c1c22a30f`。
- `correction_manifest.csv` 的 5/5 current files 均存在，实际 SHA256 与 after hash
  一致，且全部声明 `physics_output_changed=false`。
- Generator 及 central/三组 CR metadata 中不再出现陈旧 artifact、selection 或旧
  bootstrap provenance 字符串；H011 answer workspace 的同类 stale scan 为空。
- Central 与 CR metadata 清楚区分 PP Data selection、upgraded DPS construction 和
  central full-chain bootstrap；三组 CR 边界与各自 summary/CSV 一致。
- H011 `source_manifest.csv` 的 20/20 source/artifact hashes 与实际文件一致。
- H011 `pdf_byte_identity.csv` 的 23/23 before/after hashes 相同；实际文件 hash 也
  23/23 匹配，并与 H011 `figure_manifest.csv` 一致。
- Central `f_DPS=0.169980427756` 及三组 CR values
  `0.171298940286, 0.167432887843, 0.159389923011` 与实际 summary/CSV 一致。
- Producer 的 CMSSW_10_6_20 / ROOT 6.14/09 compile evidence 存在；PDF 时间戳仍为
  2026-08-06，支持“未重跑 fit/plot、只修正 metadata”的交付说明。

## Accepted consumption boundary

- Slides 可消费 H011 `figure_manifest.csv`、`source_manifest.csv`、
  `nominal_definition.json`、`uncertainty_breakdown.csv`、machine-readable summaries
  及其指向的 verified artifacts。
- 23 个 PDF 均完成 identity 验证，但 manifest 中标为
  `historical_nominal_comparison_forbidden` 的 PDF 仍禁止展示或引用其 stale 数值。
- 2026-08-07 正式首版制作已将 16 个新图复制到
  `slides/figures/accepted/H011/`，并将 13 个 machine-readable/provenance 文件复制到
  `slides/data/accepted/H011/`；local figure hashes 与 accepted manifest 全部匹配。
- Stale nominal-comparison PDF 未复制、未引用。首版构建与逐页 QA 见
  `docs/qa/JJ_DATA_DRIVEN_FIRST_DRAFT_2026-08-07.md`。
