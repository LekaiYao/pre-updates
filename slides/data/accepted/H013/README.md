# H013 reproducibility

Run from any directory with Python 3:

```bash
python3 /eos/home-l/leyao/26JJ/JPsiJPsi/docs/answers/H013_preupdates_data_driven_sigma_eff/propagate.py
```

The script uses only the Python standard library and rewrites `results.csv`,
`propagation_details.json`, and `cross_checks.json` deterministically. No ROOT,
fit, bootstrap, or large artifact is read or produced.
