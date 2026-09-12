# Repaired Formal Verification Certificate

Date: 2026-09-12 (JST)

## State

**FORMAL VERIFICATION PASS**

This certificate supersedes the pre-repair economic statement-fidelity certificate. It covers the repaired Stage-4R/4A theorem package and repaired Stage-7 welfare identity. It certifies only a proof-critical logical/algebraic core, not the complete economic model or equilibrium correspondence.

## Build provenance

- verified commit: `d6ac2a4bca0bf10dbfea23b274951d15b39d8551`
- workflow run: `34678945920`
- Lean job: `103513808791`
- Python/scope job: `103513808897`
- Lean: `4.33.1`
- Lean toolchain commit: `819816b2e0a3bf405af45ae5c7af2491d8f5bee6`
- mathlib release: `v4.33.1`
- mathlib revision: `0df444a360eaa60ab8c11dca51a86af692955474`
- formal source: `formal/DynamicTariffFormal.lean`
- build command: `lake build DynamicTariffFormal`
- build result: SUCCESS (`Built DynamicTariffFormal`; 8707 jobs)
- proof-placeholder audit: PASS
- Stage-7.5A symbolic scope audit: PASS via `verification/stage075a_scope_verify.py`

## Target map

| Economic object | Lean theorem(s) | Certified component | Explicitly outside formal coverage |
|---|---|---|---|
| T1 repaired ordering `h_0<h_M<h_F` | `fixedPoint_above_zeroRentState`, `fixedPoint_below_flat_state`, `fixedPoint_between_states`, `antitone_fixedPoint_unique` | order and at-most-one-fixed-point skeleton under stated map conditions | economic derivation of the integration map, existence/interiority from primitives, active-set optimization |
| T2 `mu_M<mu_F` | `threshold_separation`, `baseline_phi_derivative_positive` | ordered states plus increasing gain imply ordered thresholds; positivity of the recorded derivative expression | derivation of `Phi` from the complete provider continuation problem |
| T3 strict pure-regime gap | `strict_gap_reverses_pure_responses`, `mixed_state_unique` | opposite pure responses inside the strict gap; conditional uniqueness of the mixed state | mixed-equilibrium existence, probability bounds, complete equilibrium set |
| `R+` endpoint logic | `endpoint_dominance_propagates` | endpoint dominance propagates over an interval when the rival-minus-preferred difference is monotone | derivation of monotonicity from economic profits; full continuation optimization |
| W1 fixed-base welfare wedge | `private_social_wedge_identity`, `private_social_wedge_positive` | exact identity `mu_P-mu_W=d h p*(h)` and positivity under strict signs | planner interpretation and endogenous-welfare ranking |
| permanent scope guard | `hOnly_scope_counterexample` | exact outside-domain H-only advantage `23/10` | exhaustive characterization outside `R+` |

## Repaired participation and model boundary

The repaired game specifies weak future participation: zero continuation surplus participates. This is an economic strategy-domain primitive and is not encoded in Lean. Its role in implementing the binding low-type participation constraint is certified by Stage 4R/4A, not by this formal artifact.

Also outside the formal model are primitive demand derivation, global provider continuation optimization, the complete atomless integration game, alternative-equilibrium enumeration, mixed-equilibrium existence, nonquadratic/non-Uniform generality, and institutional interpretation.

## Axiom/dependency audit

The build prints dependencies for every formal theorem. All certified theorems report only the standard dependencies `propext`, `Classical.choice`, and `Quot.sound`. No project-specific axiom is introduced.

The source-level placeholder check passed in CI.

## Statement-fidelity conclusions

The formal theorems are implications from explicit hypotheses. They do not certify those economic hypotheses unless the derivation is separately formalized. In particular:

- `threshold_separation` is an organizing sufficient-condition theorem, not a theorem for arbitrary concave demand;
- `fixedPoint_between_states` certifies the repaired order skeleton, not the full primitive proof of T1;
- `endpoint_dominance_propagates` certifies interval logic, while the actual quadratic derivative identities are checked independently in `verification/stage075a_scope_verify.py`;
- W1 is a fixed-installed-base identity only.

Maximum defensible wording:

> A targeted Lean 4 formalization certifies the repaired proof-critical order, threshold, endpoint-propagation, mixed-state-uniqueness, welfare-identity, and exact-counterexample logic.

It must not be described as a formal verification of the complete economic game or global equilibrium correspondence.

## Reproducibility and rollback

`lean-toolchain` pins Lean `v4.33.1`; `lakefile.lean` pins mathlib `v4.33.1`. The successful CI run rebuilt from a fresh checkout and passed both the formal build and source-level placeholder audit.

Any material change to T1–T3/B1 quantifiers, strict `R+`, the participation convention, provider architecture decision rule, or welfare benchmark definitions makes this certificate stale.

**Final state: FORMAL VERIFICATION PASS.**
