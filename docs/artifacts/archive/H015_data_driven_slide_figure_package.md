# H015 accepted data-driven slide figure package

- Status: `accepted`
- Producer / consumer: `JPsiJPsi` / `pre-updates`
- Acceptance date: 2026-08-29
- Producer version: `sync/chensh-20260730@b89508566a2096bf40e3a99addac7d09fd901e2b`
- Consumer review: `docs/qa/archive/H015_consumer_review_2026-08-29.md`
- Archived requester: `docs/requests/archive/H015_JPsiJPsi_data_driven_slide_figure_package.md`
- Producer package: `JPsiJPsi/docs/answers/H015_preupdates_data_driven_slide_figures/`
- Accepted figures: `slides/figures/accepted/H015/`
- Accepted machine sources and metadata: `slides/data/accepted/H015/`

## Acceptance evidence

- Three request copies were byte-identical before the consumer annotation, SHA256
  `d3172be24b10d5d3b61a66b028e9ba1cf3d8df3e9a9c1ce57199c384a5b5bbc7`.
- Final producer package checksums pass 39/39; package checksum-index SHA256 is
  `202a8021af566c2d1d0dc6fd770b6bb5d65896bd6a3a126f9fc36d43b5747d7a`.
- The eight figures unaffected by the targeted correction remain byte-identical to the first
  review. F05 and F07 pass the final overlap, notation, wording and slide-size visual checks.
- F05/F07 numerical columns are exactly equal to H014 accepted evidence. The first-round
  12-cell, fit-QA, bootstrap, closure and systematic checks remain valid.
- No selection, fit, bootstrap, systematic or ROOT-production rerun occurred.

## Consumption boundary

All F01--F10 PDFs and PNGs are accepted as presentation artifacts. They may be used to rebuild
P8 onward, but each page still requires user review before entering `slides/main.tex`. H015 adds
no new physics claim and does not authorize downstream `sigma_DPS` or `sigma_eff` uncertainty
claims without the separate covariance and human physics gate.
