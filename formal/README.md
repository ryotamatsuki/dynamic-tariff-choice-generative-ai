# Formal verification boundary

This directory contains a **targeted proof-critical core**, not a formalization of the complete economic model.

## Current canonical certificate

`formal/FORMAL_VERIFICATION_CERTIFICATE_REPAIRED.md`

Current state: **FORMAL VERIFICATION PASS**.

## Toolchain

- Lean 4: pinned by `lean-toolchain`
- mathlib: pinned in `lakefile.lean`
- build: `lake update && lake exe cache get && lake build DynamicTariffFormal`

## Current claim mapping

| Economic object | Lean theorem(s) | What is certified | What remains outside |
|---|---|---|---|
| T1 repaired ordering | `fixedPoint_above_zeroRentState`, `fixedPoint_below_flat_state`, `fixedPoint_between_states`, `antitone_fixedPoint_unique` | repaired fixed-point order/uniqueness skeleton | derivation of the economic integration map and active-set optimization |
| T2 threshold separation | `threshold_separation`, `baseline_phi_derivative_positive` | state ordering plus increasing gain imply threshold ordering; derivative-expression positivity | derivation of `Phi` from full provider profit |
| T3 strict gap | `strict_gap_reverses_pure_responses`, `mixed_state_unique` | opposite pure responses and conditional mixed-state uniqueness | mixed existence, probability bounds, complete equilibrium correspondence |
| strict `R+` endpoint logic | `endpoint_dominance_propagates` | endpoint dominance propagation under monotonicity | economic derivation of monotonicity and global continuation optimization |
| W1 fixed-base wedge | `private_social_wedge_identity`, `private_social_wedge_positive` | exact algebraic identity and sign | planner interpretation and endogenous welfare |
| outside-`R+` scope guard | `hOnly_scope_counterexample` | exact `23/10` H-only advantage | exhaustive outside-domain characterization |

## Repaired game boundary

The repaired weak-participation rule — zero continuation surplus participates — is not encoded in Lean. It is part of the economic game definition and is certified in the repaired Stage-4R/4A records.

The proof assistant also does not formalize primitive demand derivation, the complete provider continuation problem, the full atomless integration game, alternative-equilibrium enumeration, nonquadratic/non-Uniform generality, or institutional interpretation.

## Statement-fidelity rule

A formal theorem of the form `assumptions -> conclusion` certifies only that implication. It does not establish that the economic primitives imply those assumptions unless that derivation is itself represented.

Accordingly, the formal artifact may be described as targeted verification of repaired proof-critical order/threshold/welfare logic, but not as verification of the complete economic model or equilibrium set.

## Dependency / placeholder policy

The formal source contains no proof placeholders in the certified build. Dependency reports are emitted for each certified theorem. The current build reports only standard mathlib/classical dependencies and no project-specific axiom.
