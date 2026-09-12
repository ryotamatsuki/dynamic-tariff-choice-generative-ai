# Dynamic Tariff Choice for Generative AI

Theory project on dynamic tariff architecture, sunk AI-specific integration, and welfare.

## Status

**Stage 6 Novelty Re-Kill / repair ratification passed.**

A Stage-11B hostile review found two certification regressions in the previously frozen game definition. Stage 4R repaired the zero-surplus participation convention and global continuation completeness; repeated Stage 4A passed on the strengthened strict regular region `R+`.

- Stage 4R repair: **PASS**
- Repeated Stage 4A: **GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS**
- Stage 6 re-kill: **GO — GO TO WELFARE / GENERALITY**
- Old Stage 8 freeze: **STALE PENDING DOWNSTREAM RERUNS**
- Next stage: **Stage 7 — Welfare / Generality / Institutional Validation**
- Portfolio status SSOT: `ryotamatsuki/economic-theory-research-portfolio#30`

## Repaired mechanism and surviving novelty

On strict `R+`, every rational-expectations H installed state lies in `[h_0,h_F]`, and both-served flat and metered continuations are strict global active-set optima over that complete candidate interval. Anticipated metering induces `h_M<h_F`, while provider metering gain rises with the installed high-use state, yielding `mu_M<mu_F`. For `mu_M<mu<mu_F`, neither pure architecture is self-consistent and the certified regular branch has a unique aggregate mixed resolution.

Stage 6 re-killed generic novelty claims. The surviving contribution is only the reciprocal feedback

`architecture expectation -> installed high-use state -> profitability of that same architecture -> architecture choice`,

which splits one fixed-state switching threshold into two self-consistency thresholds. Exogenous or architecture-insensitive integration collapses them back to one. Generic hold-up, commitment, fixed-versus-usage pricing, two-part tariffs, mixed equilibrium, inference cost, and AI/cloud application novelty are not claimed.

The broader order implication remains only an organizing sufficient-condition lemma, not arbitrary-concave-demand generality.

## Current canonical repair / re-kill records

- `docs/STAGE_04R_REPAIR.md`
- `docs/STAGE_04A_RECERTIFICATION.md`
- `theorem_certificates/stage4a_repair_certificates.md`
- `verification/stage4a_repair_independent.py`
- `docs/STAGE_06_REKILL_REPAIR_RATIFICATION.md`
- `docs/STAGE_11B_ASTRA_REFEREE_AUDIT.md`

The previous Stage-8 freeze and Stage-10 manuscript remain in the repository as historical artifacts. They must not be treated as current certification until Stage 7, Stage 7.5, Stage 7.5A and Stage 8 are rerun.

## Reproduce

With Python, Lean/Lake, and LaTeX installed:

```bash
python -m pip install -r requirements-dev.txt
python verification/stage4a_repair_independent.py
lake update
lake exe cache get
make all
```

The existing Lean artifact remains useful for its conditional algebraic core, but the prior economic statement-fidelity certificate is stale until the repaired model passes the downstream formal-verification gate again.

## Repository layout

- `paper/`, `sections/` — historical Stage-10 modular manuscript pending downstream reauthorization
- `figures/`, `tables/` — deterministically generated manuscript inputs
- `scripts/` — artifact generation and integrity gates
- `tests/` — permanent regression tests
- `verification/` — symbolic/numerical certification checks, including the independent Stage-4A repair audit
- `formal/` — Lean proof-critical core and prior formal certificate
- `theorem_certificates/` — theorem/scope certificates
- `references/` — source-checked bibliography database
- `docs/freeze/` — superseded Stage-8 registers retained for provenance
- `.github/workflows/` — theory/formal and reproducibility CI

## Change discipline

The repair is a substantive post-freeze strategy-domain / continuation-completeness change and follows `docs/CHANGE_CONTROL.md`. A new Stage-8 freeze is required before downstream manuscript work resumes.
