# Stage 4A Repair — Theorem Certificates

Date: 2026-09-12 (JST)

This file certifies only the repaired Stage-4/4A mathematical object. It does not reinstate the superseded Stage-8 freeze or Stage-7.5A formal-fidelity certificate.

## Repaired domain

All headline claims below are restricted to strict `R+` in `docs/STAGE_04R_REPAIR.md`.

The key strengthening is that both-served flat and metered continuations are strict global active-set optima over the complete rational-expectations candidate interval `h in [h_0,h_F]`, where `h_0=b_H/K_H` and `h_F=(b_H+R_F)/K_H`.

Future participation uses weak IR with participation at zero surplus.

## T1 — Metered integration ordering

**Exact claim.** For every parameter vector in `R+`, the metered rational-expectations fixed point exists uniquely and satisfies

`h_0<h_M<h_F`.

**Quantifiers.** Universal over parameters in `R+`; branch/domain restricted; not global over all positive parameters.

**Assumptions actually used.** Weak participation at equality; both-served global active-set dominance on `[h_0,h_F]`; `p_B(l,h_F)<a_L`; `d c < b_H+R_F < K_H`; positive masses/cost bounds.

**Proof type/location.** Monotone fixed-point residual in `docs/STAGE_04R_REPAIR.md` and `docs/STAGE_04A_RECERTIFICATION.md`.

**Candidate-deviation audit.** PASS.

**Alternative-equilibrium audit.** PASS: H-only/no-service expectations imply `h_0`, where both-served strictly dominates; no second fixed point found by independent global-continuation scan.

**Indifference audit.** PASS under explicit weak-participation primitive; integration cutoff is measure zero.

**Boundary/regime audit.** PASS on `R+`; exact outside-region counterexample retained.

**Continuation completeness.** PASS: provider global continuation correspondence defined at every installed state.

**Independent reconstruction.** PASS: `verification/stage4a_repair_independent.py`.

**Formalization applicability.** APPLICABLE; renewed economic fidelity pending downstream Stage 7.5A.

**Verdict.** PASS.

## T2 — Threshold separation

**Exact claim.** For every parameter vector in `R+`,

`mu_M=Phi(l,h_M)<Phi(l,h_F)=mu_F`.

**Quantifiers.** Universal on `R+`; quadratic baseline. The abstract implication from ordered states and strictly increasing gain is only a sufficient-condition lemma.

**Proof type/location.** Analytic derivative plus T1 ordering; direct-payoff difference independently reconstructed.

**Candidate-deviation audit.** PASS.

**Alternative-equilibrium audit.** PASS on the complete candidate interval because active-set alternatives are strictly dominated there.

**Indifference audit.** PASS; threshold equality cases are not part of the strict T3 claim.

**Boundary/regime audit.** PASS on `R+` only.

**Independent reconstruction.** PASS.

**Formalization applicability.** APPLICABLE.

**Verdict.** PASS.

## T3 — Pure-regime gap and mixed resolution

**Exact claim.** For every parameter vector in strict `R+` and every `mu` with `mu_M<mu<mu_F`, neither pure flat nor pure metered expectation is self-consistent. The certified regular branch has a unique aggregate mixed resolution `(h*,rho*)`, with

`h_M<h*<h_F`,

`Phi(l,h*)=mu`,

`rho*=K_H(h_F-h*)/[d p_B(l,h*)] in (0,1)`.

**Quantifiers.** Universal on strict `R+` and strict gap. Equality boundaries excluded. No global equilibrium characterization outside `R+`.

**Proof type/location.** Strict architecture best-response reversal, monotone architecture-gain root, and integration consistency.

**Candidate-deviation audit.** PASS using global continuation payoffs at `h_F` and `h_M`.

**Alternative-equilibrium audit.** PASS: H-only, no-service, L-only, zero-H and active-set alternatives do not support a hidden pure equilibrium on the claimed domain.

**Equilibrium-set status.** UNIQUE aggregate mixed equilibrium on the claimed regular branch, up to a measure-zero integration cutoff task and arbitrary off-path best-response selections that do not affect on-path outcomes.

**Indifference audit.** PASS: user zero-surplus participation explicitly defined; provider architecture indifference at `h*` is intentional and the supporting mix is uniquely pinned down.

**Boundary/regime audit.** PASS on `R+`; equality boundaries and outside-`R+` excluded.

**Continuation completeness.** PASS.

**Independent reconstruction.** PASS.

**Formalization applicability.** APPLICABLE.

**Verdict.** PASS.

## B1 — Architecture-insensitive integration benchmark

**Exact claim.** If architecture does not change the installed high-use state, `h_M=h_F=\bar h`, then

`mu_M=Phi(l,\bar h)=mu_F`.

The strict threshold gap collapses.

**Status.** PASS. This is a nested benchmark, not a novelty claim by itself.

## Permanent scope guard

At `a_L=4`, `a_H=5`, `c=1`, `l=0.1`, `h=0.6`, flat H-only pricing exceeds flat both-served pricing by exactly `23/10`.

Therefore any all-positive-parameter/global-installed-composition version of T1--T3 is prohibited.

## Certification state

**Stage 4A repaired certificate: PASS.**

**Old Stage-8 freeze: stale pending downstream reruns.**

**Old Stage-7.5A formal-fidelity certificate: stale as an economic-model certificate, although its conditional Lean algebra may remain technically valid.**
