# Stage 8 — Canonical Theory Freeze

Freeze date: 2026-09-12 (JST)
Workflow: `ryotamatsuki/research-paper-workflow` v2.1
Project: **Dynamic Tariff Choice for Generative AI: Model Improvement, Commitment, and Welfare**

## Verdict

**THEORY FROZEN — GO TO REPRODUCIBILITY SETUP.**

Entry gates are closed: Stage 4A `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`; Stage 7.5A `GO — GENERALITY / QUANTIFIER CERTIFICATION PASS`; Formal Verification Gate `FORMAL VERIFICATION PASS`.

## Frozen research question

When enterprise users make sunk AI-specific integration decisions before a provider can revise its future tariff architecture, how does the anticipated architecture change the installed base on which the provider later evaluates that same architecture, and what does this imply for tariff switching, equilibrium, and welfare?

## Frozen contribution

Anticipated metering reduces heavy-use integration relative to anticipated flat pricing, while a larger installed heavy-use state raises the provider's gain from metering. This endogenous-state feedback splits one static tariff-switching threshold into two self-consistency thresholds. For activation costs strictly between them, neither pure architecture is self-consistent. If integration is exogenous or architecture-insensitive, the thresholds collapse to one.

The paper does not claim novelty for generic hold-up, two-part tariffs, subscription-versus-usage choice, mixed strategies, or generic private/social pricing wedges.

## Canonical registers

- Model, timing, strategy sets, primitives, parameter restrictions and equilibrium concept: `docs/freeze/MODEL_REGISTER.md`
- Propositions, quantifiers, robustness and prohibited stronger claims: `docs/freeze/PROPOSITION_SCOPE_REGISTER.md`
- Welfare and benchmark definitions: `docs/freeze/WELFARE_BENCHMARK_REGISTER.md`
- Stage-4A, Stage-7.5A, formal proof, continuation, solver and counterexample evidence: `docs/freeze/VERIFICATION_REGISTER.md`
- Closest-paper distinction, institutional interpretation and explicit exclusions: `docs/freeze/CONTRIBUTION_REGISTER.md`
- Post-freeze rollback rules: `docs/CHANGE_CONTROL.md`

## Freeze identity

Pre-freeze certified repository head: `8e18cbcd52cba8b98990bcb6a4c62c1258ecc7f0`.

Formal proof-critical build source recorded in the formal certificate: `c4a158fe78cbe3dbc6d242c3bdcad169494f22d0`.

The commit adding this Stage-8 record and its linked registers is the canonical administrative freeze point. No substantive theory change is authorized after this point without change control and refreeze.

## Final routing

Stage 9 — Reproducibility Setup is authorized. Manuscript construction remains downstream of the reproducibility gate.
