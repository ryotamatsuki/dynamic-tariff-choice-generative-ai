# Dynamic Tariff Choice for Generative AI

Theory project on dynamic tariff architecture, sunk AI-specific integration, and welfare.

## Status

**Stage 9 — REPRODUCIBILITY BASELINE READY.**

The repaired Stage-8 freeze is canonical and the repository/build baseline has been rebased on it. Canonical freeze declaration: `c9e43c99d9deb56bad52637024b9dab7b3673aee`.

Current theorem package:

- T1: on strict `R+`, `h_0<h_M<h_F`;
- T2: on strict `R+`, `mu_M<mu_F`;
- T3: for `mu_M<mu<mu_F`, neither pure architecture is self-consistent and the certified branch has a unique aggregate mixed resolution;
- B1: architecture-insensitive integration collapses the threshold split;
- W1: holding installed masses fixed, `mu_P-mu_W=d h p*(h)>0`.

T1–T3 are quadratic-baseline strict-`R+` results. Arbitrary strict concavity is not a valid general theorem. Common-curvature nonquadratic survival is numerical robustness only. No non-Uniform integration-cost CDF theorem is carried into the repaired freeze. W1 is not a global endogenous-welfare theorem.

The surviving contribution is the reciprocal feedback

`expected architecture -> continuation rent -> sunk integration -> installed high-use state -> relative architecture profitability -> architecture choice`,

which splits one fixed-state threshold into two self-consistency thresholds.

## Canonical records

- `docs/STAGE_08_THEORY_FREEZE.md`
- `docs/STAGE_09_REPRODUCIBILITY_SETUP.md`
- `docs/REPRODUCIBILITY_REPAIRED.md`
- `docs/freeze_repaired/`
- `theorem_certificates/current_scope.md`
- `formal/FORMAL_VERIFICATION_CERTIFICATE_REPAIRED.md`

Build entry point: `make all`. CI entry points: `.github/workflows/verify.yml` and `.github/workflows/reproducibility.yml`.

The pre-repair Stage-9/10 certification is historical. Existing manuscript prose is only a starting scaffold until repaired Stage 10 rewrites and re-certifies the exposition.

Next authorized action: **Stage 10 — Paper Build / Repair**.

Preferred manuscript title: **Dynamic Tariff Choice for Generative AI: Integration, Commitment, and Welfare**.

Portfolio status SSOT: `ryotamatsuki/economic-theory-research-portfolio#30`.
