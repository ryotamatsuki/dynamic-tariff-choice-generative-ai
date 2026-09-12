# Theory Change Control

This project was theory-frozen at Stage 8. No substantive change may be made silently.

## Frozen object

The prior frozen theory is `docs/STAGE_08_THEORY_FREEZE.md` plus its linked registers, `theorem_certificates/current_scope.md`, and `formal/FORMAL_VERIFICATION_CERTIFICATE.md`.

Following the 2026-09-12 Stage-11B certification regression, that frozen object is retained for provenance but is **stale for current routing purposes** until the downstream gates are rerun and a new Stage-8 freeze is issued.

## Required record for any substantive change

Record: what changes; why; affected equations/definitions; affected propositions/quantifiers; affected active sets/continuations; affected welfare benchmarks; affected verification; affected Lean statements or supplied hypotheses; affected contribution/literature wording; and stages to rerun.

## Mandatory rollback routing

- Equilibrium correctness, strategy domain, continuation/globality or active-set changes: reopen Stage 4 and Stage 4A.
- Welfare accounting or planner/benchmark changes: reopen Stage 7 and earlier stages if underlying mathematics changes.
- Generality, theorem quantifiers, uniqueness, selection or benchmark wording changes: reopen Stage 7.5A.
- Any material change to a formally certified theorem, encoded hypothesis or proof-critical identity makes the current formal certificate stale and requires a new Stage-7.5A Formal Verification Gate.
- Any new mechanism, player, state, tariff instrument or extension returns to the earliest affected scientific stage.

After substantive rollback, Stage 8 must be rerun before downstream manuscript work continues.

Pure notation cleanup, typo repair, path/CI maintenance that does not change a theorem statement, and prose edits within the frozen maximum-defensible wording do not reopen theory stages.

## 2026-09-12 certification-regression event

### Trigger

Independent Stage-11B hostile review (`docs/STAGE_11B_ASTRA_REFEREE_AUDIT.md`) found two defects that the original Stage-4A gate should have caught:

1. future participation at exactly zero continuation surplus was not explicitly defined even though the provider sets the L participation constraint exactly binding;
2. the provider's global continuation best-response correspondence was not explicitly certified at every installed-state history.

### Earliest affected stage

Stage 4 / Stage 4A.

### Authorized repair

`docs/STAGE_04R_REPAIR.md` makes the smallest bounded repair:

- future participation uses weak IR and participation at zero surplus;
- integration at the exact cutoff is also specified (measure-zero under the baseline continuous distribution);
- provider continuation play is globally defined by both-served / H-only / no-service active-set maximization;
- the regular theorem domain is strengthened to `R+`, requiring strict both-served dominance over the complete rational-expectations candidate interval `[h_0,h_F]`.

No player, state, tariff instrument, utility primitive, cost primitive, or headline mechanism is added.

### Re-certification result

Repeated Stage 4A (`docs/STAGE_04A_RECERTIFICATION.md`) returns:

**GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS.**

Independent permanent artifact: `verification/stage4a_repair_independent.py`.

### Downstream regression obligations

Before manuscript/referee work resumes, rerun in canonical order:

Stage 6 → Stage 7 → Stage 7.5 → Stage 7.5A (including formal statement-fidelity) → Stage 8 refreeze.

The prior Stage-8 freeze, prior `current_scope` certificate, and prior Stage-10 manuscript are historical artifacts only until that sequence is complete.
