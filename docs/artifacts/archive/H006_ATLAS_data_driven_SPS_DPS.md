> Lifecycle: accepted historical manifest, archived on 2026-08-02. It is evidence, not current handoff status; use shared `../../../../docs/progress.md` for live state.

# H006 accepted artifact manifest

- Producer: `JPsiJPsi`
- Consumer: `pre-updates`
- Artifact: H006 ATLAS-style data-driven SPS/DPS cross-check
- Producer status: accepted for presentation
- Consumer status: accepted and consumed in slides
- Source request: `../JPsiJPsi/docs/requests/H006_preupdates_ATLAS_data_driven_SPS_DPS_slides_request.md`

## Slides inputs

All PDF inputs below are copied without modifying their physics content from
`../JPsiJPsi/tests/atlas_data_driven_sps/results/`:

- `validation/marginals_weighted.pdf`
- `pp_data_2d_adaptive14_unified_mJJ7p5/pp_yield_map.pdf`
- `templates_2d_adaptive14_unified_mJJ7p5/dps_normalized_map.pdf`
- `templates_2d_adaptive14_unified_mJJ7p5/sps_data_driven_map.pdf`
- `templates_2d_adaptive14_unified_mJJ7p5/sps_weight_map.pdf`
- `templates_2d_adaptive14_unified_mJJ7p5/dps_weight_map.pdf`
- `component_fits_delta_y_unified_mJJ7p5/delta_y_component_yields.pdf`
- `component_fits_delta_y_unified_mJJ7p5/delta_y_component_shapes_normalized.pdf`

## Verification

- Beamer source: `slides/main.tex`
- Metadata: `slides/project_setup.tex`
- Built PDF: `build/main.pdf` (ignored build product)
- Pages: 32
- Aspect ratio: 16:9
- Fastcheck: passed
- Two-pass pdflatex: passed
- Compile warnings: no overfull boxes, undefined controls, or LaTeX errors
- Visual QA: all pages reviewed; key tables and result pages re-rendered after fixes

## Copied-file SHA256

c83e9efaaca1e4ad789eccc4fd566ec46fa8f385359f4b0d5bb2c563209dd227  slides/figures/accepted/H006/delta_y_component_shapes_normalized.pdf
42d716a7e7b7d803c71e4430d02af5fc8206c73e06650607802f9002cb554456  slides/figures/accepted/H006/delta_y_component_yields.pdf
194d561f1b065e298892e3ebf266e3cf4377092cff791a7bc78e2bb5d34de988  slides/figures/accepted/H006/dps_normalized_map.pdf
877bb643adfcbddc8cfb84dca71458c3f6114b2216713cc2897b28e98ea511e7  slides/figures/accepted/H006/dps_weight_map.pdf
934afc2480c5c96810d5e74277a627121c9b3dc7c1aa702e6b28afaaee9c9195  slides/figures/accepted/H006/marginals_weighted.pdf
d5b143875a7142cbb7fcd5352505590be831b2ceb7e00f494af8d8b457fa7596  slides/figures/accepted/H006/pp_yield_map.pdf
c9c8d89e915126b5bba4da5f2a49419985e8a507fea280c5b900b41c556baaaa  slides/figures/accepted/H006/sps_data_driven_map.pdf
9f7d851054ceae77f89d88235ac9b4a21beb7d074a74005dd81f2abad1945a6a  slides/figures/accepted/H006/sps_weight_map.pdf

## H006-T1 theory-shape comparison

Status: accepted after explicit user physics-definition confirmation on 2026-07-31.

Slides consume three producer PDFs:

- `delta_phi_theory_vs_data_sps_shape.pdf`
- `m_JJ_theory_vs_data_sps_shape.pdf`
- `delta_y_theory_vs_data_sps_shape.pdf`

Presentation definition: unit-area differential shapes; no data/theory ratio.
Each slide records its variable-specific assumptions and retains the pending
fiducial/unit/density/envelope-definition caveat.

SHA256:

- delta_phi: `2bfc8b680b778eb9e24d6f6a98264f31cba3b32d95c44da0c4e229dc662d9d9b`
- m(JJ): `ccfe8bcae82e30a870549b77f5c2fb93dc820dc2cd22d91b6cc0e5449799372f`
- delta_y: `85d188bc851fdda1589f1e60611b0dd625c03333f1389af87b41578dc63d5086`


## H008--H010 accepted consumption (2026-07-31)

