# Dynamic Tariff Choice for Generative AI

Theory project on dynamic tariff architecture, sunk AI-specific integration, and welfare.

## Status

**Stage 10 — FULL DRAFT READY FOR REFEREE GATE.**

The repaired Stage-8 freeze remains canonical and Stage 9 is **REPRODUCIBILITY BASELINE READY**. Canonical freeze declaration: `c9e43c99d9deb56bad52637024b9dab7b3673aee`.

Active manuscript title: **Dynamic Tariff Choice for Generative AI: Integration, Commitment, and Welfare**.

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
- `docs/STAGE_10_PAPER_BUILD_REPAIRED.md`
- `docs/STAGE_10_FIGURE_TABLE_ARCHITECTURE.md`
- `docs/freeze_repaired/`
- `theorem_certificates/current_scope.md`
- `formal/FORMAL_VERIFICATION_CERTIFICATE_REPAIRED.md`

Build entry point: `make all`. CI entry points: `.github/workflows/verify.yml` and `.github/workflows/reproducibility.yml`. Stage 10 also enforces `scripts/check_stage10_manuscript.py`.

The original pre-repair manuscript certification is historical. The active manuscript now reflects weak participation at zero surplus, global continuation play, strict `R+`, the complete candidate interval `[h_0,h_F]`, and the permanent `23/10` outside-domain scope guard.

Next authorized action: **Stage 11 — Robustness / Referee Attack Gate**.

Portfolio status SSOT: `ryotamatsuki/economic-theory-research-portfolio#30`.
