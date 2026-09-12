# Theory Change Control

This project is theory-frozen at Stage 8. No substantive change may be made silently.

## Frozen object

The frozen theory is `docs/STAGE_08_THEORY_FREEZE.md` plus its linked registers, `theorem_certificates/current_scope.md`, and `formal/FORMAL_VERIFICATION_CERTIFICATE.md`.

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
