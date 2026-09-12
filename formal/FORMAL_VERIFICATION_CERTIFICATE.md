# Formal Verification Certificate

## Final pre-freeze state

**FORMAL VERIFICATION PASS**

This certificate closes the Stage-7.5A Formal Verification Gate for the current scope-certified theorem set. It certifies a proof-critical logical/algebraic core, not the complete economic model or global equilibrium correspondence.

## Toolchain and build provenance

- Repository: `ryotamatsuki/dynamic-tariff-choice-generative-ai`
- Verified commit: `c4a158fe78cbe3dbc6d242c3bdcad169494f22d0`
- GitHub Actions workflow: `.github/workflows/verify.yml`
- Successful workflow run: `34660791188`
- Lean: `4.33.1`
- Lean toolchain commit reported by CI: `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`
- mathlib release: `v4.33.1`
- mathlib revision resolved by Lake: `0df444a360eaa60ab8c11dca51a86af692955474`
- Formal source: `formal/DynamicTariffFormal.lean`
- Build command: `lake build DynamicTariffFormal`
- Build result: **SUCCESS** (`Built DynamicTariffFormal`; full workflow green)
- Python verification jobs in the same workflow: **SUCCESS**

## Placeholder / axiom audit

The CI placeholder audit searched `formal/*.lean` for `sorry` or `admit` and passed.

`#print axioms` output for all certified Lean theorems reports only:

- `propext`
- `Classical.choice`
- `Quot.sound`

No project-specific axiom is introduced. No definition encodes the desired economic conclusion as an axiom or opaque assumption object.

## Paper-claim to formal-theorem map

| Economic claim/component | Lean theorem | Formally certified component | Explicitly not certified |
|---|---|---|---|
| Threshold separation | `threshold_separation` | `h_M<h_F` plus `StrictMono Psi` implies `Psi h_M < Psi h_F` | derivation of `h_M<h_F` from every economic primitive; global active-set validity |
| Pure-regime gap response logic | `strict_gap_reverses_pure_responses` | activation cost strictly between the two gross gains implies opposite strict ex-post architecture responses | complete continuum-game/SPNE definition and existence of the relevant states |
| Integration fixed-point uniqueness skeleton | `antitone_fixedPoint_unique` | an antitone real map has at most one fixed point | proof that every admissible CDF/rent specification yields an antitone map |
| State-order skeleton | `fixedPoint_below_flat_state` | fixed point lies below the flat state under antitone/crossing conditions | existence/interiority and economic derivation of crossing |
| Mixed-state uniqueness skeleton | `mixed_state_unique` | strictly decreasing state response plus increasing gain gives at most one state solving provider indifference | mixed-equilibrium existence, probability bounds, off-branch active sets |
| Baseline gain monotonicity algebra | `baseline_phi_derivative_positive` | positivity of the exact Stage-4R derivative expression under sign assumptions | differentiation of the provider objective itself; continuation optimality |
| Scope counterexample | `hOnly_scope_counterexample` | exact H-only flat profit advantage `23/10` at the retained out-of-R composition | exhaustiveness of all outside-R failures |

## Statement fidelity

The Lean theorems intentionally encode implications from scope-certified assumptions. They do **not** establish that every assumption follows from arbitrary concave demand, arbitrary heterogeneity, or every feasible active set.

Therefore the maximum formal-verification wording is:

> A targeted Lean 4 formalization certifies the proof-critical order, threshold, fixed-point-uniqueness, and exact counterexample logic used by the scope-certified theorem package.

Prohibited wording:

> Lean formally verifies the complete economic model or the global equilibrium correspondence.

## Model boundary

Not fully formalized:

- primitive utility maximization and demand derivation;
- provider global continuation optimization over every tariff/active set;
- the complete atomless integration game;
- Stage-4A off-branch global-deviation enumeration;
- welfare accounting from primitives;
- empirical/institutional interpretation.

These remain covered by the analytic Stage-4R/4A/7 evidence and regression tests, not by the proof assistant.

## Rollback rule

Any material change to T1–T3 assumptions, theorem quantifiers, the definition of the regular region, provider architecture decision rule, or the formalized sufficient-condition theorem makes this certificate stale and requires a new build plus statement-fidelity audit before refreeze.

## Gate decision

The applicable proof-critical targets build successfully, statement fidelity is explicit, no unexplained placeholder/project-specific axiom remains, and reproducible toolchain/build evidence exists.

**Final state: FORMAL VERIFICATION PASS.**
