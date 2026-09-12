# Formal verification boundary

This directory contains a **proof-critical core**, not a formalization of the complete economic model.

## Toolchain

- Lean 4: pinned by `lean-toolchain`
- mathlib: pinned in `lakefile.lean`
- Build: `lake update && lake exe cache get && lake build`

## Claim mapping

| Paper claim | Lean theorem | What is certified | What remains outside the formal model |
|---|---|---|---|
| T2 threshold separation | `threshold_separation` | strict state ordering + strictly increasing gain imply ordered thresholds | derivation of `h_M<h_F` and construction of provider payoff from primitives |
| T3 strict gap | `strict_gap_reverses_pure_responses` | costs between the two gains imply opposite ex-post pure responses | complete continuum-game equilibrium definition and active-set economics |
| General-CDF uniqueness skeleton | `antitone_fixedPoint_unique` | antitone map has at most one fixed point | proof that a particular CDF/rent system generates that antitone map |
| General-CDF state order skeleton | `fixedPoint_below_flat_state` | fixed point lies below flat state under antitone/crossing conditions | economic derivation of those conditions |
| Mixed resolution uniqueness skeleton | `mixed_state_unique` | strictly decreasing installed state plus increasing gain gives at most one mixed state | existence, probability bounds, and full strategy-space characterization |
| Baseline monotonicity algebra | `baseline_phi_derivative_positive` | positivity of the exact derivative expression under sign assumptions | derivation of that derivative from provider profit |
| Out-of-R scope guard | `hOnly_scope_counterexample` | exact arithmetic H-only profit advantage in the retained counterexample | claim that this exhausts all possible outside-R failures |

## Statement-fidelity rule

A theorem of the form `assumptions -> conclusion` certifies only the implication. In particular, Lean does not by itself certify that the model's economic primitives imply the assumptions unless that derivation is also encoded.

The manuscript must therefore describe this artifact as targeted formal verification of threshold/order/case logic, not as formal verification of the complete economic model or equilibrium correspondence.

## Placeholder / axiom policy

Certified source must contain no `sorry`, `admit`, or project-specific axioms. The source prints axiom dependencies for each headline formal theorem. Standard mathlib/classical dependencies are not project-specific economic assumptions.
