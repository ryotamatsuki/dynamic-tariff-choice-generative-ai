# Current theorem / scope certificate

Stage 4A: **GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS**.  
Stage 7.5A: **GO — GENERALITY / QUANTIFIER CERTIFICATION PASS**.  
Formal Verification Gate: **FORMAL VERIFICATION PASS**.  
Stage 8: **THEORY FROZEN**.  
Stage 9: **REPRODUCIBILITY BASELINE READY**.  
Stage 10: **FULL DRAFT READY FOR REFEREE GATE**.  
Stage 11 prior closeout: historical **GO — REFEREE ATTACK GATE PASS**.  
Stage 11 Astra repair recheck: **REPAIR WITHIN STAGE 11 — literature-source blocker remains**.

Canonical repaired freeze declaration: `c9e43c99d9deb56bad52637024b9dab7b3673aee`.
Historical repaired Stage-11 audit report: `docs/STAGE_11_REFEREE_ATTACK_REPAIRED.md`.
Historical independent Stage-11 audit: `verification/stage11_repaired_independent.py`.
Current additive Astra repair verifier: `verification/stage11_astra_repair_verify.py`.

## T1

For every parameter vector in strict repaired region `R+`, the metered rational-expectations fixed point exists uniquely and satisfies

`h_0<h_M<h_F`.

Maturity: PROVED. Formal coverage: PROOF-CRITICAL CORE. Quadratic baseline only.

## T2

For every parameter vector in strict `R+`,

`mu_M=Phi(l,h_M)<Phi(l,h_F)=mu_F`.

Maturity: PROVED. Formal coverage: PROOF-CRITICAL CORE.

The abstract ordered-state plus increasing-gain implication is only an organizing sufficient-condition lemma, not an arbitrary-concavity theorem.

## T3

For every parameter vector in strict `R+` and every `mu` satisfying `mu_M<mu<mu_F`, neither pure flat nor pure metered expectation is self-consistent. The certified branch has a unique aggregate mixed resolution.

Maturity: PROVED. Formal coverage: PROOF-CRITICAL CORE. Outside-`R+` global characterization is excluded.

## Pure-boundary characterization added in the Stage-11 Astra repair

Because provider indifference is permitted, the pure metered outcome is self-consistent for `mu<=mu_M`, and the pure flat outcome is self-consistent for `mu>=mu_F`. At `mu=mu_M`, aggregate consistency forces `rho=1` and `h=h_M`; at `mu=mu_F`, it forces `rho=0` and `h=h_F`. Provider indifference at the pure induced state does not make arbitrary endpoint mixing aggregate-consistent because any non-pure endpoint mixture changes the installed state and breaks the provider tie through strict monotonicity of `Phi`.

This boundary clarification does **not** alter T1--T3, the primitive set, or strict `R+`; it repairs the manuscript's previous strict-inequality wording around the closed pure-equilibrium regions. It is checked by the additive Python verifier and is not newly claimed as Lean-certified.

## B1

Architecture-insensitive integration implies `h_M=h_F`, hence `mu_M=mu_F` and threshold collapse.

Maturity: PROVED.

## W1

Holding installed `(l,h)` fixed on the quadratic both-served branch,

`mu_P-mu_W=d h p*(h)>0`.

Maturity: PROVED. Formal coverage: PROOF-CRITICAL CORE. This is not a global endogenous-welfare theorem.

## Generality and robustness ceiling

Common-curvature nonquadratic survival is numerical robustness only. Arbitrary strict concavity is not a valid general theorem. No non-Uniform integration-cost CDF theorem is in the repaired certified claim set.

Stage 11 retains a permanent hostile generality guard: with strictly concave but heterogeneous quadratic curvatures, the high-use continuation-rent ordering can reverse. Future manuscript or journal-positioning language must not promote the baseline mechanism to arbitrary strict concavity.

## Permanent scope guards

1. At `a_L=4,a_H=5,c=1,l=0.1,h=0.6`, H-only flat pricing exceeds both-served flat pricing by exactly `23/10`. Any all-positive-parameter/global-installed-composition formulation is prohibited.
2. Weak participation at zero continuation surplus is an explicit baseline tie-breaking primitive. No theorem equating the baseline pure-strategy characterization to a strict-participation convention is certified.
3. The Astra repair derives the complete candidate interval from optimal continuation before applying endpoint dominance; `[h_0,h_F]` is not an imposed search restriction.
4. The Astra repair's finite-deviation evaluator crosses `p=a_L` and `p=a_H`, checks threshold fixed fees and explicit negative subsidies, and does not use solver failure as evidence against deviations.

## Formal-verification state

Canonical certificate: `formal/FORMAL_VERIFICATION_CERTIFICATE_REPAIRED.md`.

Verified repaired build source `d6ac2a4bca0bf10dbfea23b274951d15b39d8551`, workflow run `34678945920`, Lean 4.33.1 / mathlib v4.33.1. Formal coverage remains targeted proof-critical logic only, not the complete game/equilibrium correspondence. The Astra repair adds manuscript and Python verification of active-set globality, candidate-interval completeness, boundary equilibria, and the explicit mixed strategy construction. **No new Lean proof was added**, so none of those additions may be described as newly formally verified.

## Stage-11 novelty ceiling and current blocker

The surviving novelty claim is restricted to the specific reciprocal architecture-state feedback and the resulting expectation-contingent threshold split. Generic hold-up, the generic expectation--participation--repricing sequence, fixed-versus-usage pricing, two-part tariffs, metering costs, mixed pricing equilibria, AI/cloud application, and the fixed-installed-base private/social wedge are not standalone novelty claims.

`docs/STAGE_11_ASTRA_REPAIR_PRIOR_ART.md` records the fresh prior-art comparison. Hagiu (2006) is the strongest unresolved source item: the publisher abstract and a complete public working-paper predecessor were inspected, but the complete published RAND version of record was not accessible in the current environment. Under the explicit fail-closed repair instruction, that source limitation prevents final Stage-11 re-ratification.

## Routing

**Stage 12 authorization is PAUSED.** Remain in **Stage 11 repair** until the complete published Hagiu (2006) comparison is closed. If the published text contains a whole-game absorber for the specific reciprocal architecture-state-profitability loop and two-threshold/mixing result, roll back to Stage 6; otherwise Stage 11 may be re-ratified without changing T1--T3.
