# Current theorem / scope certificate

Stage 7.5A status: **GO — GENERALITY / QUANTIFIER CERTIFICATION PASS**.

Formal Verification Gate: **FORMAL VERIFICATION PASS**.

Stage 8: **THEORY FROZEN**. Stage 9: **REPRODUCIBILITY BASELINE READY**. Stage 10 paper construction is authorized; theorem scope remains unchanged from the Stage-8 freeze.

## T1 — Metered integration ordering

**Baseline statement.** On the Stage-4A-certified regular both-served region `R`, the metered rational-expectations fixed point exists uniquely and satisfies `0 < h_M < h_F`.

- Construction proof: PASS
- Independent Stage-4A attack: PASS
- Scope: branch-specific, not global
- Generalization: a broader state-order result is available under explicit antitone/interiority/crossing conditions; not asserted for arbitrary CDF/rent systems.

Maximum wording: “On a regular both-served region, anticipated metering induces a strictly smaller high-use installed state than anticipated flat pricing.”

Prohibited wording: “Metering always reduces integration for all positive parameters.”

## T2 — Threshold separation

**Baseline statement.** On `R`, `mu_M < mu_F`.

**Sufficient-condition statement.** If `h_M < h_F` and gross metering gain `Psi(h)` is strictly increasing, then `Psi(h_M) < Psi(h_F)`.

- Baseline analytic proof: PASS
- Stage-4A attack: PASS
- Abstract order-theoretic implication: PASS analytically
- Targeted Lean theorem: PASS (`threshold_separation`)

Maximum wording: “Architecture-sensitive integration can split a static tariff threshold when metering induces a lower installed high-use state and metering gain rises with that state.”

Prohibited wording: “All concave demand systems exhibit threshold separation.”

## T3 — Pure-regime gap

**Baseline statement.** On strict `R`, if `mu_M < mu < mu_F`, neither pure flat nor pure metered expectation is self-consistent; the regular branch has a unique mixed resolution.

- Candidate-deviation audit: PASS
- Alternative-equilibrium audit on the strict regular branch: PASS
- Boundary equality cases excluded
- Outside-`R` global characterization not claimed
- Lean strict-gap response implication: PASS
- Lean conditional mixed-state uniqueness skeleton: PASS

Abstract sufficient-condition wording may state only the no-pure-regime implication from ordered thresholds. Uniqueness of a mixed resolution additionally requires a continuous strictly monotone installed-state response to the provider's mixing probability.

## W1 — Fixed-installed-base welfare wedge

Holding `(l,h)` fixed on the baseline both-served branch,

`mu_P - mu_W = d h p*(h) > 0`.

This is a fixed-allocation benchmark, not a global endogenous-welfare theorem.

Maximum wording: “Holding the installed base fixed, the monopolist meters over a larger activation-cost region than a social evaluator comparing the same decentralized allocations.”

Prohibited wording: “Metering is always socially excessive.”

## Permanent scope counterexample

At `a_L=4`, `a_H=5`, `c=1`, `l=0.1`, `h=0.6`, H-only flat pricing beats the both-served flat continuation by exactly `23/10` in provider profit. Any theorem statement quantified over all positive installed compositions is therefore false.

The exact arithmetic difference is independently retained in Python regression code and in Lean theorem `hOnly_scope_counterexample`.

## Formal-verification state

**FORMAL VERIFICATION PASS.**

Successful CI build: workflow run `34660791188`, target `DynamicTariffFormal`, Lean 4.33.1 / mathlib v4.33.1. The build reports only standard logical/library axioms (`propext`, `Classical.choice`, `Quot.sound`) for the formal targets and the no-`sorry`/`admit` audit passes.

The formalization boundary and statement-fidelity limits are recorded in `formal/FORMAL_VERIFICATION_CERTIFICATE.md`.
