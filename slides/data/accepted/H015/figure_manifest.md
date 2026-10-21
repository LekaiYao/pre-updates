# H015 figure manifest

Status: `ready` for consumer review.

## F01 - Prompt-prompt yield in Data

- PDF: `figures/pp_yield_map_current12.pdf` (`10bac02398a6defa605a280ba4618bad19bdebd0bd664a3380e802fdca34465a`)
- PNG: `figures/pp_yield_map_current12.png` (`1476cfc0349d842b039482d16037d643f98b1841e0d18e34f5357e311b3e47d3`)
- Machine source: `data/cells_current12.csv`
- Definition: N_PP and fitted uncertainty in each accepted cell
- Caveat: 12/12 accepted cell fits; errors are fitted prompt-prompt uncertainties

## F02 - Data-driven control region in the 12-cell phase space

- PDF: `figures/control_region_geometry_current12.pdf` (`33f6e052bcddfdecf13703a222411aa144f21e32816dd0f9d92834501eb5b638`)
- PNG: `figures/control_region_geometry_current12.png` (`2cc4a7d190b1d3ba4dcbe7d55bba420b7912a4df4cdb0e7f5cff4230d1edb176`)
- Machine source: `data/cells_current12.csv`
- Definition: Accepted 12-cell geometry with the single low-|Delta phi| control cell
- Caveat: Geometry only; the highlighted control cell supplies DPS normalization

## F03 - CR-normalized data-derived DPS yield; Data-derived SPS residual

- PDF: `figures/dps_sps_decomposition_current12.pdf` (`e540a7a826def1671d09e0550e0be0b10f638f6fe2a157fb72488be3b4298574`)
- PNG: `figures/dps_sps_decomposition_current12.png` (`0d18dd564d9c1ab0c086e0d6c3ef1b0ca744afa44cc12a3f001d0c32089d133a`)
- Machine source: `data/cells_current12.csv`
- Definition: Stored DPS/SPS yields and propagated per-cell uncertainties
- Caveat: Signed SPS residuals are retained without truncation

## F04 - Prompt single-J/psi extraction in Data

- PDF: `figures/single_jpsi_fit_summary.pdf` (`8318c98f2df543d017682ccaf1c534251cf61613f4d9b8f93123be37180082ae`)
- PNG: `figures/single_jpsi_fit_summary.png` (`5553be81e3f190ca53f88e0282d9ce2ee6194b578620ede5360b9db0062f7960`)
- Machine source: `data/single_jpsi_fit_qa.csv;tests/atlas_data_driven_sps/results/fdps_systematics_final_v1/category/global_calibrated/jpsi1_sweights.root;tests/atlas_data_driven_sps/results/fdps_systematics_final_v1/category/global_calibrated/jpsi2_sweights.root;Data/ULntuple16/CMSSW_10_6_20/src/NtupleAnalyzer/Model_4D_tot.root`
- Definition: Unweighted mass/decay-length projections with saved two-stage yield-fit parameters
- Caveat: Projection only; no fitTo call and no fit result was regenerated

## F05 - Single-J/psi category dependence

- PDF: `figures/single_jpsi_category_dependence.pdf` (`36bd0c0ba186334ba905f44f745959a4fbce91d66e262fbb10cd01534eadc031`)
- PNG: `figures/single_jpsi_category_dependence.png` (`7fd4efcb1267a46ce785d3214b7013733a9d40adcc931dd2dca6e70ce1932e05`)
- Machine source: `data/single_jpsi_category_dependence.csv`
- Definition: Accepted central value and pT/|y| category variations
- Caveat: Alternatives are variations; neither is assigned a method-status label

## F06 - Full-workflow bootstrap distribution

- PDF: `figures/bootstrap_fdps_fixed500.pdf` (`4e155265e4f38c1c0d03f93c3076f6f1f0f490f3099f3a6703826239bf4e279e`)
- PNG: `figures/bootstrap_fdps_fixed500.png` (`ee68c5e268ffe8fc96cd6f589e590f3aafc47a64c037977f23bf00a7a77ab6a2`)
- Machine source: `data/bootstrap_fdps_fixed500.csv;data/bootstrap_plot_metadata.json`
- Definition: Accepted fixed 500/500 full-workflow replica f_DPS distribution
- Caveat: No failed or replacement attempts; 20 fixed bins over [0.02,0.40]

## F07 - Control-region definition and purity variations

- PDF: `figures/control_region_variations.pdf` (`d270ac5a18f9ede328839f8ca5b291847d0c2dcc9fdb7c34a5bb7a6a95da4938`)
- PNG: `figures/control_region_variations.png` (`7ace94f8d336ce649337c00c12ea5db21aca9e98747bee3548960ddc42cd1f50`)
- Machine source: `data/control_region_variations.csv`
- Definition: Accepted CR-boundary and zero/MC-leakage f_DPS variations
- Caveat: Envelope is the accepted group envelope, not an additional fit

## F08 - Pure-DPS full-workflow closure

- PDF: `figures/pure_dps_full_workflow_closure.pdf` (`6edcb1af522b9f162d88be0b358860a3b85f33bf5fc15fbc1002f19dad9bf0c1`)
- PNG: `figures/pure_dps_full_workflow_closure.png` (`388cbd3d6ae5b141f0dcf9b840f02c3fbe9da358a4cb2cf6c4d8c15aedd9a3b4`)
- Machine source: `data/pure_dps_full_workflow_closure.json`
- Definition: Expected/recovered pure-DPS fraction and accepted mapping to Data uncertainty
- Caveat: Conditional on the current DPS simulation model being treated as correct

## F09 - Data-driven method uncertainty

- PDF: `figures/method_systematic_breakdown.pdf` (`ec1e0064c30535e82c75fda56920402fd68b72eb7da0bb9eea264dce68a4e71d`)
- PNG: `figures/method_systematic_breakdown.png` (`412e19f0a618fce5e0635420b9e9b1b9bd61410d0ac993b0e3ddb4d7c903cfa7`)
- Machine source: `data/method_systematic_breakdown.csv`
- Definition: Three included groups and separate upward/downward quadrature
- Caveat: Deferred and diagnostic sources are intentionally absent, not set to zero

## F10 - SPS residual significance by cell

- PDF: `figures/sps_significance_map_current12.pdf` (`2e6420aa4acb27a36b14956e8fa1c31df851d7d4cf2d92364d7d43b097c04e39`)
- PNG: `figures/sps_significance_map_current12.png` (`7975367e9db6753477731cb2dec7ad7ea1442693a992e01947de0e1625e838bb`)
- Machine source: `data/cells_current12.csv`
- Definition: Stored signed per-cell SPS residual significance
- Caveat: Per-cell diagnostic only; not a global significance or extra systematic
