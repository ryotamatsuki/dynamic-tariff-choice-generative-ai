# Repaired Stage 8 — Verification / Continuation Register

Date: 2026-09-12 (JST)

## Entry-gate status

- repeated Stage 4A: **GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS**;
- repaired Stage 6: **GO**;
- repaired Stage 7: **GO**;
- repaired Stage 7.5: **GO TO STAGE 7.5A**;
- repaired Stage 7.5A: **GO — GENERALITY / QUANTIFIER CERTIFICATION PASS**;
- Formal Verification Gate: **FORMAL VERIFICATION PASS**.

Canonical analytic certificate: `theorem_certificates/stage4a_repair_certificates.md`.
Canonical scope certificate: `docs/STAGE_075A_REPAIRED_CERTIFICATION.md`.
Canonical formal certificate: `formal/FORMAL_VERIFICATION_CERTIFICATE_REPAIRED.md`.

## Continuation completeness

Provider continuation is globally defined at every installed state by comparing both-served, H-only, and no-service candidates. L-only is infeasible under the anonymous common tariff when H is installed. The repaired strict `R+` certifies both-served global dominance on the complete rational-expectations candidate interval `[h_0,h_F]`.

Off-path continuation classes relevant to unilateral deviations are therefore defined. T1–T3 use both-served formulas only on `R+`; no global equilibrium theorem outside `R+` is claimed.

Unresolved material continuations used as evidence: **0**.
Numerical failures interpreted as unprofitable deviations: **0**.
Invalid active sets interpreted as equilibrium evidence: **0**.

Independent direct-payoff/global-continuation artifact: `verification/stage4a_repair_independent.py`.

## Python / regression evidence

- `verification/baseline_checks.py` — exact baseline algebra and permanent `23/10` scope counterexample;
- `verification/stage4a_repair_independent.py` — repaired active-set and alternative-equilibrium audit;
- `verification/stage7_repaired_verify.py` — welfare identities and strict-`R+` opposite-sign welfare examples;
- `verification/stage075a_scope_verify.py` — repaired quantifier/endpoint/welfare scope checks;
- `verification/stage11b_astra_independent_audit.py` — independent nonquadratic survival and strict-concavity counterexample evidence.

## Formal verification

Verified repaired build source: `d6ac2a4bca0bf10dbfea23b274951d15b39d8551`.
Workflow run: `34678945920`.

- Lean 4.33.1;
- mathlib v4.33.1, resolved revision `0df444a360eaa60ab8c11dca51a86af692955474`;
- build command `lake build DynamicTariffFormal`;
- build result SUCCESS;
- no-`sorry`/`admit` audit PASS;
- dependencies reported only `propext`, `Classical.choice`, `Quot.sound`;
- no project-specific axiom.

Formal coverage is **PROOF-CRITICAL CORE**, not the complete economic game.

Mapped Lean components include threshold ordering, strict-gap response reversal, antitone fixed-point uniqueness, repaired lower/upper state ordering, mixed-state uniqueness skeleton, positivity of the baseline `Phi_h` expression, endpoint-dominance propagation, W1 identity/sign, and the exact `23/10` outside-domain counterexample.

Not formalized: weak-participation strategy primitive, primitive demand derivation, complete provider tariff optimization, full atomless equilibrium correspondence, mixed-equilibrium existence/probability bounds, endogenous welfare comparison, institutional interpretation.

## Permanent regression/scope guards

Certified baseline:

`a_L=4, a_H=5, c=1, b_L=16/5, K_L=4, b_H=1/2, K_H=8, mu=13/10`,

with `h_0=1/16<h_M<h_F=5/8` and `mu_M<mu<mu_F`.

Permanent outside-domain guard:

`a_L=4,a_H=5,c=1,l=0.1,h=0.6`, where H-only flat pricing exceeds both-served flat profit by exactly `23/10`.

Therefore any all-positive-parameter/global-installed-composition formulation is prohibited.
