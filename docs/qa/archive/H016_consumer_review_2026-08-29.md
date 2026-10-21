# H016 consumer review — 2026-08-29

Status: `accepted` after the targeted producer revision and consumer re-review documented below.

## Scope checked

- Requester, producer, and answer-workspace request copies.
- Producer Git branch/HEAD and dirty state.
- Package checksum index, machine inputs/results, propagation code, validation record, manifests.
- Four new PDF/PNG figures and the reused H015 F07 reference.
- Independent arithmetic for `f_DPS`, `sigma_DPS`, `sigma_eff`, asymmetric systematics, and rho scan.
- Targeted rerun of the existing DPS GEN-only `count.cpp` because package metadata and the actual
  ROOT input path disagreed.

## Checks passed

1. Three request copies are byte-identical, SHA256
   `e894b4aa92e137d184469c40896c8a98cefaf1dde1d298650aeb6adb9c07c5ee`.
2. Producer state is `sync/chensh-20260730@b89508566a2096bf40e3a99addac7d09fd901e2b`;
   current tracked worktree is clean. H016 reports a clean intake state.
3. All 19 entries in `package_checksums.sha256` pass.
4. Accepted `f_DPS=0.170423232645`, fixed-500 stat `0.059331299623`, and method systematic
   `+0.010177290968/-0.011083850610` match H014.
5. Conditional `sigma_DPS(mJJ>7.5)=6.339744254394 pb` and its reported rho=0 propagation reproduce
   the machine inputs.
6. The existing `count.cpp` rerun reproduces `pool1=7772`, `pool2=3943`,
   `nTried=30644975`, `nEvent=30256975`, hence `epsilon_m=0.987338870402`.
7. SPS-MC leakage is correctly recorded as a member of the CR definition/purity envelope, not a
   fourth independent systematic; the negative endpoint is the 110-degree MC-leakage variant.
8. Four new figures are single-page 16:9 PDFs with matching PNGs; rendered pages are readable and
   cross-section figures are visibly labelled preliminary. H016-F05 correctly reuses accepted H015 F07.

## Blocking findings

### 1. Mass-extrapolation provenance and uncertainty are incomplete

- `inputs.json` names repository-local
  `GEN_nofilter/.../direct/DPS_2016_JJ_[1-10].root`, but those files do not exist there.
  `count.cpp` actually reads `/eos/user/c/chensh/JPsiJPsi/.../direct/`.
- The package does not record the ten actual ROOT paths with hashes/size/mtime, the `count.cpp` hash,
  or a captured command/output that rebuilds the counts from ROOT. `calculate_results.py` only consumes
  already-entered counts from `inputs.json`.
- `epsilon_m` is fixed with no statistical or model uncertainty. The package repeatedly says this was
  omitted “by current user instruction”, but no such user gate exists in H016 or the current slides
  handoff.
- Correlation of this DPS-MC extrapolation with the existing pure-DPS closure/model dependence is not
  discussed.

Required fix: correct the input path and freeze full provenance; provide a reproducible extraction
record; estimate the source-event/statistical and relevant model uncertainty, or present a precise
proposal for a user gate without claiming prior approval; map overlap with the pure-DPS closure source.

### 2. Pair-cross-section systematic is not source-level

The request requires a source-level correlation/cancellation map. H016 instead retains the CMS pair
`2.5 pb` as one aggregate row (or one non-BR aggregate row for `sigma_eff`) and assumes independence
from the data-driven method systematic. The current AN provides five active sources: branching fraction,
CMS luminosity, acceptance/efficiency, lifetime-variable choice, and fitter stability. In particular,
acceptance/efficiency and fitting sources can overlap conceptually with pair corrections and PP/single-J
fit variations used in the data-driven workflow; independence is not established.

Required fix: expand the five AN sources in `uncertainty_source_map.csv`, propagate them individually,
and state evidence for correlation, cancellation, or unknown status against every relevant `f_DPS`
source. Do not silently preserve aggregate independence where the relationship is unknown.

### 3. Asymmetric `sigma_eff` propagation changed method without a gate

`calculate_results.py` uses a linear Jacobian for the inverse dependence on `f_DPS`. The earlier H013
propagation used endpoint evaluation. With the current inputs:

- exact `f_DPS` contribution to `sigma_eff`: `+0.172250/-0.139542 mb`;
- H016 linear contribution: `+0.161048/-0.147875 mb`;
- after combining the other current components, exact total is approximately
  `+0.248016/-0.226525 mb`, versus reported `+0.240371/-0.231752 mb`.

The difference changes the recommended two-decimal upward uncertainty from `+0.24` to `+0.25`.

Required fix: explicitly choose and justify endpoint, Jacobian, or toy propagation, obtain the required
human gate if changing the established convention, and regenerate tables/figures consistently.

## Human gates still open

1. Whether rho=0 may remain the visible preliminary statistical propagation while
   `Cov(f_DPS,sigma_pair_total)` is unresolved.
2. Whether and how to use the new `epsilon_m` correction and its uncertainty.
3. Whether the corrected `sigma_eff` may enter this update as a preliminary result.

## Consumer decision

H016 is `needs-fix`, not `accepted`. H016-F01 is numerically consistent with already accepted H014
facts and H016-F05 is already accepted through H015, but this does not partially accept the H016 package.
Slides must continue to consume the existing H014/H015 accepted copies until a corrected H016 package
passes re-review and the user physics gates.


## Final targeted re-review

- Producer remains clean at
  `sync/chensh-20260730@b89508566a2096bf40e3a99addac7d09fd901e2b`; the three request copies
  remain byte-identical. The revised package checksum index passes 22/22.
- The ten actual DPS GEN-only ROOT paths now match the files on EOS. All ten size/mtime entries
  match; the first and last ROOT hashes and the `count.cpp` hash were independently spot-checked.
  The frozen reproduction record gives the previously reproduced counts and
  `epsilon_m=0.987338870402081`.
- The user explicitly approved a fixed central `epsilon_m` correction without uncertainty for this
  preliminary round; the package no longer asserts that the uncertainty is zero and records the
  future source-event/model treatment without putting it into the visible slide claim.
- The five AN pair-systematic percentages are now explicit sources. Their independent quadrature is
  `6.8193548%` or `2.53679999 pb`; the rounded AN display value `2.5 pb` is not used as an exact input.
- Independent source-by-source recomputation reproduces
  `sigma_DPS=6.339744 +/-2.209492 +0.574668/-0.597425 pb` and
  `sigma_eff=2.476240 +/-0.863018 +0.253003/-0.223538 mb`. The latter uses exact asymmetric
  endpoints; the branching-fraction term cancels as specified.
- The user-approved rho=0 preliminary statistical reference and conditional-independence convention
  are explicit. Unknown covariance remains a future improvement, not a blocker for this update.
- Only changed F02--F04 were re-rendered. They are single-page 16:9, readable, unclipped and visibly
  preliminary. Unchanged F01 and reused accepted H015 F07 were not redundantly re-audited.

## Final consumer decision

H016 passes the consumer gate in full. Its frozen local machine/text inputs and F01--F04 figures may
be consumed for P18 onward, subject to the normal page-level user review. This acceptance does not
modify `slides/main.tex` or rebuild `build/main.pdf`.
