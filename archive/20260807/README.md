# JJ quick progress update — 2026-08-07

## Positioning

This archive freezes the slides used for a **quick internal presentation of analysis progress that
had not yet been reported**. It is intentionally a status snapshot, not a polished or publication-
quality deck, and not the design/content baseline for the next update.

The next update should be planned and authored as a new deck. It may selectively reuse accepted
physics results, verified artifacts, figures, macros, and individual ideas from this snapshot, but
must not inherit the full page sequence or wording by default. The approved title/thanks geometry
remains reusable under the project rules.

## Frozen contents

- `JJ_update_260807.pdf`：30-page 16:9 presentation shown on 2026-08-07.
- `main.tex`：exact Beamer body used to build the archived PDF.
- `project_setup.tex`：exact presentation metadata used for the archived PDF.
- `SHA256SUMS`：identity of the three frozen files.

Source repository state before the archive commit：
`analysis/jj@cf68d1992c19ad45424435981c125ac6a83fdcac`。

## Physics and writing boundary

- Data-driven `f_DPS` and effective-cross-section material comes only from accepted H011/H013
  artifacts.
- The data-driven result remains an internal cross-check and does not replace the CMS MC-template
  nominal.
- The quoted effective-cross-section uncertainty is a provisional partial systematic;
  `Cov(f_DPS,P)` remains unresolved and the statistical uncertainty is pending.
- This archive records what was shown. It does not freeze future slide order, emphasis, wording,
  main/backup allocation, or a future nominal/systematic decision.

Build and visual QA are frozen in
`docs/qa/archive/JJ_DATA_DRIVEN_FIRST_DRAFT_2026-08-07.md`.
