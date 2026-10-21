# JJ data-driven nominal-method and uncertainty update plan

Status: complete; P1--P23 accepted and incorporated; formal 23-page build passed
Date: 2026-08-28
Accepted input baseline: accepted state through the 2026-08-07 update
Target: a self-contained approximately 30-minute explanation of the role, current internal nominal
method, and uncertainty analysis of data-driven SPS/DPS separation in JJ; approximately 25 pages is
an initial planning estimate, not a hard limit

## Scope and fixed boundaries

- Code-side work has progressed beyond the accepted 2026-08-07 baseline and is reported to have
  completed a new data-driven internal nominal method and its uncertainty analysis.
- H014 completed consumer review on 2026-08-29. Selected machine/text inputs are accepted under
  `slides/data/accepted/H014/`; two PDFs with stale visible `adaptive 14 cells` titles are excluded.
- The 2026-08-07 deck and all frozen archives remain unchanged.
- This is a new deck from zero, not an edited or shortened copy of the 2026-08-07 narrative.
- Reuse only accepted physics artifacts and verified figures. Reuse the approved title/thanks
  geometry, project theme, macros, and selected layout components where useful.
- Visible wording in this update must describe the AN template-fit method and the data-driven
  method without assigning “nominal” to the MC template fit or “cross-check” to data-driven.
  Compare their inputs, assumptions, limitations, advantages, and results directly.
- H014 supersedes H011 for the current data-driven `f_DPS` central/stat/method-systematic definition.
  H013 downstream values are not updated because replica-matched covariance remains unresolved.
- Selection, fit, central definition, nominal status, systematics labels, and numerical values may
  not change without a separate user physics gate.
- Visible slide text must use reader-facing physics language and must not expose internal artifact
  or collaboration IDs.

## Audience and timing

- Presentation duration: approximately 30 minutes.
- Audience: analysis-group members who are not all familiar with the JJ analysis.
- Pedagogical consequence: introduce the AN template-fit construction and its reported
  `f_DPS` result before motivating the data-driven workflow through a method-level comparison.
- Initial working estimate: about 23--25 pages including title, thanks, and focused backup. Page
  count may change as needed for a clear 30-minute narrative; there is no hard page-count limit.

## Section review status

- Workflow: generate one logical section in ignored temporary source, review and revise it, then
  incorporate only the accepted version into `slides/main.tex`.
- “Incorporate into main” means merge TeX only. Rebuild `build/main.pdf` only when the user
  explicitly requests a full main compilation.
- Temporary review directories must begin with the corresponding page number, for example
  `tmp/review/p01_title/` or `tmp/review/p02_p05_role/`, so outputs remain easy to locate.
- Title section (P1): accepted by the user and incorporated into `slides/main.tex` on 2026-08-28;
  the formal one-page deck passed fastcheck, full latexmk compilation, log audit, and visual review.
- Current title draft: `Data-driven SPS/DPS separation in J/psi-pair production`.
- The title page has no subtitle, per user instruction.
- P2--P4 were accepted by the user and incorporated into `slides/main.tex` on 2026-08-29. P2 uses
  two AN input-shape figures; P3 uses two simultaneous-fit result figures and presents `f_DPS`;
  P4 compares MC-method limitations with data-driven advantages. The four-page formal deck passed
  fastcheck, full latexmk, log audit, visible-wording checks, and full visual QA.
- P5--P7 were accepted by the user and incorporated into `slides/main.tex` on 2026-08-29.
  The formal seven-page deck passed fastcheck, full compilation, log audit, and visible-wording
  checks. The first P8--P10 review batch was withdrawn because its P8/P9 analysis geometry and CR
  visuals were reconstructed on the slides side. H015 is now accepted, and the replacement batch
  `tmp/review/p08_p10_h015/` uses its producer-authored F01--F03 figures. P8--P10 were accepted and
  incorporated into `slides/main.tex` on 2026-08-29; the formal ten-page deck passed fastcheck,
  full compilation, log/wording audit, and full visual QA. Never integrate the withdrawn
  `tmp/review/p08_p10_pair_decomposition/` batch.
