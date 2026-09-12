# Dynamic Tariff Choice for Generative AI

Theory project on dynamic tariff architecture, sunk AI-specific integration, and welfare.

## Status

**Stage 8 repaired theory freeze completed — THEORY FROZEN / GO TO REPRODUCIBILITY SETUP.**

Canonical repaired freeze declaration: `c9e43c99d9deb56bad52637024b9dab7b3673aee`.

The current theorem package is:

- T1: on strict `R+`, `h_0<h_M<h_F`;
- T2: on strict `R+`, `mu_M<mu_F`;
- T3: for `mu_M<mu<mu_F`, neither pure architecture is self-consistent and the certified branch has a unique aggregate mixed resolution;
- B1: architecture-insensitive integration collapses the threshold split;
- W1: holding installed masses fixed, `mu_P-mu_W=d h p*(h)>0`.

T1–T3 are quadratic-baseline strict-`R+` results. Arbitrary strict concavity is not a valid general theorem. Common-curvature nonquadratic survival is numerical robustness only. No non-Uniform integration-cost CDF theorem is carried into the repaired freeze. W1 is not a global endogenous-welfare theorem.

The surviving contribution is the reciprocal feedback

`expected architecture -> continuation rent -> sunk integration -> installed high-use state -> relative architecture profitability -> architecture choice`,

which splits one fixed-state threshold into two self-consistency thresholds. Generic hold-up, two-part tariffs, mixed equilibrium, AI/cloud application novelty, and quality/model improvement are not claimed as standalone contributions.

## Canonical freeze records

- `docs/STAGE_08_THEORY_FREEZE.md`
- `docs/freeze_repaired/MODEL_REGISTER.md`
- `docs/freeze_repaired/PROPOSITION_SCOPE_REGISTER.md`
- `docs/freeze_repaired/WELFARE_BENCHMARK_REGISTER.md`
- `docs/freeze_repaired/VERIFICATION_REGISTER.md`
- `docs/freeze_repaired/CONTRIBUTION_REGISTER.md`
- `theorem_certificates/current_scope.md`
- `formal/FORMAL_VERIFICATION_CERTIFICATE_REPAIRED.md`

Formal Verification Gate: **PASS**. The Lean artifact certifies a targeted proof-critical core only, not the complete game/equilibrium correspondence.

The previous freeze based on `2597e82044ec94a58fad033227ea415e64af8c6d` and pre-repair Stage-9/10 artifacts are historical only.

Next authorized action: **rerun/rebase Stage 9 — Reproducibility Setup on the repaired freeze**.

Preferred manuscript title after the downstream reproducibility gate: **Dynamic Tariff Choice for Generative AI: Integration, Commitment, and Welfare**.

Portfolio status SSOT: `ryotamatsuki/economic-theory-research-portfolio#30`.
