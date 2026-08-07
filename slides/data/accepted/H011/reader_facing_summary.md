# Data-driven SPS/DPS update

The main methodological advance is to purify prompt single-J/psi candidates before event
mixing. The two J/psi slots are fitted separately in mass and decay length, and their prompt
sWeights are used to construct pairs from different source events. All allowed cross-event
pairs are included, eliminating the random-pair sampling dependence of the earlier method.

The current provisional central scheme uses separate central and forward single-J/psi fits,
split at `abs(y)=1.2`. It builds 6,061,749 accepted cross-event pairs, normalizes the mixed DPS
template in `abs(delta_y)>=1.8` and `abs(delta_phi)<=pi/2`, and obtains
`f_DPS=0.169980`. All nominal component fits and all tested control-region variations converge.

A full source-event bootstrap has produced 500 successful replicas. Their sample standard
deviation is `0.056796`, but 29 additional attempts fail in category calibrations or a sparse
prompt-prompt cell. For the current presentation this SD is labeled as the statistical
uncertainty with the 500/529 failure disclosure. The completed category and control-region
studies give separate tested method sensitivities of `+0.007264/-0` and
`+0.001319/-0.010591`; treating the groups as independent gives a provisional combined
`+0.007382/-0.010591` systematic uncertainty. It is not a complete systematic uncertainty.

The remaining limitations are the single-J/psi functional-form and fixed-shape dependence,
acceptance/efficiency and pair-trigger corrections, alternative two-dimensional binning,
control-region purity, and the residual assumption that prompt single-J/psi kinematics can be
used to model DPS after mixing. The method remains a data-driven cross-check and does not
replace the current CMS MC-template nominal without a new physics decision.
