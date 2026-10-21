# Data-driven SPS/DPS separation in prompt J/psi-pair production

The data-driven method constructs the DPS shape from prompt single-J/psi candidates in data.
The two J/psi slots are fitted separately in mass and decay length. Resolution parameters are
first calibrated, then fixed in a yield-only fit used to compute prompt sWeights. Every allowed
Jpsi1 candidate is paired with every Jpsi2 candidate from a different source event. This
deterministic all-pairs construction avoids random mixing seeds and yields 6,061,749 accepted
mixed pairs.

Prompt-prompt yields in data are extracted with a four-dimensional fit in twelve cells of
abs(delta_y) and abs(delta_phi). The mixed DPS template is normalized in one control cell,
abs(delta_y)>=1.8 and abs(delta_phi)<=pi/2, where the nominal method assumes DPS dominance.
Subtracting the normalized DPS contribution gives the SPS component. The resulting
data-driven internal nominal is
`f_DPS = 0.170 +/- 0.059 (stat.) +0.010/-0.011 (method syst.)`.

The statistical uncertainty is the standard deviation of 500 fixed full source-event bootstrap
replicas. All 500 succeed without replacement; 1000/1000 single-J calibrations, 1000/1000
yield-only fits and 6000/6000 prompt-prompt cell fits pass the quality criteria. This supersedes
the older successful-only ensemble that required 529 attempts.

The method systematic combines three independently defined groups in quadrature: single-J
category dependence, control-region definition and purity, and a pure-DPS Monte Carlo
full-workflow closure test. Alternative two-dimensional binning and four one-dimensional
projection fits are retained as cross-checks and are not included. Acceptance, efficiency,
correction and detailed four-dimensional fitter variations remain deferred or backup studies
and must not be silently interpreted as zero.

The four one-dimensional template fits give f_DPS values of 0.1719 from abs(delta_y), 0.1713
from abs(delta_phi), 0.1635 from the pair mass and 0.1706 from abs(y(JJ)). Their agreement is a
formal consistency check; the shifts are not assigned as an additional systematic.

This result is the nominal definition within the data-driven method. It remains a cross-check
of the CMS MC-template result and does not replace the CMS nominal measurement.
