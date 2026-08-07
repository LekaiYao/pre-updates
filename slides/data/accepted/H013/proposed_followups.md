# H013 proposed follow-up

The existing artifacts cannot determine `Cov(f_DPS, sigma_pair)` because each
successful replica stores the refitted fraction but not a matched total corrected
pair cross-section estimator. The minimum correlation-resolving follow-up is a
joint source-event bootstrap that records both estimators for every accepted draw,
then computes their covariance before propagating `f_DPS * sigma_pair`.

This follow-up must preserve the existing 500/529 failure accounting or first
resolve the conditional-selection bias. It was not executed under H013 because
the request explicitly forbids new bootstrap production.

For a complete systematic uncertainty, matched variations are also needed for
pair acceptance/efficiency/trigger corrections, single-J functional form,
fixed-shape parameters, 2D binning, CR purity/SPS leakage, and the residual
single-J factorization assumption. Shared correction and fit variations should
produce `f_DPS` and `sigma_pair` together so their covariance is not guessed.
