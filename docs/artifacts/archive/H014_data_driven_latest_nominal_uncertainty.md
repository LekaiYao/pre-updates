# H014 accepted artifact manifest

## Identity and status

- Producer: `JPsiJPsi`
- Consumer: `pre-updates`
- Producer status: `ready`
- Consumer status: `accepted with explicit figure exclusions` (2026-08-29)
- Producer version:
  `sync/chensh-20260730@24823a5d476c18aee1f3134e86da645063965ef1`
- Producer workspace:
  `../JPsiJPsi/docs/answers/H014_preupdates_data_driven_latest_nominal_uncertainty/`
- Consumer review: `docs/qa/archive/H014_consumer_review_2026-08-29.md`
- Local accepted inputs: `slides/data/accepted/H014/`

## Accepted facts

- Global calibrated two-stage single-J mass-times-ctau fit for each slot; resolution scales
  are frozen before yield-only sPlot.
- Deterministic all-cross-event `Jpsi1 x Jpsi2` construction with same-source rejection and
  signed pair weights; 6,061,749 accepted mixed pairs.
- Twelve-cell PP extraction and one control cell at `abs(delta_y)>=1.8` and
  `abs(delta_phi)<=pi/2`; the internal central assumes zero SPS leakage in that cell.
- User-frozen data-driven result:
  `f_DPS=0.170423232645 +/-0.059331299623 (stat.)
  +0.010177290968/-0.011083850610 (method syst.)`.
- The bootstrap is a fixed 500/500 full source-event ensemble with zero failures and no
  replacement. The method systematic combines three approved groups in quadrature.
- Four one-dimensional projections are consistency diagnostics and do not enter the
  systematic; deferred sources are not treated as zero.

## Consumer verification and exclusions

- Package hashes: 13/13 matched.
- Indexed artifacts: 16/16 matched.
- Indexed figures: 12/12 hashes matched.
- Indexed code: 10/10 matched.
- `pp_yield_map.pdf` and `sps_significance_map.pdf` are excluded because their visible titles
  retain the stale phrase `adaptive 14 cells` for current 12-cell content.
- No H014 PDF is currently accepted into the local slide figure area.
- Downstream `sigma_DPS` and `sigma_eff` uncertainties are not superseded by H014 because
  replica-matched covariance with the total pair estimator remains unresolved.

## Visible wording boundary

The deck compares methods through inputs, assumptions, limitations, advantages and results.
It does not assign “nominal” to the MC template fit or “cross-check” to data-driven.
