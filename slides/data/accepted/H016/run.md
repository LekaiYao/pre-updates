# H016 reproduction

From the JPsiJPsi repository root:

```bash
python3 docs/answers/H016_preupdates_data_driven_final_results/scripts/calculate_results.py
python3 docs/answers/H016_preupdates_data_driven_final_results/scripts/plot_figures.py
python3 docs/answers/H016_preupdates_data_driven_final_results/scripts/build_package.py
```

These commands only perform deterministic post-processing and plotting. Pair systematics use the five AN percentages directly without normalization; sigma_eff systematics use exact source-by-source endpoints. They do not rerun the
selection, single-J fits, PP fits, fixed-500 bootstrap, or method systematics. The frozen analysis
artifacts were produced with CMSSW_10_6_20 / ROOT 6.14/09 / cmssw-el7.

The mass extrapolation input is reproduced from the existing DPS GEN-only acceptance sample by
`GEN_nofilter/DPS/ULPythia2016/CMSSW_10_2_5/src/4mu_acc/count.cpp`. The actual inputs are
`/eos/user/c/chensh/JPsiJPsi/GEN_nofilter/DPS/ULPythia2016/CMSSW_10_2_5/src/4mu_acc/direct/DPS_2016_JJ_[1-10].root`;
their hashes, sizes and mtimes plus the captured command/output are frozen in `validation.txt`. The two
`GEN_pair_id` slots are kept separate, both J/psi satisfy `10<=pT<=40 GeV` and `abs(y)<2.0`,
same-source combinations are excluded, and `epsilon_m=N(mJJ>7.5)/N(all)=30256975/30644975`.

For compatibility QA of the relevant JJ PP fitter source, compile it without running a fit in the
required environment and direct ACLiC products to `/tmp`:

```bash
mkdir -p /tmp/leyao/h016_aclic
cmssw-el7 --command-to-run 'cd Data/ULntuple16/CMSSW_10_6_20/src && eval "$(scramv1 runtime -sh)" && cd /eos/home-l/leyao/26JJ/JPsiJPsi && root -l -b -q -e "gSystem->SetBuildDir(\"/tmp/leyao/h016_aclic\",true); std::cout << \"compile_status=\" << gSystem->CompileMacro(\"tests/atlas_data_driven_sps/fit_pp_2d_adaptive.cpp\",\"kO\") << std::endl;"'
```
