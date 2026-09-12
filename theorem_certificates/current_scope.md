# Current theorem / scope certificate

Stage 4A: **GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS**.  
Stage 7.5A: **GO — GENERALITY / QUANTIFIER CERTIFICATION PASS**.  
Formal Verification Gate: **FORMAL VERIFICATION PASS**.  
Stage 8: **THEORY FROZEN**.  
Stage 9: **REPRODUCIBILITY BASELINE READY**.  
Stage 10: **FULL DRAFT READY FOR REFEREE GATE**.  
Stage 11: **GO — REFEREE ATTACK GATE PASS**.

Canonical repaired freeze declaration: `c9e43c99d9deb56bad52637024b9dab7b3673aee`.
Canonical repaired Stage-11 audit report: `docs/STAGE_11_REFEREE_ATTACK_REPAIRED.md`.
Canonical independent Stage-11 audit: `verification/stage11_repaired_independent.py`.

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

Maturity: PROVED. Formal coverage: PROOF-CRITICAL CORE. Equality thresholds and outside-`R+` global characterization are excluded.

## B1

Architecture-insensitive integration implies `h_M=h_F`, hence `mu_M=mu_F` and threshold collapse.

Maturity: PROVED.

## W1

Holding installed `(l,h)` fixed on the quadratic both-served branch,

`mu_P-mu_W=d h p*(h)>0`.

Maturity: PROVED. Formal coverage: PROOF-CRITICAL CORE. This is not a global endogenous-welfare theorem.

## Generality and robustness ceiling

Common-curvature nonquadratic survival is numerical robustness only. Arbitrary strict concavity is not a valid general theorem. No non-Uniform integration-cost CDF theorem is in the repaired certified claim set.

Stage 11 adds a permanent hostile generality guard: with strictly concave but heterogeneous quadratic curvatures, the high-use continuation-rent ordering can reverse. This confirms that future manuscript or journal-positioning language must not promote the baseline mechanism to arbitrary strict concavity.

## Permanent scope guards

1. At `a_L=4,a_H=5,c=1,l=0.1,h=0.6`, H-only flat pricing exceeds both-served flat pricing by exactly `23/10`. Any all-positive-parameter/global-installed-composition formulation is prohibited.
2. Weak participation at zero continuation surplus is an explicit baseline tie-breaking primitive. No theorem equating the baseline pure-strategy characterization to a strict-participation convention is certified.
3. Stage-11 finite-deviation checks deliberately cross the low-use active-set boundary `p=a_L` and compare both-served, H-only, and no-service continuations. No profitable deviation was found on the frozen exact example over the certified candidate interval; this complements but does not enlarge the analytic Stage-4A certificate.

## Formal-verification state

Canonical certificate: `formal/FORMAL_VERIFICATION_CERTIFICATE_REPAIRED.md`.

Verified repaired build source `d6ac2a4bca0bf10dbfea23b274951d15b39d8551`, workflow run `34678945920`, Lean 4.33.1 / mathlib v4.33.1. Formal coverage is targeted proof-critical logic only, not the complete game/equilibrium correspondence.

Stage-11 closeout audit head `f07d7c39a79b9b7144024d220380812b40d2aad1` passed verify push run `34693026544` and reproducibility push run `34693026560` before merge through PR #1.

## Stage-11 novelty ceiling

The surviving novelty claim is restricted to the reciprocal architecture-state feedback and the resulting expectation-contingent threshold split. Generic hold-up, future-pricing effects on sunk investment, fixed-versus-usage pricing, two-part tariffs, metering costs, mixed pricing equilibria, AI/cloud application, and the fixed-installed-base private/social wedge are not standalone novelty claims.

## Routing

**Stage 12 — Journal Positioning is authorized.** Journal positioning must respect the repaired theorem scope and the Stage-11 novelty ceiling; it may not reopen killed claims or broaden the functional-form/general-equilibrium scope in order to target a higher-ranked journal.
