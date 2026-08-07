# H013 accepted artifact manifest

## Identity and acceptance

- Producer：`JPsiJPsi`
- Consumer：`pre-updates`
- Producer workspace：`../JPsiJPsi/docs/answers/H013_preupdates_data_driven_sigma_eff/`
- Codes context：`sync/chensh-20260730@24823a5d476c18aee1f3134e86da645063965ef1`
- AN context：clean `main@f9111cf83716d44ec63ae04600ad970d8fed6ab4`
- Producer status：`ready`
- Consumer status：`accepted`（2026-08-07）
- User physics gate：accepted current-round central values and provisional partial systematic;
  statistical covariance remains unresolved and must be displayed as pending, never replaced by the
  `rho=0` reference.
- Consumer review：`docs/qa/H013_consumer_review_2026-08-07.md`

## Accepted result and wording boundary

- Data-driven internal result：`sigma_DPS=6.3232719125232 pb`，recommended display
  `6.32 pb`。
- Effective cross section：`sigma_eff=2.514527745559081 mb`，recommended display
  `2.51 mb`。
- Provisional partial systematic：
  `sigma_DPS=+0.505963324936/-0.579476688377 pb`；
  `sigma_eff=+0.255645451864/-0.201842751309 mb`。
- Statistical covariance between the H011 `f_DPS` bootstrap and AN pair-total cross section is not
  identifiable from existing artifacts. The `rho=-1,0,+1` values are sensitivity/reference only;
  no formal statistical uncertainty is accepted for `sigma_DPS` or `sigma_eff` in this round.
- Mandatory caveats：data-driven internal cross-check、partial/incomplete systematic、stat pending
  covariance、500/529 bootstrap conditioning；不得表述为替代 CMS MC-template nominal。
- CMS nominal comparison uses the corrected `sigma_eff=1.261908... mb` convention; stale
  `1.59 mb` remains forbidden.

## Consumer verification

- Requester/producer request copies were byte-identical before lifecycle annotation，SHA256
  `7e7e0db5ec8f74f8e1c8a31ae31f0f4f8cb93110e80e02da88c01cf784a6c9a6`。
- H011/AN source hashes and all producer package hashes matched current files.
- `propagate.py` passed `py_compile`; an isolated `/tmp` rerun reproduced `results.csv`、
  `propagation_details.json` and `cross_checks.json` byte-for-byte.
- Independent central-value and endpoint-systematic calculations reproduced all accepted values.
- BR cancellation、inverse-denominator asymmetric directions、H006 E4 and CMS nominal numerical
  cross-checks passed；19-row uncertainty source map preserved missing/unknown sources.

## Local accepted inputs and SHA256

The following producer files were copied byte-identically to `slides/data/accepted/H013/`：

- `f48f744ba700345ceda030736b517275536382f77654d07ae747d9beaf435d24`  `README.md`
- `3c230525ec40623c905026e675773dd695b445faad74537e242602bd696b887b`  `answer.md`
- `ae76ef55ae8f5c1e29533a815db4cc43f4435dd6df01a08cebd52d8bc10245d6`  `artifact_metadata.txt`
- `ad32f42fc3d77fe621b9750e1c950659475fe3456d99c69b2803c7f47714031a`  `cross_checks.json`
- `3a899e679e0a8743ccca35eaec48a3425e6bf7b47e818afc42791d425b4af223`  `inputs.json`
- `beb0c9ce80d03f2ee77a102b18749109e199cd784e298d6d30fad0905ca689db`  `propagate.py`
- `83e4f61affebf7cc8df16a672d14cb8801638868b6c004cbb02e648637aa1cf3`  `propagation_details.json`
- `2de9b6b803836edd749be73da75bb35fba793a1bd8b72805fcaa90b1c5552408`  `proposed_followups.md`
- `18a753d81a1c2833369fcc5cff73404b6581d767331338b4e9c464b9e5cf829f`  `results.csv`
- `e3488d5066172f01456ed53c27bb79e885a159fceb1db0fa76b4ecd8ffab1798`  `uncertainty_source_map.csv`

## Slides consumption

P21 may compare the data-driven and CMS nominal results using compact center-plus-uncertainty
notation. It must show both `f_DPS` and `sigma_eff`; the data-driven `sigma_eff` uncertainty is the
accepted provisional partial systematic only and must visibly retain `stat pending`.
