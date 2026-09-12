# Current theorem / scope certificate

Stage 4A: **GO — MATHEMATICAL ADVERSARIAL CERTIFICATION PASS**.  
Stage 7.5A: **GO — GENERALITY / QUANTIFIER CERTIFICATION PASS**.  
Formal Verification Gate: **FORMAL VERIFICATION PASS**.  
Stage 8: **THEORY FROZEN**.  
Stage 9: **REPRODUCIBILITY BASELINE READY**.

Canonical repaired freeze declaration: `c9e43c99d9deb56bad52637024b9dab7b3673aee`.

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

## Permanent scope guard

At `a_L=4,a_H=5,c=1,l=0.1,h=0.6`, H-only flat pricing exceeds both-served flat pricing by exactly `23/10`. Any all-positive-parameter/global-installed-composition formulation is prohibited.

## Formal-verification state

Canonical certificate: `formal/FORMAL_VERIFICATION_CERTIFICATE_REPAIRED.md`.

Verified repaired build source `d6ac2a4bca0bf10dbfea23b274951d15b39d8551`, workflow run `34678945920`, Lean 4.33.1 / mathlib v4.33.1. Formal coverage is targeted proof-critical logic only, not the complete game/equilibrium correspondence.

## Routing

Stage 10 paper build/repair is authorized only against the repaired Stage-8 freeze and the Stage-9 writing contract in `docs/STAGE_09_REPRODUCIBILITY_SETUP.md`. Pre-repair Stage-10 wording has no inherited certification.
