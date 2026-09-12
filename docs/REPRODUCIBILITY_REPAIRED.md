# Repaired Reproducibility Guide

Freeze declaration: `c9e43c99d9deb56bad52637024b9dab7b3673aee`.

Canonical scope:
- `docs/STAGE_08_THEORY_FREEZE.md`
- `docs/freeze_repaired/`
- `theorem_certificates/current_scope.md`
- `formal/FORMAL_VERIFICATION_CERTIFICATE_REPAIRED.md`

Environment: Python 3.12, `sympy==1.14.0`, Lean 4.33.1, mathlib v4.33.1, and LaTeX with `latexmk`.

Run `make all` after installing the documented dependencies. Partial targets are `make verify-python`, `make verify-lean`, `make artifacts`, and `make paper`.

CI entry points are `.github/workflows/verify.yml` and `.github/workflows/reproducibility.yml`.

Generated manuscript inputs come from `scripts/generate_outputs.py`. Permanent regressions are in `tests/test_regressions.py` and `verification/`.

Stage 10 must use the repaired freeze and `R+` scope. Older manuscript prose is retained only as a buildable starting scaffold until Stage 10 is rerun.
