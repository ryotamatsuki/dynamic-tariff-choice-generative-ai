# Dynamic Tariff Choice for Generative AI

Theory project on dynamic tariff architecture, sunk AI-specific integration, and welfare.

## Status

**Repaired Stage 7 completed — GO TO STAGE 7.5.**

A Stage-11B hostile review found two certification regressions in the previously frozen game definition. Stage 4R repaired the zero-surplus participation convention and global continuation completeness; repeated Stage 4A passed on strengthened strict regular region `R+`. Stage 6 then re-killed novelty claims and Stage 7 re-certified welfare, generality scope, equilibrium-selection scope, and institutional interpretation.

- Stage 4R repair: **PASS**
- Repeated Stage 4A: **GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS**
- Stage 6 re-kill: **GO — GO TO WELFARE / GENERALITY**
- Repaired Stage 7: **GO TO STAGE 7.5**
- Old Stage 8 freeze: **STALE PENDING DOWNSTREAM RERUNS**
- Next stage: **Stage 7.5 — Full-paper value / freeze decision**
- Portfolio status SSOT: `ryotamatsuki/economic-theory-research-portfolio#30`

## Repaired mechanism and surviving novelty

On strict `R+`, every rational-expectations H installed state lies in `[h_0,h_F]`, and both-served flat and metered continuations are strict global active-set optima over that complete candidate interval. Anticipated metering induces `h_M<h_F`, while provider metering gain rises with the installed high-use state, yielding `mu_M<mu_F`. For `mu_M<mu<mu_F`, neither pure architecture is self-consistent and the certified regular branch has a unique aggregate mixed resolution.

The surviving contribution is only the reciprocal feedback

`architecture expectation -> installed high-use state -> profitability of that same architecture -> architecture choice`,

which splits one fixed-state switching threshold into two self-consistency thresholds. Architecture-insensitive integration collapses them back to one. Generic hold-up, commitment, fixed-versus-usage pricing, two-part tariffs, mixed equilibrium, inference cost, and AI/cloud application novelty are not claimed.

## Repaired Stage 7 welfare scope

At a fixed installed base on the certified both-served branch,

`mu_P-mu_W=d h p*(h)>0`.

This is a fixed-allocation welfare wedge, not a global endogenous-welfare theorem. The restricted architecture-commitment welfare ranking is sign-indeterminate even among examples satisfying strict `R+`.

Generality remains narrow. A Stage-11B strictly concave counterexample reverses `h_M<h_F`, so arbitrary-concave-demand generality is prohibited. The broader order implication remains only an organizing sufficient-condition lemma.

## Current canonical repair / downstream records

- `docs/STAGE_04R_REPAIR.md`
- `docs/STAGE_04A_RECERTIFICATION.md`
- `theorem_certificates/stage4a_repair_certificates.md`
- `verification/stage4a_repair_independent.py`
- `docs/STAGE_06_REKILL_REPAIR_RATIFICATION.md`
- `docs/STAGE_07_REPAIRED_WELFARE_GENERALITY.md`
- `verification/stage7_repaired_verify.py`
- `docs/STAGE_11B_ASTRA_REFEREE_AUDIT.md`

The standard verification workflow and local `make verify` path include the repaired Stage-7 welfare checks.

The previous Stage-8 freeze and Stage-10 manuscript remain in the repository as historical artifacts. They must not be treated as current certification until Stage 7.5, Stage 7.5A and Stage 8 are rerun.

## Reproduce

With Python and Lean/Lake installed:

```bash
python -m pip install -r requirements-dev.txt
make verify
```

The existing Lean artifact remains useful for its conditional algebraic core, but the prior economic statement-fidelity certificate is stale until the repaired model passes Stage 7.5A again.

## Repository layout

- `paper/`, `sections/` — historical Stage-10 modular manuscript pending downstream reauthorization
- `figures/`, `tables/` — historical/deterministically generated manuscript inputs
- `scripts/` — artifact generation and integrity gates
- `tests/` — permanent regression tests
- `verification/` — symbolic/numerical certification checks and hostile independent audits
- `formal/` — Lean proof-critical core and prior formal certificate
- `theorem_certificates/` — theorem/scope certificates
- `references/` — source-checked bibliography database
- `docs/freeze/` — superseded Stage-8 registers retained for provenance
- `.github/workflows/` — theory/formal and reproducibility CI

## Change discipline

The repair is a substantive post-freeze strategy-domain / continuation-completeness change and follows `docs/CHANGE_CONTROL.md`. A new Stage-8 freeze is required before manuscript/referee work resumes.
