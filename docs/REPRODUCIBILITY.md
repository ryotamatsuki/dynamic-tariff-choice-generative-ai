# Reproducibility Guide

Stage-8 theory freeze SHA: `2597e82044ec94a58fad033227ea415e64af8c6d`.

## Environment

- Python: CI uses 3.12
- Python dependency: `sympy==1.14.0` from `requirements-dev.txt`
- Lean: `leanprover/lean4:v4.33.1` from `lean-toolchain`
- mathlib: `v4.33.1` from `lakefile.lean`
- Manuscript: LaTeX with `latexmk`; CI installs TeX Live packages `texlive-latex-recommended`, `texlive-latex-extra`, `texlive-pictures`, and `lmodern`

## One-command gate

With Python, Lean/Lake, and LaTeX available:

```bash
python -m pip install -r requirements-dev.txt
lake update
lake exe cache get
make all
```

`make all` runs frozen-theory symbolic/robustness checks, unit regressions, repository-integrity checks, the explicit Lean target, deterministic table/figure generation, and the manuscript build.

## Partial gates

```bash
make verify-python
make verify-lean
make artifacts
make paper
```

Generated files:

- `figures/threshold_phase.tex`
- `tables/baseline_example.tex`
- `paper/main.pdf`

They are reproducible build outputs and are intentionally git-ignored.

## CI

- `.github/workflows/verify.yml`: symbolic/robustness Python checks plus explicit Lean build and placeholder audit.
- `.github/workflows/reproducibility.yml`: full-history freeze-integrity check, permanent regressions, deterministic artifact generation, LaTeX build, and PDF artifact upload.

## Provenance and scope

- Stage-8 freeze: `docs/STAGE_08_THEORY_FREEZE.md`
- Frozen model and theorem scope: `docs/freeze/`
- Formal proof boundary: `formal/FORMAL_VERIFICATION_CERTIFICATE.md`
- Permanent theorem scope: `theorem_certificates/current_scope.md`
- Post-freeze changes: `docs/CHANGE_CONTROL.md`

No generated number in the manuscript should be hand-edited when it can be produced by `scripts/generate_outputs.py` or an existing verification script.
