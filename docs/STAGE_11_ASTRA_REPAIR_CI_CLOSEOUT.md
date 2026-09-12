# Stage 11 Astra repair — CI closeout evidence

Date: 2026-09-13 (JST)

This record is additive to `docs/STAGE_11_ASTRA_REPAIR_RECHECK.md` and records the execution evidence for the repair branch. It does not change the fail-closed Stage-11 routing caused by the unresolved published-Hagiu source comparison.

## Repair identity

- audit target / repair base: `b85f386f458ed394d0df9b0f2af5b1de02c27d59`
- repair branch: `repair/stage11-astra-reservations`
- substantive tested repair head: `a86e67be4ac27c7380d35efbf19bf4ce95b55046`
- pull request: `dynamic-tariff-choice-generative-ai#2`

## Successful closeout runs on the substantive tested head

### Verify

PR verify run `34711647194`: **SUCCESS**.

The same repaired verifier suite had already passed on the immediately preceding substantive head `53e30a7afc0974783a4eaa54dbec64686cae968f` in push verify run `34711481279`, including:

- baseline symbolic checks;
- robustness checks;
- repaired Stage-4A independent audit;
- repaired Stage-7 welfare checks;
- historical repaired Stage-11 independent referee checks;
- new Astra Stage-11 repair checks;
- Stage-10 manuscript scope gate;
- Lean build and placeholder audit.

The final `a86e67...` change only escaped underscores in a prose-only repository path in the Related Literature section; PR verify run `34711647194` then revalidated the full verify workflow on that exact head.

### Reproducibility

Push reproducibility run `34711644954`: **SUCCESS** on `a86e67be4ac27c7380d35efbf19bf4ce95b55046`.

It passed:

- frozen-theory regression and integrity gates;
- deterministic figure/table generation;
- LaTeX toolchain installation;
- manuscript PDF build;
- artifact upload.

## Failures encountered and repaired during the recheck

Failures were not treated as evidence of a pass.

1. The first new Astra repair verifier run failed because a manuscript guard required the literal phrase `average marginal price` while the repaired manuscript said `average price`. The mathematical checks had passed; the guard was corrected to test the actual semantic prohibition. The subsequent Astra repair check passed in CI.
2. Reproducibility run `34711481266` failed at manuscript build because the Related Literature section printed a repository path containing unescaped underscores. The path was converted to escaped `\texttt{...}` form. Reproducibility run `34711644954` then passed on the repaired head.

No NaN, solver nonconvergence, missing branch, or CI failure was reclassified as a successful deviation test.

## Formal-verification scope

The existing Lean target was rerun only as a regression check. No new Lean theorem was added for the Astra repair. The new active-set globality, candidate-interval completeness, pure-boundary characterization, and explicit mixed-strategy construction are supported by analytic manuscript proofs plus the additive Python/SymPy verifier; they are **not** newly described as Lean-certified.

## Gate implication

The code/manuscript/reproducibility part of the Astra reservation repair is green on `a86e67be4ac27c7380d35efbf19bf4ce95b55046`.

Nevertheless, the canonical gate remains:

**REPAIR WITHIN STAGE 11 — STAGE 12 PAUSED.**

Reason: the complete published RAND version of Hagiu (2006), *Pricing and Commitment by Two-Sided Platforms*, was not accessible in the current environment. Under the explicit fail-closed instruction, green CI does not override that unresolved source comparison. If the published full text later establishes whole-game absorption of the specific reciprocal architecture-state-profitability loop and two-threshold/interior-mixing result, roll back to Stage 6; otherwise Stage 11 may be re-ratified and Stage 12 authorized.
