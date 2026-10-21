# H014 accepted slide inputs

Consumer acceptance date: 2026-08-29.

Producer package:
`JPsiJPsi/docs/answers/H014_preupdates_data_driven_latest_nominal_uncertainty/`
at `sync/chensh-20260730@24823a5d476c18aee1f3134e86da645063965ef1`.

The package files and 16 indexed text/CSV artifacts were copied byte-identically after
consumer review. Their source SHA256 values are recorded in `package_metadata.txt` and
`artifact_index.csv`; the 10 code hashes are in `code_manifest.csv`.

Accepted slide claims include the global two-stage single-J fit/sPlot, deterministic
cross-slot all-pairs mixing, 12-cell PP extraction and single-CR decomposition, fixed
500/500 bootstrap, three-group method systematic, and the frozen `f_DPS` result.

Figure exclusions:

- `pp_yield_map.pdf` is not copied or accepted for slides because its visible title says
  `adaptive 14 cells` although the plotted artifact contains the current 12-cell geometry.
- `sps_significance_map.pdf` is not copied or accepted for the same stale visible title.
- No H014 PDFs are frozen here. Any later figure consumption requires a separate selection
  from the verified manifest and a visual/title audit.

The visible deck must not describe the MC template fit as “nominal” or the data-driven
method as a “cross-check”. Downstream `sigma_DPS`/`sigma_eff` uncertainties remain outside
this acceptance because the replica-matched covariance is unresolved.
