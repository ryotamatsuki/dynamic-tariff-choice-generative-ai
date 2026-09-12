# Stage 8 — Canonical Theory Freeze (Repaired Model)

Freeze date: 2026-09-12 (JST)  
Workflow: `ryotamatsuki/research-paper-workflow` v2.1  
Project: **Dynamic Tariff Choice for Generative AI: Integration, Commitment, and Welfare**

## Verdict

**THEORY FROZEN — GO TO REPRODUCIBILITY SETUP.**

This repaired freeze supersedes the earlier Stage-8 freeze based on commit `2597e82044ec94a58fad033227ea415e64af8c6d`.

Entry hard gates are closed:

- repeated Stage 4A: `GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS`;
- repaired Stage 7.5A: `GO — GENERALITY / QUANTIFIER CERTIFICATION PASS`;
- Formal Verification Gate: `FORMAL VERIFICATION PASS`.

## Frozen research question

When users make sunk, relationship-specific AI integration decisions before a provider can revise its future tariff architecture, can expectations about future flat versus metered pricing alter the installed high-use composition in a way that feeds back into the provider's own later architecture incentive?

## Frozen contribution

On strict repaired region `R+`, anticipated metering induces a smaller high-use installed state than anticipated flat pricing, while the provider's gross gain from metering rises with that installed state. The architecture expected before integration therefore changes the state on which the same architecture is later evaluated. A single fixed-state switching threshold splits into two self-consistency thresholds `mu_M<mu_F`. For `mu_M<mu<mu_F`, neither pure architecture is self-consistent. Architecture-insensitive integration collapses the two thresholds.

The contribution is this reciprocal state feedback, not generic hold-up, two-part tariffs, subscription-versus-usage pricing, mixed strategies, AI as an application label, or quality/model improvement.

## Canonical repaired registers

- Model, strategy domain, weak-participation rule, global continuation correspondence, strict `R+`, and equilibrium objects: `docs/freeze_repaired/MODEL_REGISTER.md`
- Proposition quantifiers, proof maturity, robustness scope, and prohibited stronger claims: `docs/freeze_repaired/PROPOSITION_SCOPE_REGISTER.md`
- Welfare and exact benchmark definitions: `docs/freeze_repaired/WELFARE_BENCHMARK_REGISTER.md`
- Stage-4A/7.5A/formal/continuation/counterexample evidence: `docs/freeze_repaired/VERIFICATION_REGISTER.md`
- Contribution, closest-paper distinction, institutional interpretation, title, and explicit exclusions: `docs/freeze_repaired/CONTRIBUTION_REGISTER.md`

Canonical upstream certificates:

- `docs/STAGE_04R_REPAIR.md`
- `docs/STAGE_04A_RECERTIFICATION.md`
- `theorem_certificates/stage4a_repair_certificates.md`
- `docs/STAGE_06_REKILL_REPAIR_RATIFICATION.md`
- `docs/STAGE_07_REPAIRED_WELFARE_GENERALITY.md`
- `docs/STAGE_075_REPAIRED_FREEZE_DECISION.md`
- `docs/STAGE_075A_REPAIRED_CERTIFICATION.md`
- `formal/FORMAL_VERIFICATION_CERTIFICATE_REPAIRED.md`

## Frozen claim scope

T1–T3 are quadratic-baseline theorems on strict `R+`. The abstract ordered-state/increasing-gain result is only an organizing sufficient-condition lemma. Common-curvature nonquadratic survival is numerical robustness only. Arbitrary strict concavity is not a valid general theorem. No non-Uniform-CDF theorem is carried into this freeze.

W1, `mu_P-mu_W=d h p*(h)>0`, is a fixed-installed-base identity, not a global endogenous-welfare theorem. P0 is the only object called first best; P1 is fixed-allocation; P2 is restricted architecture commitment.

## Formal-verification boundary

State: **FORMAL VERIFICATION PASS**.

Verified repaired formal build source: `d6ac2a4bca0bf10dbfea23b274951d15b39d8551`; workflow run `34678945920`; Lean 4.33.1; mathlib revision `0df444a360eaa60ab8c11dca51a86af692955474`; `lake build DynamicTariffFormal` succeeded; placeholder audit passed; no project-specific axiom.

Formal coverage is **PROOF-CRITICAL CORE** only. Weak participation, full provider continuation optimization, the complete atomless equilibrium correspondence, mixed-equilibrium existence, endogenous welfare comparison, and institutional interpretation are not fully formalized.

## Continuation completeness and permanent scope guard

Provider continuation is globally defined at every installed state by both-served / H-only / no-service comparison. On strict `R+`, both-served continuation strictly dominates over the complete rational-expectations candidate interval `[h_0,h_F]`. Material unresolved continuations used as evidence: zero.

Permanent outside-domain guard: at `a_L=4,a_H=5,c=1,l=0.1,h=0.6`, H-only flat pricing beats both-served flat pricing by exactly `23/10`. Hence no all-positive-parameter/global-installed-composition version is frozen.

## Freeze identity

Pre-freeze certified repository head: `a1726561e9167ed100bd423eb4898fff275de029`.

The commit created by this repaired Stage-8 declaration, together with the repaired registers above, is the canonical freeze declaration point. Later administrative descendants may record CI/status without changing the frozen theory.

## Routing

Stage 9 — Reproducibility Setup must now be **rerun/rebased on this repaired freeze** before manuscript/referee work resumes. The earlier Stage-9/10 artifacts remain historical until that downstream rerun is completed.

Post-freeze theory changes are governed by `docs/CHANGE_CONTROL.md`; no silent theory drift is permitted.
