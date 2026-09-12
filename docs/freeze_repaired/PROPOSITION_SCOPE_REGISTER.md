# Repaired Stage 8 — Proposition / Scope Register

Date: 2026-09-12 (JST)

## T1 — Integration ordering

**Maturity: PROVED. Formal coverage: PROOF-CRITICAL CORE.**

For every parameter vector in strict `R+`, the metered rational-expectations fixed point exists uniquely and satisfies

`h_0<h_M<h_F`.

This is a quadratic-baseline result. No claim is made outside `R+` or for arbitrary concave demand.

## T2 — Threshold separation

**Maturity: PROVED. Formal coverage: PROOF-CRITICAL CORE.**

For every parameter vector in strict `R+`,

`mu_M=Phi(l,h_M)<Phi(l,h_F)=mu_F`.

The abstract statement “`h_M<h_F` plus strictly increasing `Psi` implies `Psi(h_M)<Psi(h_F)`” is only a sufficient-condition / organizing lemma. It is not primitive demand generality.

## T3 — Pure-regime gap

**Maturity: PROVED. Formal coverage: PROOF-CRITICAL CORE.**

For every parameter vector in strict `R+` and every `mu` with `mu_M<mu<mu_F`, neither pure flat nor pure metered expectation is self-consistent. The certified branch has a unique aggregate mixed resolution `(h*,rho*)` with `h_M<h*<h_F`.

Equality cases `mu=mu_M,mu_F` are excluded. No global equilibrium characterization outside `R+` is claimed.

## B1 — Threshold-collapse benchmark

**Maturity: PROVED.**

If integration is architecture-insensitive so that `h_M=h_F`, then `mu_M=mu_F`; the threshold split and strict pure-regime gap collapse.

## W1 — Fixed-installed-base welfare wedge

**Maturity: PROVED. Formal coverage: PROOF-CRITICAL CORE.**

Holding installed `(l,h)` fixed on the quadratic both-served branch, with `d>0,h>0`,

`mu_P-mu_W=d h p*(h)>0`.

This is a fixed-allocation result only and is not a global endogenous-welfare theorem.

## W2 — Endogenous architecture welfare ranking

**Maturity: NUMERICALLY SUPPORTED ONLY as sign-indeterminacy evidence.**

Strict-`R+` examples with opposite welfare rankings are retained. Therefore no unconditional flat-versus-metered welfare ranking is frozen.

## Robustness classification

- common-curvature nonquadratic examples: **NUMERICALLY SUPPORTED ONLY**;
- arbitrary strict concavity: **REJECTED as a general claim**; a retained counterexample reverses `h_M<h_F`;
- non-Uniform integration-cost CDF theorem: **not in the current certified claim set**;
- abstract order implication: **PROVED sufficient-condition lemma**, not a function-class theorem.

## Explicitly prohibited stronger wording

Do not claim all positive parameters, arbitrary concave demand, every heterogeneity distribution, arbitrary active sets, global mixed-equilibrium uniqueness outside `R+`, endogenous integration always creates a gap, metering is always socially excessive, flat pricing is always welfare superior, or a universal quality/model-improvement tariff transition.
