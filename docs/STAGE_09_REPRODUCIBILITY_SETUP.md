# Stage 9 — Repository / Reproducibility Setup

Date: 2026-09-12 (JST)
Workflow: `ryotamatsuki/research-paper-workflow` v2.1
Project: **Dynamic Tariff Choice for Generative AI: Model Improvement, Commitment, and Welfare**

## Verdict

**REPRODUCIBILITY BASELINE READY.**

Stage 10 paper construction is authorized, subject to the exact writing contract below. No theory change was made in Stage 9.

## 1. Starting remote state

At Stage-9 work start:

- `main`: `2597e82044ec94a58fad033227ea415e64af8c6d`;
- that SHA is the Stage-8 canonical theory-freeze point;
- branches visible: `main` only;
- open pull requests: none.

The setup was built forward from that freeze. No reset to a historical SHA was used.

## 2. Production repository tree

The production scaffold now includes:

- `paper/main.tex` — modular manuscript entry point;
- `sections/` — Stage-10 section files;
- `figures/` and `tables/` — generated manuscript inputs plus pipeline documentation;
- `scripts/generate_outputs.py` — deterministic table/figure generator from the frozen exact example;
- `scripts/check_integrity.py` — freeze-ancestry, required-path, and scope-guard checks;
- `tests/test_regressions.py` — permanent frozen-theory regressions;
- `verification/` — exact symbolic and robustness checks retained from certification;
- `formal/` — Lean proof-critical core and formal certificate;
- `theorem_certificates/` — theorem/scope certificate;
- `references/references.bib` — bibliography database scaffold;
- `docs/freeze/` — canonical Stage-8 model, proposition, welfare, verification, and contribution registers;
- `docs/REPRODUCIBILITY.md` — local/CI reproduction guide;
- `.github/workflows/verify.yml` and `.github/workflows/reproducibility.yml` — independent formal/theory and full repository gates;
- `Makefile` — documented build interface.

## 3. Build system

The documented full local-equivalent gate is:

```bash
python -m pip install -r requirements-dev.txt
lake update
lake exe cache get
make all
```

`make all` runs Python verification/regression/integrity checks, the explicit Lean target and placeholder audit, deterministic figure/table generation, and the LaTeX manuscript build.

Partial targets are `make verify-python`, `make verify-lean`, `make artifacts`, and `make paper`.

## 4. Verification and permanent tests

Frozen-theory verification remains in:

- `verification/baseline_checks.py`;
- `verification/robustness_checks.py`;
- `formal/DynamicTariffFormal.lean`.

Permanent regressions are in `tests/test_regressions.py`, including:

1. the exact certified regular example with `h_M<h_F` and `mu_M<mu<mu_F`;
2. the outside-`R` H-only counterexample with exact advantage `23/10`;
3. collapse of the two architecture thresholds when the installed state is architecture-insensitive.

`check_integrity.py` additionally requires the Stage-8 freeze SHA to remain an ancestor of the build head and checks that the permanent scope guards remain present.

## 5. Theorem certificates and claim-scope artifacts

Canonical locations:

- `theorem_certificates/current_scope.md`;
- `formal/FORMAL_VERIFICATION_CERTIFICATE.md`;
- `docs/freeze/PROPOSITION_SCOPE_REGISTER.md`;
- `docs/freeze/VERIFICATION_REGISTER.md`;
- `docs/freeze/WELFARE_BENCHMARK_REGISTER.md`;
- `docs/freeze/CONTRIBUTION_REGISTER.md`.

These are retained as first-class repository artifacts and are not replaced by manuscript summaries.

## 6. Environment / dependency record

- Python CI: 3.12;
- Python: `sympy==1.14.0`;
- Lean: 4.33.1;
- mathlib: v4.33.1;
- LaTeX build: `latexmk` plus TeX Live recommended/extra/pictures and `lmodern`.

Lean and mathlib remain pinned by `lean-toolchain` and `lakefile.lean`.

## 7. Figure and table pipeline

`scripts/generate_outputs.py` regenerates:

- `figures/threshold_phase.tex`;
- `tables/baseline_example.tex`.

Both files are generated from frozen exact expressions, are git-ignored, and are consumed directly by `sections/03_equilibrium.tex`. They are not to be hand-edited.

## 8. CI validation

Full Stage-9 reproducibility workflow run `34663574054` passed:

- frozen-theory symbolic and robustness checks: PASS;
- three permanent unit regressions: PASS;
- freeze/scope integrity gate: PASS;
- deterministic artifact generation: PASS;
- LaTeX toolchain install: PASS;
- manuscript scaffold build: PASS;
- PDF artifact upload: PASS.

The existing `verify` workflow separately runs the baseline/robustness checks and the explicit Lean target with the no-`sorry`/`admit` audit. This remains a required independent gate.

## 9. Provenance / decision locations

- Stage-8 freeze: `docs/STAGE_08_THEORY_FREEZE.md`;
- Stage-9 reproduction instructions: `docs/REPRODUCIBILITY.md`;
- post-freeze theory changes: `docs/CHANGE_CONTROL.md`;
- portfolio stage/status SSOT: `ryotamatsuki/economic-theory-research-portfolio#30`.

## 10. Remaining blockers

None for Stage 10 section writing. The bibliography is intentionally only a scaffold at Stage 9; source-verified entries must be added as Stage-10 prose is written.

## 11. Exact Stage-10 writing contract

Stage 10 may write and reorganize exposition only under all of the following constraints:

1. the Stage-8 theory freeze and linked registers are authoritative;
2. no player, state, tariff instrument, timing change, equilibrium claim, welfare benchmark, or theorem quantifier may be added or changed without `docs/CHANGE_CONTROL.md` rollback/refreeze;
3. every theorem/proposition statement must remain within `docs/freeze/PROPOSITION_SCOPE_REGISTER.md` and be traceable to the certificate/verification artifacts;
4. the regular both-served region `R` and the H-only counterexample must remain visible wherever globality could be misunderstood;
5. nonquadratic cases remain numerical robustness only, and arbitrary-concave-demand wording is prohibited;
6. the Lean artifact must be described as proof-critical-core verification only;
7. the fixed-installed-base welfare wedge must not be promoted to a global endogenous welfare ranking;
8. numerical manuscript objects must be generated from repository source when feasible rather than hand edited;
9. literature metadata and institutional facts must be source-verified before citation;
10. repository verification and manuscript build gates must remain green after writing changes.

## Final routing

**REPRODUCIBILITY BASELINE READY — GO TO STAGE 10 PAPER BUILD.**
