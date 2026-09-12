# Dynamic Tariff Choice for Generative AI

Working research repository for a theory project on dynamic tariff architecture, sunk AI-specific integration, and welfare.

## Status

**Pre-freeze candidate project.**

- Canonical workflow: `ryotamatsuki/research-paper-workflow` v2.1
- Current gate: **Stage 7.5A — Generality / Quantifier Red-Team**
- Canonical verdict: **CONDITIONAL GO**
- Single blocking item: **Formal Verification Gate**
- Stage 8 Canonical Theory Freeze: **NOT YET AUTHORIZED**
- Portfolio execution record: `ryotamatsuki/economic-theory-research-portfolio#30`

This repository is the canonical location for the project's mathematical, verification, and formal artifacts from this point forward. The central portfolio Issue remains the stage/status SSOT.

## Research question

When enterprise users make sunk AI-specific integration decisions before a provider can revise its future tariff architecture, how does the anticipated architecture change the installed base on which the provider later evaluates that same architecture, and what does this imply for tariff switching, equilibrium, and welfare?

## Core certified mechanism

On the Stage-4A-certified regular both-served region `R`:

1. anticipated metering induces a lower installed high-use state than anticipated flat pricing, `h_M < h_F`;
2. the provider's gross metering gain is increasing in the installed high-use state;
3. therefore the ordinary static tariff threshold separates into `mu_M < mu_F`;
4. for `mu_M < mu < mu_F`, neither pure flat nor pure metered architecture is self-consistent;
5. with exogenous or architecture-insensitive integration, `h_M = h_F` and the gap collapses.

Stage 7.5A additionally identifies a broader **sufficient-condition theorem** based on ordered architecture-induced states plus a strictly increasing metering-gain map. This is not a theorem for arbitrary concave demand systems.

## Scope guards

The paper must not claim that endogenous integration always creates a tariff-regime gap. The baseline theorem is branch-specific to a regular region in which both task classes remain served under the relevant continuation tariffs. An H-only active-set counterexample outside that region is retained as a permanent regression test.

The fixed-installed-base welfare result is also deliberately narrow: the provider's metering threshold exceeds the corresponding social threshold for the same installed allocation, but no unconditional full-endogenous welfare ranking is claimed.

## Repository layout

- `docs/` — current status, theorem scope, provenance, and stage certificates
- `verification/` — symbolic/numerical regression checks
- `formal/` — Lean 4 proof-critical core and formalization boundary
- `theorem_certificates/` — theorem/scope certificates
- `.github/workflows/` — reproducible Python and Lean verification

A manuscript tree (`paper/`, `figures/`, `submission/`) is intentionally not initialized before Stage 8 theory freeze.

## Reproducibility

Python verification:

```bash
python -m pip install -r requirements-dev.txt
python verification/baseline_checks.py
python verification/robustness_checks.py
```

Lean verification:

```bash
lake update
lake exe cache get
lake build
```

The Lean toolchain and mathlib release are pinned in `lean-toolchain` and `lakefile.toml`.

## Workflow discipline

No new variables, extensions, applications, contracts, or theorem engineering are authorized while Stage 7.5A remains open. The next admissible action is to close the Formal Verification Gate on the frozen theorem set. Only after Stage 7.5A passes may the project enter Stage 8 Canonical Theory Freeze.
