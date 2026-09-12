# Theory Change Control

Current theory freeze: repaired Stage 8 declaration commit `c9e43c99d9deb56bad52637024b9dab7b3673aee`.

Canonical current records are `docs/STAGE_08_THEORY_FREEZE.md`, `docs/freeze_repaired/`, `theorem_certificates/current_scope.md`, and `formal/FORMAL_VERIFICATION_CERTIFICATE_REPAIRED.md`.

The earlier freeze based on `2597e82044ec94a58fad033227ea415e64af8c6d`, the old `docs/freeze/` records, old formal certificate, and pre-repair Stage-9/10 certification are historical only.

Any substantive change must record what changed, why, affected equations/propositions/quantifiers, continuation or active-set effects, welfare benchmarks, verification, formal theorem statements, contribution wording, and stages to rerun.

Rollback rules:

- equilibrium, participation, strategy-domain, continuation/globality, or active-set change -> Stage 4/4A;
- welfare accounting or planner benchmark change -> Stage 7 and any earlier affected stage;
- generality, theorem quantifier, uniqueness, selection, or benchmark wording change -> Stage 7.5A;
- material change to a formally certified theorem or encoded hypothesis -> formal certificate stale and fresh Stage-7.5A Formal Verification Gate required;
- new mechanism, player, state, tariff instrument, or extension -> earliest affected scientific stage.

After substantive rollback, rerun all affected downstream gates and Stage 8. No silent theory drift is permitted.

Pure notation cleanup, typo repair, citation maintenance, CI/path maintenance, and prose edits within frozen maximum-defensible wording do not reopen theory.

Stage-11B certification-regression provenance remains recorded in `docs/STAGE_04R_REPAIR.md` and `docs/STAGE_04A_RECERTIFICATION.md`. The repaired model specifies weak future participation at zero surplus, global provider continuation play, and strict `R+` over the complete candidate interval `[h_0,h_F]`.

Stage 9 has now been rerun/rebased on the repaired freeze. Stage 10 may proceed only under `docs/STAGE_09_REPRODUCIBILITY_SETUP.md`; pre-repair manuscript wording is not automatically re-certified.
