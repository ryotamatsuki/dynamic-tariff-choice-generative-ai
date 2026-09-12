# Project status

Last synchronized: 2026-09-12 (JST)

## Canonical workflow state

- Workflow: `ryotamatsuki/research-paper-workflow` v2.1
- Stage 7.5: **GO**
- Stage 7.5A: **CONDITIONAL GO**
- Stage 8: **BLOCKED**
- Single blocker: obtain a successful Lean kernel-checked build and close statement-fidelity / axiom / placeholder audit on the frozen theorem set.

## Canonical roles

- This repository: canonical mathematical, verification, and formal-artifact source from repository initialization onward.
- `ryotamatsuki/economic-theory-research-portfolio#30`: portfolio stage/status SSOT and historical execution record.
- Historical pre-repository Stage reports remain preserved in the central portfolio; they are provenance inputs, not competing current sources.

## Frozen theorem scope entering Stage 7.5A

### Baseline theorem

Within the Stage-4A-certified regular both-served region `R`:

- `T1`: the metered integration fixed point is unique and `0 < h_M < h_F`;
- `T2`: `mu_M < mu_F`;
- `T3`: if `mu_M < mu < mu_F`, neither pure architecture is self-consistent and the regular branch has a unique mixed resolution;
- exogenous or architecture-insensitive integration collapses the two thresholds to one.

### Stage-7.5A sufficient-condition theorem

Let `h_F` and `h_M` be the installed high-use states induced by anticipating flat and metered architecture. Let `Psi(h)` denote the provider's gross gain from metering before the real activation cost `mu`.

If

1. `h_M < h_F`, and
2. `Psi` is strictly increasing,

then

`mu_M := Psi(h_M) < Psi(h_F) =: mu_F`.

For any `mu` strictly between these thresholds, pure flat and pure metered expectations are both inconsistent with the provider's ex-post best response. If the installed state induced by a metering probability varies continuously and strictly monotonically between `h_F` and `h_M`, the mixed installed state is unique.

Classification: **SUFFICIENT-CONDITION THEOREM**, not a general theorem over all concave demand systems.

## Scope restrictions that must remain visible

- Baseline global active-set characterization outside `R` is not claimed.
- An H-only counterexample outside `R` is a permanent regression test.
- Nonquadratic power-utility checks are numerical robustness only.
- Strict concavity alone is not certified to imply state ordering or monotone metering gain.
- The fixed-installed-base welfare wedge is not a global endogenous-welfare ranking.

## Immediate next action

Close the Formal Verification Gate only. No theory extension is authorized before Stage 8.
