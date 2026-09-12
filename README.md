# Dynamic Tariff Choice for Generative AI

Theory project on dynamic tariff architecture, sunk AI-specific integration, and welfare.

## Status

**Stage 7.5 full-paper value gate passed — GO TO STAGE 7.5A GENERALITY / QUANTIFIER RED-TEAM.**

A Stage-11B hostile review found two certification regressions in the previously frozen game definition. Stage 4R repaired the zero-surplus participation convention and global continuation completeness; repeated Stage 4A passed on strengthened strict regular region `R+`. Stage 6 re-killed novelty claims, Stage 7 re-certified welfare/generality/institutional scope, and Stage 7.5 concluded that the repaired mechanism still warrants full-paper investment.

- Stage 4R repair: **PASS**
- Repeated Stage 4A: **GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS**
- Stage 6 re-kill: **GO**
- Repaired Stage 7: **GO**
- Repaired Stage 7.5: **GO TO STAGE 7.5A GENERALITY / QUANTIFIER RED-TEAM**
- Old Stage 8 freeze: **STALE PENDING RENEWED STAGE 7.5A**
- Next stage: **Stage 7.5A — Generality / Quantifier Red-Team and formal-fidelity gate**
- Portfolio status SSOT: `ryotamatsuki/economic-theory-research-portfolio#30`

## Repaired mechanism and surviving novelty

On strict `R+`, every rational-expectations H installed state lies in `[h_0,h_F]`, and both-served flat and metered continuations are strict global active-set optima over that complete candidate interval. Anticipated metering induces `h_M<h_F`, while provider metering gain rises with the installed high-use state, yielding `mu_M<mu_F`. For `mu_M<mu<mu_F`, neither pure architecture is self-consistent and the certified regular branch has a unique aggregate mixed resolution.

The surviving contribution is only the reciprocal feedback

`architecture expectation -> installed high-use state -> profitability of that same architecture -> architecture choice`,

which splits one fixed-state switching threshold into two self-consistency thresholds. Architecture-insensitive integration collapses them back to one. Generic hold-up, commitment, fixed-versus-usage pricing, two-part tariffs, mixed equilibrium, inference cost, and AI/cloud application novelty are not claimed.

## Stage 7.5 full-paper value decision

The project remains a full-paper candidate because the threshold split is an exact theorem on a transparent strict domain, the architecture-insensitive benchmark identifies the source of the effect, the mechanism can be stated without notation, at least one nonquadratic common-curvature formulation preserves the mechanism numerically, and the welfare analysis has real non-transfer content.

The project must nevertheless remain narrow:

- strict `R+` is substantive and must be prominent;
- arbitrary strict concavity does not preserve `h_M<h_F` in general;
- the abstract order implication is only an organizing sufficient-condition lemma;
- the fixed-installed-base welfare wedge is not a global policy theorem;
- institutional evidence motivates the timing and tariff menu but does not establish the causal feedback empirically.

Recommended title after repaired theory is refrozen: **Dynamic Tariff Choice for Generative AI: Integration, Commitment, and Welfare**. The old “Model Improvement” wording is unsupported by the headline theorem.

Journal positioning: **IJIO remains a plausible but demanding first target; JIE is not preferred at the repaired scope.** The main risk is that a referee views the interaction theorem as too narrow relative to the hold-up/commitment literature.

Stage 7.5A receives the repaired Stage-4R/4A records, exact theorem certificates, Stage-6 novelty record, repaired Stage-7 welfare/generality record, Stage-4A and Stage-7 verification scripts, Stage-11B nonquadratic/counterexample evidence, and the existing Lean source as a conditional algebraic artifact pending renewed statement-fidelity certification.

## Current canonical records

- `docs/STAGE_04R_REPAIR.md`
- `docs/STAGE_04A_RECERTIFICATION.md`
- `theorem_certificates/stage4a_repair_certificates.md`
- `verification/stage4a_repair_independent.py`
- `docs/STAGE_06_REKILL_REPAIR_RATIFICATION.md`
- `docs/STAGE_07_REPAIRED_WELFARE_GENERALITY.md`
- `verification/stage7_repaired_verify.py`
- `docs/STAGE_075_REPAIRED_FREEZE_DECISION.md`
- `docs/STAGE_11B_ASTRA_REFEREE_AUDIT.md`

The previous Stage-8 freeze and Stage-10 manuscript remain in the repository as historical artifacts. They must not be treated as current certification until Stage 7.5A passes and a new Stage-8 freeze is issued.

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
