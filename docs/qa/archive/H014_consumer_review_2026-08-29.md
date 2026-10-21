# H014 consumer review

Status: accepted with explicit figure exclusions on 2026-08-29.

## Identity and package checks

- Requester and producer request copies are byte-identical, SHA256
  `47c31e6d18f36b0ee90d7e61a0648bc171aff5a27c8592d54aaa841b4f6baed5`.
- Producer branch/HEAD matches package metadata:
  `sync/chensh-20260730@24823a5d476c18aee1f3134e86da645063965ef1`.
- All 13 package-file hashes match `package_metadata.txt`.
- Actual files match 16/16 artifact-index hashes, 12/12 figure-manifest hashes and
  10/10 code-manifest hashes; no indexed file is missing.
- Four tracked producer dirty files are disclosed in `nominal_definition.json`, are not
  H014-owned, and are not referenced by the artifact, figure or code manifests.

## Physics and QA checks

- Source definition: 119 files, 6132 entries, 2492 selected events.
- Single-J extraction: separate slot fits, calibrated two-stage mass-times-ctau model,
  frozen resolution scales before yield-only sPlot; both fit summaries close the prompt
  sWeight sum to the fitted prompt yield.
- Mixing: 6,118,202 Cartesian pairs, 2,456 same-source rejects, 53,997 mass rejects,
  6,061,749 accepted pairs; signed prompt-sWeight product times nominal correction.
- PP extraction: 12/12 fits pass in the current 12-cell geometry.
- Decomposition independently reproduces
  `f_DPS = 832.859420193 / 4887.00635042 = 0.170423232645`.
- Fixed bootstrap is 500/500 with no failures or replacement; sample SD is
  `0.0593312996229`.
- Independent quadrature reproduces method systematic
  `+0.010177290968/-0.011083850610` from category, CR/purity and pure-DPS closure groups.
- Deferred sources remain explicit; downstream covariance with the total pair estimator
  remains unresolved.

## Differences and exclusions

- The two known stale metadata fields are correctly superseded by current summary/cells/code:
  global is user-frozen and the actual geometry is 12 cells.
- `pp_yield_map.pdf` and `sps_significance_map.pdf` visibly say `adaptive 14 cells`.
  Their hashes are valid, but their visible titles conflict with the current 12-cell claim;
  they are excluded from slide acceptance. The numerical artifacts are unaffected.
- The producer reader-facing wording retains historical method-status labels. It is accepted
  only as internal reference; the current deck uses the user-mandated neutral wording.

## Local freeze and consumption boundary

- Accepted package and selected text evidence are frozen under `slides/data/accepted/H014/`.
- No H014 PDF is copied locally in this acceptance.
- P5--P7 may use accepted machine facts to build source-backed TikZ schematics.
- New downstream `sigma_DPS` or `sigma_eff` uncertainty claims still require a separate
  covariance and physics gate.
