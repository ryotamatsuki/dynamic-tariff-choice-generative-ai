# Stage 8 — Verification / Continuation Register

## Gate status

- Stage 4R symbolic derivation/regression: PASS.
- Stage 4A independent mathematical adversarial certification: PASS on `R`.
- Stage 6R novelty re-ratification: GO.
- Stage 7 welfare/benchmark audit: GO.
- Stage 7.5 full-paper value gate: GO.
- Stage 7.5A generality/quantifier certification: GO.
- Formal Verification Gate: **FORMAL VERIFICATION PASS**.

## Stage-4A theorem certificates

- T1 `0<h_M<h_F`: PASS, branch-specific.
- T2 `mu_M<mu_F`: PASS conditional on `R`.
- T3 no-pure gap and unique mixed regular-branch resolution: PASS for strict interior `R`.
- Global-all-parameters formulation: intentionally rejected.

Independent direct-payoff evaluator includes both-served and H-only continuations instead of assuming the desired active set.

## Continuation / active-set status

Economically relevant continuation active sets are both served, H-only, and no service. Under an anonymous common tariff, a tariff serving L cannot exclude higher-value H.

T1–T3 use both-served formulas only on `R`, where Stage 4A certified global continuation optimality over the relevant on-path interval.

Individual atomless deviations do not move aggregate installed masses. No material on-path continuation for T1–T3 is unresolved.

Unresolved on-path continuations used as evidence: **0**.
Numerical failures treated as unprofitable deviations: **0**.
Invalid active sets treated as equilibrium evidence: **0**.

## Formal-verification certificate

Canonical certificate: `formal/FORMAL_VERIFICATION_CERTIFICATE.md`.

Pinned provenance:

- Lean 4.33.1;
- mathlib v4.33.1;
- resolved mathlib revision `0df444a360eaa60ab8c11dca51a86af692955474`;
- successful workflow run `34660791188`;
- explicit build `lake build DynamicTariffFormal`;
- no-`sorry`/`admit` audit PASS.

`#print axioms` reports only `propext`, `Classical.choice`, `Quot.sound`; no project-specific axiom.

Formal coverage class: **PROOF-CRITICAL CORE**, not the full economic model.

Formal theorem map:

- `threshold_separation` — state ordering + strict monotonicity -> threshold ordering;
- `strict_gap_reverses_pure_responses` — strict gap -> opposite pure ex-post responses;
- `antitone_fixedPoint_unique` — at most one fixed point;
- `fixedPoint_below_flat_state` — state ordering under antitone/crossing conditions;
- `mixed_state_unique` — uniqueness skeleton for mixed installed state;
- `baseline_phi_derivative_positive` — exact positivity skeleton;
- `hOnly_scope_counterexample` — exact outside-`R` counterexample.

Not fully formalized: primitive utility/demand derivation, global tariff optimization across every active set, complete atomless game/SPNE correspondence, welfare derivation, institutional interpretation.

## Permanent regression tests

Exact regular example:

`a_L=4, a_H=5, c=1, b_L=16/5, K_L=4, b_H=1/2, K_H=8, mu=13/10`.

It has `l=4/5`, `h_F=5/8`, `h_M=(sqrt(2849)-17)/80`, and `mu_M<13/10<mu_F`; both-served continuations dominate H-only over the relevant interval.

Permanent scope counterexample:

`a_L=4, a_H=5, c=1, l=0.1, h=0.6`.

H-only flat pricing exceeds both-served flat profit by exactly `23/10`. Therefore any global-all-positive-parameters version is false.
