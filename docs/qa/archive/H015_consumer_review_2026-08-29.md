# H015 consumer review

Status: `accepted` on 2026-08-29 after targeted F05/F07 producer correction and consumer
re-review. Accepted inputs are frozen under `slides/figures/accepted/H015/` and
`slides/data/accepted/H015/`; this review did not modify `slides/main.tex`.

## Identity and provenance checks

- Requester, producer and answer request copies are byte-identical, SHA256
  `d3172be24b10d5d3b61a66b028e9ba1cf3d8df3e9a9c1ce57199c384a5b5bbc7`.
- Producer Git state matches package metadata: clean
  `sync/chensh-20260730@b89508566a2096bf40e3a99addac7d09fd901e2b`.
- Package checksums pass 39/39. F01--F10 each provide one-page PDF and PNG; manifest
  page sizes, PNG dimensions and hashes match the actual files.
- F04 external ROOT inputs match the three hashes in the manifest. The plotting source
  reads the saved `global_yield_fit_result` and contains no `fitTo` call.
- Reproduction scripts validate/copy accepted inputs and redraw figures; no selection,
  fit, bootstrap or systematic rerun is present.

## Numerical and physics checks

- H015 `cells_current12.csv` is value-identical to the H014 accepted 12-cell table; the
  byte difference is newline encoding only. It contains 12 cells and one control cell.
- Independent cell summation gives
  `f_DPS = 0.170423232644604` and PP = DPS + SPS to floating-point precision.
- The 500 replica values independently reproduce mean `0.170392853017426` and sample SD
  `0.059331299622922`, matching H014 and the H015 metadata.
- Independent up/down quadrature gives `+0.010177290968035/-0.011083850609733`, matching
  the accepted method-systematic result.
- Single-J fit QA, category/CR variations and pure-DPS closure values match the accepted
  H014 machine evidence. No changed physics definition or value was found.

## Visual and wording review

- F01--F04 and F06--F10 have the requested reader-facing titles, 12-cell geometry where
  applicable, legible labels and no clipping. No banned method-status or internal request
  wording appears.
- F05 is not acceptable: the category-envelope annotation box obscures the
  `|y| split at 1.2` marker and its numerical label.
- F07 is not fully compliant with the global variable convention: the four angular rows
  are labeled `phi <= 70 deg` / `phi <= 110 deg`; they must use `|Delta phi|` (or the
  corresponding rendered Greek notation) consistently.

## Required producer fix

1. Move the F05 envelope annotation away from all three data rows so every marker and
   numerical label remains visible at slide size.
2. Change the F07 angular row labels to `|Delta phi| <= 70 deg` and
   `|Delta phi| <= 110 deg`, retaining the existing zero-/MC-leakage distinction.
3. Regenerate only the affected F05/F07 PDF and PNG files and refresh their manifest and
   package checksums. Do not rerun analysis, fits, bootstrap or systematic variations.

After those presentation-only corrections, consumer re-review may be limited to the changed
figures, visible text, updated hashes and package metadata. Until then H015 remains
`needs-fix` and none of its figures may enter `slides/main.tex`.


## Final targeted re-review

- Producer retained clean `sync/chensh-20260730@b89508566a2096bf40e3a99addac7d09fd901e2b`;
  request identity and the no-analysis-rerun declaration are unchanged.
- Updated package checksums pass 39/39. The eight unaffected figures remain byte-identical:
  16/16 prior PDF/PNG hashes match.
- F05 PDF/PNG hashes changed to remove the overlap. The envelope is now above the plot;
  all three markers and numerical labels are unobscured at slide size.
- F07 PDF/PNG and label-source hashes changed. All four angular rows now render
  `|Delta phi|` consistently; leakage markers, legend and numerical labels remain clear.
- Every F05/F07 `f_DPS` and signed-shift value is exactly equal to the H014 accepted table.
- Both corrected PDFs are single-page 16:9 vector outputs with matching PNG previews; no
  banned method-status or internal request wording is visible.

H015 therefore passes the consumer gate in full. F01--F10 may be consumed from the local
accepted directories, subject to normal per-slide user review before integration into main.
