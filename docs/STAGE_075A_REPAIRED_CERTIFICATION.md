# Stage 7.5A — Repaired Generality / Quantifier Certification

Date: 2026-09-12 (JST)

## Verdict

**GO — GENERALITY / QUANTIFIER CERTIFICATION PASS.**

Formal Verification Gate: **FORMAL VERIFICATION PASS**.

Next authorized action: **Stage 8 — Canonical Theory Freeze**.

## Certified theorem scope

- **T1.** For every parameter vector in strict `R+`, the metered rational-expectations fixed point exists uniquely and satisfies `h_0<h_M<h_F`.
- **T2.** For every parameter vector in strict `R+`, `mu_M=Phi(l,h_M)<Phi(l,h_F)=mu_F`.
- **T3.** For every parameter vector in strict `R+` and every `mu` with `mu_M<mu<mu_F`, neither pure architecture is self-consistent; the certified branch has a unique aggregate mixed resolution.
- **B1.** Architecture-insensitive integration, `h_M=h_F`, collapses the two thresholds.
- **W1.** Holding installed `(l,h)` fixed on the quadratic both-served branch, `mu_P-mu_W=d h p*(h)>0` for positive `d,h`.
- **W2.** No universal sign is authorized for the restricted architecture-commitment welfare ranking; strict-`R+` examples of both signs exist.

Equality cases `mu=mu_M,mu_F` are outside T3. No all-positive-parameter result and no result outside strict `R+` is claimed.

## Generality classification

- T1–T3: **BASELINE FUNCTIONAL FORM on strict `R+`**.
- `h_M<h_F` plus increasing `Psi` implies threshold ordering: **SUFFICIENT-CONDITION / organizing lemma**.
- common-curvature nonquadratic example: **NUMERICAL ROBUSTNESS ONLY**.
- arbitrary strict concavity: **not valid as a general claim**; the Stage-11B example reverses `h_M<h_F`.
- non-Uniform integration-cost CDF theorem: **not included in the current certified claim set**.
- W1: **BASELINE ANALYTIC IDENTITY**.
- endogenous architecture welfare: **no universal ranking**.

## Equilibrium and selection scope

The repaired game makes zero-surplus future participation an explicit primitive. It is not an undisclosed refinement. Under strict `R+`, repaired Stage 4A covers the complete rational-expectations candidate interval `[h_0,h_F]` and certifies strict both-served dominance there. H-only and no-service do not provide hidden self-confirming pure outcomes on the claimed domain.

The integration cutoff is measure zero under the baseline continuous Uniform distribution. Provider indifference at the mixed state is intentional. Equality architecture thresholds are excluded from the strict headline result.

Outside `R+`, provider continuation is defined, but no global equilibrium or welfare theorem is claimed. The exact H-only advantage `23/10` remains the permanent scope guard.

## Welfare benchmark terminology

- **P0 first best:** planner chooses integration and usage directly. This is the only object called first best.
- **P1 fixed-allocation benchmark:** installed masses are held fixed while flat and metered decentralized allocations are compared.
- **P2 restricted architecture-commitment benchmark:** architecture is committed before integration while tariff parameters are later reoptimized within the chosen architecture.

W1 applies only to P1. It does not imply that metering is globally excessive once integration is endogenous.

## Evidence

Canonical mathematical evidence:

- `docs/STAGE_04R_REPAIR.md`
- `docs/STAGE_04A_RECERTIFICATION.md`
- `theorem_certificates/stage4a_repair_certificates.md`
- `verification/stage4a_repair_independent.py`
- `verification/stage075a_scope_verify.py`
- `verification/stage11b_astra_independent_audit.py`
- `verification/stage7_repaired_verify.py`

`verification/stage075a_scope_verify.py` independently checks the repaired endpoint derivative identities, `Phi_h`, the fixed-base welfare identity, exact repaired baseline margins, and the permanent outside-domain `23/10` example.

## Formal verification

Current certificate: `formal/FORMAL_VERIFICATION_CERTIFICATE_REPAIRED.md`.

Verified commit: `d6ac2a4bca0bf10dbfea23b274951d15b39d8551`.

GitHub Actions run `34678945920` passed both Python and Lean jobs. Lean 4.33.1 built `DynamicTariffFormal`; mathlib resolved to revision `0df444a360eaa60ab8c11dca51a86af692955474`. The dependency report contains only standard Lean/mathlib dependencies and no project-specific axiom.

The renewed formal target adds repaired-state ordering, endpoint propagation, and the fixed-base welfare identity to the previously formalized threshold/mixed-state core. It still does not formalize the weak-participation rule, the complete provider continuation problem, the full atomless integration game, mixed-equilibrium existence, or institutional interpretation.

## Required manuscript scope after refreeze

The next authorized manuscript revision must:

- use **Integration**, not “Model Improvement,” in the title unless theory is reopened;
- state T1–T3 as strict-`R+` quadratic-baseline results;
- label nonquadratic results as numerical robustness;
- omit a non-Uniform-CDF theorem;
- keep W1 explicitly fixed-installed-base;
- describe Lean as targeted formal verification only.

## Routing

No rollback is required. The repaired certified claim set survived Stage 7.5A with narrower, explicit scope.

**GO — GENERALITY / QUANTIFIER CERTIFICATION PASS.**
