# H015 producer answer: data-driven presentation figures

Status: `ready` for pre-updates consumer review. This package contains presentation-only
figures derived from H014-accepted machine sources. It does not change or rerun selection,
fits, the fixed-500 bootstrap, systematic variations, geometry, or physics values.

## Direct result

F01-F10 are complete as vector PDF and matching PNG preview. All figures are single-page
16:9 outputs. F01-F03 and F10 use the actual current 12-cell geometry; no visible
`adaptive 14 cells` wording remains.

F04 uses the saved central `global_yield_fit_result`, saved candidate trees, and the existing
`Model_4D_tot.root` workspace to draw mass and decay-length projections. The plotting entry
point does not call `fitTo`. It was compiled and run in CMSSW_10_6_20 / ROOT 6.14/09 /
cmssw-el7.

F06 uses exactly the accepted fixed 500/500 replica values. The plotting input reproduces
the accepted mean `0.170392853017` and sample SD `0.059331299623`; its 20 uniform histogram
bins over `[0.02,0.40]` are frozen in `data/bootstrap_plot_metadata.json`.

## Figure status

- F01: prompt-prompt Data yield map, with 12/12 accepted cell fits.
- F02: current 12-cell geometry and the single control cell.
- F03: CR-normalized data-derived DPS and signed SPS residual maps.
- F04: saved two-stage single-J/psi fit projections and component curves.
- F05: accepted single-J/psi category dependence and asymmetric envelope.
- F06: accepted fixed-500 full-workflow bootstrap distribution.
- F07: accepted control-region definition/purity variations and group envelope.
- F08: accepted pure-DPS full-workflow closure and uncertainty mapping.
- F09: the three included method groups and separate up/down quadrature.
- F10: signed per-cell SPS residual significance, explicitly diagnostic only.

## Reproduction and provenance

Run `bash scripts/run_all.sh` from this package directory or the repository root. The script
only validates/copies accepted machine values and redraws figures. Machine inputs are under
`data/`; exact paths, hashes, selection, definitions, commands, caveats, page sizes, and PNG
dimensions are in `figure_manifest.csv` and `figure_manifest.md`. Package-wide hashes are in
`package_checksums.sha256`; package status and dirty-file ownership are in
`package_metadata.json`.

The package is producer `ready`, not consumer `accepted`. pre-updates must still perform its
hash, wording, geometry, numerical, and slides-size visual review before copying any figure
into the deck.
