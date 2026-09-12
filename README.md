# Dynamic Tariff Choice for Generative AI

Theory project on dynamic tariff architecture, sunk AI-specific integration, and welfare.

## Status

**Stage 9 Reproducibility Baseline completed.**

- Stage 8: **THEORY FROZEN**
- Stage 9: **REPRODUCIBILITY BASELINE READY**
- Next stage: **Stage 10 — Paper Build**
- Portfolio status SSOT: `ryotamatsuki/economic-theory-research-portfolio#30`

## Frozen mechanism

On the certified regular both-served region `R`, anticipated metering induces a lower high-use installed state than anticipated flat pricing, while provider metering gain rises with that state. Hence one static switching threshold separates into `mu_M<mu_F`. For `mu_M<mu<mu_F`, neither pure architecture is self-consistent. Exogenous or architecture-insensitive integration collapses the thresholds to one.

The broader result is a sufficient-condition theorem, not arbitrary-concave-demand generality.

## Reproduce

With Python, Lean/Lake, and LaTeX installed:

```bash
python -m pip install -r requirements-dev.txt
lake update
lake exe cache get
make all
```

See `docs/REPRODUCIBILITY.md` for environment and partial-gate details.

## Repository layout

- `paper/`, `sections/` — modular manuscript scaffold
- `figures/`, `tables/` — deterministically generated manuscript inputs
- `scripts/` — artifact generation and freeze-integrity gates
- `tests/` — permanent regression tests
- `verification/` — symbolic/numerical certification checks
- `formal/` — Lean proof-critical core and formal certificate
- `theorem_certificates/` — theorem/scope certificate
- `references/` — bibliography database
- `docs/freeze/` — canonical Stage-8 model/scope/welfare/verification/contribution registers
- `.github/workflows/` — theory/formal and full reproducibility CI

## Canonical records

- `docs/STAGE_08_THEORY_FREEZE.md`
- `docs/STAGE_09_REPRODUCIBILITY_SETUP.md`
- `docs/REPRODUCIBILITY.md`
- `docs/freeze/MODEL_REGISTER.md`
- `docs/freeze/PROPOSITION_SCOPE_REGISTER.md`
- `docs/freeze/WELFARE_BENCHMARK_REGISTER.md`
- `docs/freeze/VERIFICATION_REGISTER.md`
- `docs/freeze/CONTRIBUTION_REGISTER.md`
- `docs/CHANGE_CONTROL.md`
- `theorem_certificates/current_scope.md`
- `formal/FORMAL_VERIFICATION_CERTIFICATE.md`

## Verification boundary

Python regression/robustness checks, permanent scope-counterexample tests, freeze-integrity checks, deterministic artifact generation, manuscript build, and the explicit Lean target are automated. The Lean certificate covers a proof-critical core only, not the complete economic model or global equilibrium correspondence.

## Change discipline

Any substantive post-freeze change to the model, theorem quantifiers, active-set/globality claims, welfare benchmarks, or formalized proof-critical statements must follow `docs/CHANGE_CONTROL.md` and be refrozen before downstream manuscript work continues.