- The first P11--P13 batch was rejected and deleted; none of those pages entered `slides/main.tex`.
- The single-J fit-projection page was accepted and inserted after P6 on 2026-08-29. Former
  P7--P10 are now P8--P11. The formal eleven-page deck passed fastcheck, full compilation,
  log/wording audit, and full visual QA; statistical uncertainty begins at P12.
- P12--P13 were accepted by the user and incorporated into `slides/main.tex` on 2026-08-29.
  The formal 13-page deck passed fastcheck, full compilation, log/wording checks, and complete
  visual QA; method systematic uncertainty begins at P14.
- P14--P17 were accepted and incorporated into `slides/main.tex` on 2026-08-29. The formal
  17-page deck passed fastcheck, full latexmk compilation, log/wording checks, and focused visual
  QA; `build/main.pdf` SHA256 is
  `4ba13f94b42e981af0a608905dca5f66d6a2895a17d631b71aa3c99e55e00dee`.
- H016 final targeted consumer re-review is `accepted`. The accepted package freezes complete
  mass-extrapolation provenance, source-level pair-systematic propagation, exact asymmetric endpoints,
  and the user-approved preliminary conventions. Machine/text inputs are frozen under
  `slides/data/accepted/H016/` and F01--F04 under `slides/figures/accepted/H016/`. These outputs
  now support the result/closing section beginning at P18; each page still requires user review.
- Visible P18--P23 wording must compare the current data-driven and AN results without a
  `Preliminary` label. The producer metadata status remains unchanged; internal covariance and
  future-improvement caveats stay outside the visible deck.
- P18--P23 were accepted and incorporated into `slides/main.tex` on 2026-08-29. The formal
  23-page deck passed fastcheck, full latexmk, log/wording audit and full visual review;
  `build/main.pdf` SHA256 is `d180cc464336f7809d898db3ecdb0205b2668cdca39bfc15827c9d6ceeee4ef1`.

## Main framework

1. **AN template fit and motivation for data-driven — 4 pages including title.** Present the AN
   template-fit construction, its `f_DPS` result, and a direct comparison of MC-method limitations
   with data-driven advantages, without status labels for either method.
2. **Current data-driven construction and central fraction — 7 pages.** Build the workflow from
   single-J extraction and its fit projections through event mixing, PP extraction, current cell/CR
   geometry, and SPS/DPS decomposition.
3. **Statistical uncertainty — 2 pages.** Explain the source-event bootstrap, fixed ensemble,
   full-workflow rerun, estimator distribution, and accepted statistical interpretation.
4. **Method/systematic uncertainty — 4 pages.** Present the three selected sources separately and
   then show their asymmetric quadrature combination.
5. **Final results, derived cross sections, interpretation, and takeaways — about 6 pages.** Using the accepted
   H016 boundary, present the final `f_DPS` summary, `sigma_DPS`, `sigma_eff`, their uncertainty
   treatment, a direct method comparison, closing takeaways, and thanks.
6. **Backup — about 1 page.** Retain only a high-value accepted diagnostic if needed for discussion.

Initial estimate: approximately 23--24 pages including title, thanks, and focused backup; this is not a cap.

## Five-page breakdown

### Pages 1–5 — AN template fit and motivation for data-driven

| Page | Purpose and key content | Accepted evidence / visual | Transition or gate |
|---|---|---|---|
| 1 | Title: data-driven SPS/DPS separation in JJ | Approved title geometry and project metadata | Date/title metadata require user approval |
| 2 | AN template-fit method: SPS/DPS templates, fitted observables, and fit structure | Current accepted AN method definition and source-backed schematic | Establish how the MC-based separation is performed |
| 3 | AN template fit and its `f_DPS` result | Current accepted AN fit figure/result and concise uncertainty labels | Move from the existing result to method dependence |
| 4 | Why develop a data-driven method? | Side-by-side comparison of MC-method limitations and data-driven advantages | Motivate the data-driven construction without status labels |
| 5 | Current method roadmap | H014 accepted workflow diagram or a source-backed reconstruction | Begin the current nominal construction |

### Pages 6–10 — data-driven construction through CR normalization

