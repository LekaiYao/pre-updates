# H013 consumer review：data-driven sigma_DPS 与 sigma_eff propagation

日期：2026-08-07  
Producer artifact：`../JPsiJPsi/docs/answers/H013_preupdates_data_driven_sigma_eff/`  
Consumer verdict：**technical review passed; awaiting user physics gate**  
Artifact status：`ready`，尚未转为 `accepted`

## 已通过的核对

- Requester 与 producer `request.md` byte-identical，SHA256 均为
  `7e7e0db5ec8f74f8e1c8a31ae31f0f4f8cb93110e80e02da88c01cf784a6c9a6`。
- Codes context 为 `sync/chensh-20260730@24823a5d476c18aee1f3134e86da645063965ef1`；
  AN context 为 clean `main@f9111cf83716d44ec63ae04600ad970d8fed6ab4`。
- `inputs.json` 中 H011 uncertainty、accepted manifest、AN result/systematics 与 Appendix F
  的 SHA256 全部与当前文件匹配。
- `artifact_metadata.txt` 登记的 9 个 producer 文件 SHA256 全部匹配实际文件。
- `propagate.py` 通过 `py_compile`；在 `/tmp` 独立重跑后，`results.csv`、
  `propagation_details.json` 和 `cross_checks.json` 均 byte-identical。
- 独立复算确认中心值：`sigma_DPS=6.3232719125232 pb`、
  `sigma_eff=2.514527745559081 mb`。
- 独立 endpoint 复算确认 provisional partial systematic：
  `sigma_DPS=+0.505963324936/-0.579476688377 pb`，
  `sigma_eff=+0.255645451864/-0.201842751309 mb`。
- 分母不确定度映射到 `sigma_eff` 时方向正确反转；CMS pair BR component 从
  `sigma_eff` 的 pair aggregate 中移除，没有再次加入 PDG BR；完整 `sigma_DPS`
  保留已发表 pair systematic。
- 旧 H006 E4 和当前 CMS MC-template `sigma_eff=1.261908... mb` numerical
  cross-check 通过；未使用 stale `1.59 mb`。
- `uncertainty_source_map.csv` 覆盖 19 项来源，明确区分 included、missing、unknown
  correlation 和 exact cancellation；没有把 H011 partial systematic 冒充完整误差。

## 统计 covariance 结论

H011 successful replicas 保存了 `f_DPS`，没有保存与每个 replica 匹配的 corrected
pair-total estimator，因此现有 artifacts 无法确定 `Cov(f_DPS,P)`。Producer 正确地没有
静默采用 `rho=0`，而只给出 sensitivity/reference：

- `rho=-1`：`sigma_DPS stat=2.010840595788 pb`，`sigma_eff stat=0.799649775568 mb`；
- `rho=0`：`sigma_DPS stat=2.115288955251 pb`，`sigma_eff stat=0.841184274136 mb`；
- `rho=+1`：`sigma_DPS stat=2.214817109095 pb`，`sigma_eff stat=0.880762284921 mb`。

这些数值仍继承 500/529 attempts、29 failures 和 successful-only conditional-selection
caveat。`rho=0` 只能是 independent-input reference，不是 correlation-resolved result。

## 未满足的 acceptance gate

未发现需要 codes 修正的实现或 provenance defect，但根据 H013 request 与项目规则，以下
事项必须由用户确认后才能将 artifact 转为 `accepted`：

1. 接受中心值 `sigma_DPS=6.3232719125232 pb`、`sigma_eff=2.514527745559081 mb`；
2. 是否批准当前 provisional partial systematic 及显示口径；
3. statistical treatment 选择：保持 `stat pending` 并要求后续 joint bootstrap，或明确
   采用某个 provisional correlation convention；
4. 是否接受推荐舍入 `6.32 pb` 和 `2.51 mb`，并始终保留 data-driven internal、
   partial/incomplete systematic 和 non-nominal wording。

在上述 gate 完成前，H013 保持 open、producer artifact 保持 `ready`，不得写入 slides。
