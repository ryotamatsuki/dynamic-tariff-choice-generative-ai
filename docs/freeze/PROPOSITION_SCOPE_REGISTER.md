# Stage 8 — Proposition / Scope Register

## T1 — Integration ordering

**Maturity: PROVED. Formal coverage: PROOF-CRITICAL CORE.**

For every parameter vector in certified regular region `R`, the metered rational-expectations high-use installed mass exists uniquely and satisfies `0<h_M<h_F`.

No claim at mass caps, outside `R`, or when another active set is globally optimal.

## T2 — Threshold separation

**Maturity: PROVED. Formal coverage: PROOF-CRITICAL CORE.**

For every parameter vector in `R`, `mu_M<mu_F`.

Abstract sufficient-condition version: if `h_M<h_F` and provider gross metering gain `Psi(h)` is strictly increasing, then `Psi(h_M)<Psi(h_F)`.

This is not a theorem for arbitrary concave demand.

## T3 — Pure-regime gap

**Maturity: PROVED. Formal coverage: PROOF-CRITICAL CORE.**

For every parameter vector in strict `R` and each `mu` satisfying `mu_M<mu<mu_F`, neither pure flat nor pure metered expectation is self-consistent.

On the certified regular branch there is a unique mixed resolution. Baseline mixed state `h*` satisfies `Phi(l,h*)=mu` and

`rho*=K_H(h_F-h*)/[d p(h*)]`.

Equality boundaries are excluded. Global uniqueness outside `R` is not claimed.

## B1 — Threshold-collapse benchmark

**Maturity: PROVED.**

If integration is exogenous or architecture-insensitive so `h_M=h_F`, then `mu_M=mu_F`; the pure-regime gap collapses to one ordinary threshold.

## W1 — Fixed-installed-base private/social wedge

**Maturity: PROVED. Formal coverage: analytic only.**

For fixed `(l,h)` on the certified both-served branch with `d>0,h>0`,

`mu_P-mu_W=d h p*(h)>0`.

This is a fixed-allocation benchmark only.

## W2 — Full endogenous welfare ranking

**Maturity: NUMERICALLY SUPPORTED ONLY as sign-indeterminacy evidence.**

Within the baseline family, architecture-commitment welfare ranking reverses for admissible integration-cost parameters. Therefore no unconditional welfare ranking is asserted.

## Quality-transition statement

**Maturity: CONDITIONAL COMPARATIVE-STATIC INTERPRETATION.**

A `flat -> gap/mixed -> metered` path can arise when quality moves the certified thresholds monotonically relative to a fixed activation cost. No universal AI lifecycle law is claimed.

## Approved robustness

- General strictly increasing integration-cost CDFs only under explicit antitone/interiority/crossing sufficient conditions.
- Nonquadratic power-utility cases `r=3,4`: numerical robustness only.
- Abstract threshold-separation theorem from ordered architecture-induced states plus increasing `Psi`.

## Prohibited stronger wording

Do not claim:

- all positive parameters;
- arbitrary concave demand;
- every heterogeneity distribution;
- arbitrary active sets;
- global mixed-equilibrium uniqueness outside `R`;
- endogenous integration always creates a regime gap;
- metering is always socially excessive;
- flat is always welfare superior;
- universal quality-driven tariff transition.
