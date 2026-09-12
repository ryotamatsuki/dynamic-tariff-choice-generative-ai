# Dynamic Tariff Choice for Generative AI

Theory project on dynamic tariff architecture, sunk AI-specific integration, and welfare.

## Status

**Stage 4R repair completed; repeated Stage 4A passed.**

A Stage-11B hostile review found two certification regressions in the previously frozen game definition: zero-surplus future participation was not explicitly specified, and provider continuation play was not globally certified at all installed-state histories. The repair now makes zero-surplus participation an explicit weak-IR primitive and defines the provider's global continuation best-response correspondence by active-set maximization.

- Stage 4R repair: **PASS**
- Repeated Stage 4A: **GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS**
- Old Stage 8 freeze: **STALE PENDING DOWNSTREAM RERUNS**
- Next stage: **Stage 6 — Novelty Re-Kill / repair ratification**
- Portfolio status SSOT: `ryotamatsuki/economic-theory-research-portfolio#30`

## Repaired mechanism and scope

The core mechanism survives the repair. On the strengthened strict regular region `R+`, every rational-expectations H installed state lies in `[h_0,h_F]`, and both-served flat and metered continuations are strict global active-set optima over that complete interval. Anticipated metering then induces `h_M<h_F`, while provider metering gain rises with the installed high-use state, yielding `mu_M<mu_F`. For `mu_M<mu<mu_F`, neither pure architecture is self-consistent and the certified regular branch has a unique aggregate mixed resolution.

The broader order implication remains only a sufficient-condition lemma, not arbitrary-concave-demand generality.

## Current canonical repair records

- `docs/STAGE_04R_REPAIR.md`
- `docs/STAGE_04A_RECERTIFICATION.md`
- `theorem_certificates/stage4a_repair_certificates.md`
- `verification/stage4a_repair_independent.py`
- `docs/STAGE_11B_ASTRA_REFEREE_AUDIT.md`

The previous Stage-8 freeze and Stage-10 manuscript remain in the repository as historical artifacts. They must not be treated as current certification until Stage 6, Stage 7, Stage 7.5, Stage 7.5A and Stage 8 are rerun.

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