| Page | Purpose and key content | Accepted evidence / visual | Transition or gate |
|---|---|---|---|
| 6 | Single-J source construction | H014 accepted extraction/calibration evidence | Define the two independent prompt-weighted source samples |
| 7 | Single-J mass and decay-length fit projections | H015 F04 producer fit-summary figure | Make the prompt extraction visible before event mixing |
| 8 | Deterministic cross-slot all-pairs mixing | H014 accepted pairing and rejection metadata | State factorization, same-source rejection, pair weight and mass selection |
| 9 | PP Data extraction in the common 2D phase space | H015 F01 producer PP-yield map | Establish the pair-data input in the common cells |
| 10 | CR normalization | H015 F02 producer CR geometry plus accepted equations | Fix the DPS normalization without interpreting it as a purity measurement |

### Pages 11–15 — central fraction, statistical uncertainty, and first systematics

| Page | Purpose and key content | Accepted evidence / visual | Transition or gate |
|---|---|---|---|
| 11 | Cell-by-cell DPS/SPS decomposition and integrated `f_DPS` | H015 F03 producer component maps plus H014 accepted result | Complete the central fraction extraction |
| 12 | Source-event bootstrap design | H014 accepted resampling and fixed-ensemble definition | Explain what is resampled and that the full workflow is rerun |
| 13 | Bootstrap QA and estimator distribution | H015 F06 fixed-500 distribution | Present the accepted statistical uncertainty |
| 14 | Single-J category/model source | H015 F05 category-dependence plot | Build the first selected systematic envelope |
| 15 | Control-region definition/purity source | H015 F07 CR-variation plot | Build the second selected systematic envelope |

### Pages 16–23 — remaining systematic, final results, and closing

| Page | Purpose and key content | Accepted evidence / visual | Transition or gate |
|---|---|---|---|
| 16 | Pure-DPS full-workflow closure source | H015 F08 closure plot | Map the closure bias to the third selected systematic |
| 17 | Asymmetric combination of the three selected sources | H015 F09 systematic-breakdown plot | Present the combined method uncertainty |
| 18 | Final data-driven `f_DPS` summary | Accepted H016 final-result figure and machine table | Freeze the latest result and uncertainty status |
| 19 | `sigma_DPS` final calculation | Accepted H016 propagation figure | Explain pair-cross-section input and uncertainties |
| 20 | `sigma_eff` final calculation | Accepted H016 propagation figure | Explain effective-cross-section convention and uncertainties |
| 21 | Data-driven result beside the AN template-fit result | Accepted H016 summary plus current accepted AN result | Compare values and inputs without method-status labels |
| 22 | Three closing takeaways | Role, construction, uncertainties, and derived results | Prepare the audience for discussion |
| 23 | Thanks | Approved closing geometry | Separate courtesy page after the conclusion |

### Page 24 — focused backup if needed

| Page | Purpose and key content | Accepted evidence / visual | Transition or gate |
|---|---|---|---|
| 24 | Focused backup if needed | H015 F10 corrected 12-cell significance map | Retain one high-value discussion aid |

## Draft and review workflow after approval

1. Produce one logical section quickly in an ignored temporary review source.
2. Compile and render only that section for user review; revise the temporary section until accepted.
3. Incorporate the accepted section into `slides/main.tex`; do not put rejected trials into main.
4. Repeat for the next section, using only artifacts accepted after H014 consumer review.
5. After all sections are incorporated, run the full build, internal-ID check, log audit, and
   complete visual QA.
6. Freeze the final PDF/source/setup under a new non-overwriting archive and move this plan to
   `docs/plans/archive/`.

## Completion gates

- Main framework and total page allocation explicitly approved by the user.
- H014 producer delta is complete, consumer-reviewed, user-approved where required, and selected
  slide inputs are accepted and traceable to a frozen local manifest.
- No change to physics definitions or numerical values without explicit approval.
- Page count remains proportionate to the approximately 30-minute talk; approximately 25 pages is
  a planning estimate rather than a completion gate.
- Build succeeds with no fatal, undefined, or material overflow issues.
- Every page passes visual inspection and visible text contains no internal collaboration IDs.