User confirmed H008, H009, and H010 for pre-updates consumption. Producer
`metadata.txt` files are the physics wording source; CSV files were used to
cross-check every transcribed value.

- H008: accepted. `h008_control_region_validation.pdf` is embedded on slide 7.
  Slides 7--9 state that nominal-CR equality is imposed by normalization and is
  not independent DPS-purity evidence or absolute theory--Data agreement.
- H009: accepted. `h009_validation_summary.pdf`, page 2, is embedded on slide
  25. H009 metadata/CSV facts are used on slides 10 and 20--29 for the
  central-value-only weight scope, 50,000-toy definition, closure ensembles,
  tested variations, envelope scope, and propagated uncertainty breakdown.
- H010: accepted. H010 metadata/CSV values are used on slide 30. The producer
  PDF is retained as an accepted source artifact but is deliberately not
  embedded because it displays the forbidden stale `1.59 mb`; the slide quotes
  only the corrected code-side recomputation and identifies it as not yet
  updated in the AN text.

Accepted copied PDFs and SHA256:

- `fae9b473cdddce42a8acdc57302c5cc54da138a2cc6c3e8ff194cf5ab48923f0`  `slides/figures/accepted/H006/h008_control_region_validation.pdf`
- `bdb3c6d78868bfa2085100a367d8884b456231e5f8a3b71d9236b04a9cc40e8b`  `slides/figures/accepted/H006/h009_validation_summary.pdf`
- `dca1d430149a017964c39cdc505ee7f6f44654cc3b370601748c53beb78792ff`  `slides/figures/accepted/H006/h010_nominal_comparison.pdf`

Final verification: fastcheck passed; `latexmk` completed; 32 pages; no
overfull/underfull boxes or LaTeX errors; full-deck contact-sheet review plus
focused visual checks for slides 4--9, 25, and 28--30 passed. Final build hash:
`65649d3187c9893fcd0562f4fe05bfea4014f30d58bb798b095f882a0af7e6e9`.


## Emergency report edition (2026-07-31)

At user request, the current `build/main.pdf` is a 31-page emergency edition:

- the former H008 P7 is omitted; H008 remains accepted but is not displayed;
- P29 compares `Data-driven results` with the current CMS AN nominal; the internal
  H006 label and both requested explanatory lines are omitted;
- the two deferred discussion topics are recorded in
  `docs/qa/H006_emergency_report_followups_2026-07-31.md`.

Fastcheck, latexmk, warning audit, and focused visual QA of P6--P7 and P29
passed. PDF SHA256: `9c98200d5cd54ecfed52debbd00d8036e627ca351754d8cadfcf7279f98c824b`.


## Report layout update (2026-07-31)

- Title page identifies `Speaker: Lekai Yao`.
- Slides 13--15 use accepted nominal PP-corrected-yield PDFs:
  `delta_phi_component_yields.pdf`, `evt_mass_component_yields.pdf`, and
  `evt_y_component_yields.pdf`.
- The SPS-leakage closure/sensitivity definition is explicit on slide 21.
- Summary is slide 28; Reference is slide 29; statistical pseudoexperiment
  details are backup slides 30--31 after `\appendix`.

Yield-PDF SHA256: `3ca798cd6265376f9319e2d0da46f03838715eaed278d2204ccdbdf8f4fea143`,
`33543fd950037bb440698bf7743c8193fda005a26fffb1ae0b5eb1f9420b91b0`,
`899e1dc348fda7dbd73790c3020b9c8a8f950c327d7bb963247319997c1282d6`.


## H007 acceptance (2026-08-04)

User confirmed the consumer validation and changed H007 from `ready` to `accepted`.
The accepted input area now uses the six H007 PDFs: `marginals_weighted.pdf`,
`pp_yield_map.pdf`, `dps_normalized_map.pdf`, `sps_data_driven_map.pdf`,
`sps_weight_map.pdf`, and `dps_weight_map.pdf`. Producer metadata remains the
physics source of truth; selection and 14-cell binning are unchanged.

Consumer verification: fastcheck and `latexmk` passed; the deck remains 31
pages with no reported LaTeX layout warnings. The H007-updated build SHA256 is
`3eccb1285350f8e7c688f2ba06c54a49800bdd52e5d24c8cd68120295172f512`.
It differs from the frozen pre-H007 report edition, as intended: the archive
was frozen before the accepted H007 files replaced the working slide inputs.

Frozen report archive:

- `archive/20260731/JJ_update_260731.pdf`
- `archive/20260731/main.tex`
- `archive/20260731/project_setup.tex`
