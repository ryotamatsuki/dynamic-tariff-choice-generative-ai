# Dynamic Tariff Choice for Generative AI

Theory project on dynamic tariff architecture, sunk AI-specific integration, and welfare.

## Status

**Stage 8 Canonical Theory Freeze completed.**

- Stage 7.5A: GO
- Formal Verification Gate: PASS
- Stage 8: **THEORY FROZEN**
- Next stage: **Stage 9 — Reproducibility Setup**
- Portfolio status SSOT: `ryotamatsuki/economic-theory-research-portfolio#30`

## Frozen mechanism

On the certified regular both-served region `R`, anticipated metering induces a lower high-use installed state than anticipated flat pricing, while provider metering gain rises with that state. Hence one static switching threshold separates into `mu_M<mu_F`. For `mu_M<mu<mu_F`, neither pure architecture is self-consistent. Exogenous or architecture-insensitive integration collapses the thresholds to one.

The broader result is a sufficient-condition theorem, not arbitrary-concave-demand generality.

## Canonical freeze files

- `docs/STAGE_08_THEORY_FREEZE.md`
- `docs/freeze/MODEL_REGISTER.md`
- `docs/freeze/PROPOSITION_SCOPE_REGISTER.md`
- `docs/freeze/WELFARE_BENCHMARK_REGISTER.md`
- `docs/freeze/VERIFICATION_REGISTER.md`
- `docs/freeze/CONTRIBUTION_REGISTER.md`
- `docs/CHANGE_CONTROL.md`
- `theorem_certificates/current_scope.md`
- `formal/FORMAL_VERIFICATION_CERTIFICATE.md`

## Verification

Python regression/robustness checks and the explicit Lean target build run in `.github/workflows/verify.yml`. The Lean certificate covers a proof-critical core only, not the complete economic model or global equilibrium correspondence.

## Change discipline

Any substantive post-freeze change to the model, theorem quantifiers, active-set/globality claims, welfare benchmarks, or formalized proof-critical statements must follow `docs/CHANGE_CONTROL.md` and be refrozen before downstream manuscript work continues.
