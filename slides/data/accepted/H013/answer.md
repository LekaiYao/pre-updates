# H013 answer: data-driven sigma_DPS and sigma_eff propagation

Status: `ready`. These are producer recommendations for a data-driven internal
result, not the CMS MC-template nominal. Final numbers and uncertainty labels
still require the user gate requested by H013.

## Direct result

Using the accepted H011 central value and the current AN pair cross section,

`sigma_DPS = f_DPS * P = 0.169980427756 * 37.2 pb`

gives the machine-precision value

`sigma_DPS = 6.3232719125232 pb`.

With `X = BR * sigma(single J/psi) = 10.63 nb` and `BR = 0.05961`,

`sigma_eff[mb] = 0.001 * 0.5 * X[nb]^2 / (BR^2 * sigma_DPS[pb])`

gives

`sigma_eff = 2.514527745559081 mb`.

The recommended display precision is `sigma_DPS = 6.32 pb` and
`sigma_eff = 2.51 mb`. The current recommended uncertainty statement is:

`sigma_DPS = 6.32 +0.51/-0.58 (partial syst.) pb`, with stat pending the
`Cov(f_DPS,P)` gate.

`sigma_eff = 2.51 +0.26/-0.20 (partial syst.) mb`, with stat pending the same
covariance gate.

The word `partial` is mandatory: the H011 systematic does not yet cover all
listed sources.

## Statistical covariance audit

The H011 source-event bootstrap and the AN pair cross section use the same CMS
pair-data sample. Existing successful replicas save the refitted `f_DPS`, but do
not save a matched replica-level corrected total pair cross section. Therefore
the current artifacts cannot determine or estimate `Cov(f_DPS,P)`.

Using

`Var(fP) = P^2 Var(f) + f^2 Var(P) + 2 f P Cov(f,P)`

with `Cov(f,P)=rho * sigma_f * sigma_P`, the sensitivity is:

- `rho=-1`: `sigma_DPS stat = 2.010840595788 pb` and
  `sigma_eff stat = 0.799649775568 mb`;
- `rho=0`: `sigma_DPS stat = 2.115288955251 pb` and
  `sigma_eff stat = 0.841184274136 mb`;
- `rho=+1`: `sigma_DPS stat = 2.214817109095 pb` and
  `sigma_eff stat = 0.880762284921 mb`.

The `rho=0` values are an independent-input reference, not the recommended
correlation-resolved result. The ATLAS single-J/psi statistical input is from a
different experiment and dataset and is added independently in `sigma_eff`.
It is numerically small (`0.01 nb`) but retained.

All statistical scenarios inherit the H011 caveat: the quoted
`sigma_f = 0.056796474528` is the sample SD of 500 successful replicas from 529
attempts. There were 29 failures: 14 Jpsi1 category calibrations, 7 Jpsi2
category calibrations, and 8 sparse PP-cell fits. Because these failures are not
proved missing at random, the successful-only distribution is conditional and
may be biased. A joint source-event bootstrap recording both `f_DPS` and `P` is
the minimum follow-up; H013 does not authorize running it.

## Partial systematic propagation

For `sigma_DPS`, the propagation keeps the full AN pair systematic `2.5 pb`,
including its BR contribution, because `sigma_DPS` is reported as a full physical
cross section. Category, CR, and the pair aggregate are separate current sources.
Endpoint propagation followed by the approved independent-group quadrature gives:

`sigma_DPS partial syst = +0.505963324936/-0.579476688377 pb`.

For `sigma_eff`, the same endpoint method preserves inverse-denominator direction
and nonlinearity. The pair BR component is first removed from the AN aggregate:

`pair non-BR syst = sqrt(2.5^2 - (37.2*0.0078)^2) = 2.483104342230 pb`.

The ATLAS integrated-bin systematic `0.09 nb` and its separate 1.13% luminosity
uncertainty are included as distinct sources. This gives:

`sigma_eff partial syst = +0.255645451864/-0.201842751309 mb`.

The asymmetry reverses as expected: downward changes of `f_DPS` or `P` increase
`sigma_eff`, while upward changes decrease it. Exact one-source endpoints, not a
symmetrized denominator error, are combined.

The current category and CR groups are independent only under the user-approved
H011 provisional rule. Combining them with the AN pair aggregate and ATLAS
sources at zero correlation is a provisional source-definition assumption:
their currently evaluated knobs are disjoint. It is not evidence that future
acceptance/efficiency/trigger or fit-model variations are uncorrelated.

## Branching fraction and units

The CMS pair result is a full cross section because AN divides the corrected
yield by `L * BR^2`. The ATLAS numerator is visible, `X=BR*sigma_single`. Defining
the visible DPS pair cross section as

`Y = BR^2 * sigma_DPS = 0.0224688115292353 pb`,

the formula is simply `sigma_eff = 0.5 * X^2 / Y`, with the required unit factor
`0.001` from `nb^2/pb` to `mb`. The common dimuon BR uncertainty cancels exactly.
The BR central value is needed only to convert the full pair input to `Y`; its
uncertainty is neither added separately nor left inside the pair systematic for
`sigma_eff`. This avoids the old double counting in the generic nominal script.

Both inputs use prompt J/psi, `10<pT<40 GeV`, `abs(y)<2.0`, and nominal
unpolarized acceptance. The CMS denominator additionally requires
`m(Jpsi Jpsi)>7.5 GeV`. There is no corresponding observable for an inclusive
single-J/psi numerator, so this cut is not applied to `X`. The result is therefore
a fiducial effective cross section tied to that pair-specific cut, consistent
with the existing H006 E4 convention; it should not be described as cut-independent.

## Correlation and double-counting conclusion

The detailed decisions are in `uncertainty_source_map.csv`. The main points are:

- CMS pair and ATLAS single-J/psi luminosities are independent because they come
  from different experiments and datasets;
- BR cancels for `sigma_eff` but remains in the full `sigma_DPS` uncertainty;
- H011 category and CR variations do not numerically duplicate AN acceptance,
  efficiency, trigger, or fitter sources;
- this absence is a missing-uncertainty problem, not proof of zero correlation;
- future shared correction or fit variations must produce `f_DPS` and `P`
  together, so their covariance is propagated rather than counted twice.

Still missing are the H011 correction variations, functional form, fixed shapes,
alternative 2D binning, factorization bias, and a CR-purity/SPS-leakage study.
Consequently no complete systematic uncertainty is claimed.

## Numerical cross-checks

The implementation reproduces the old H006 E4 inputs:

- `sigma_DPS = 7.160002611679201 pb` versus reference `7.16000261168 pb`;
- `sigma_eff = 2.220675540092444 mb` versus reference `2.22067554009 mb`;
- `sigma_eff stat = 0.220214013320374 mb` versus reference
  `0.22021401332 mb`.

It also reproduces the current CMS MC-template nominal post-processing from
`sigma_DPS=12.6 pb`:

`sigma_eff = 1.261908148155081 mb`, consistent with code-side `1.26191 mb` and
current AN `1.26 mb`. The stale `1.59 mb` value is not used.

## Reproducibility and consumer gate

Run `python3 propagate.py`; it uses only the Python standard library and rewrites
the machine-readable result files deterministically. No ROOT, RooFit, fit,
bootstrap, or large artifact is run. `request.md` is byte-identical to the
requester copy.

Before consumer acceptance, the user must confirm either a statistical
correlation convention or the need for the proposed joint bootstrap, and confirm
that the partial-systematic display above is the desired interim result.
