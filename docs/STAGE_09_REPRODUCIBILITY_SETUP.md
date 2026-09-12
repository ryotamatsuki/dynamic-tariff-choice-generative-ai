# Stage 9 — Repository / Reproducibility Setup (Repaired Freeze)

Date: 2026-09-12 (JST)  
Workflow: `ryotamatsuki/research-paper-workflow` v2.1  
Project: **Dynamic Tariff Choice for Generative AI: Integration, Commitment, and Welfare**

## Verdict

**REPRODUCIBILITY BASELINE READY.**

Stage 9 is rerun/rebased on the repaired Stage-8 freeze. No theory, theorem scope, benchmark definition, or economic mechanism is changed here.

## 1. Starting remote state

At repaired Stage-9 work start:

- `main`: `8311e4cfddd016cd6a69126d26d9c52339549c4e`;
- canonical repaired Stage-8 freeze declaration: `c9e43c99d9deb56bad52637024b9dab7b3673aee`;
- visible branches: `main` and `audit/stage11b-astra-independent`;
- open pull requests: none.

The audit branch is retained as provenance and was not overwritten. No reset to a historical SHA was used.

## 2. Canonical production tree

The reproducibility baseline uses:

- `paper/main.tex` — modular LaTeX entry point;
- `sections/` — manuscript section sources to be rewritten/re-certified at Stage 10;
- `figures/`, `tables/` — deterministic generated inputs;
- `scripts/generate_outputs.py` — deterministic figure/table generation;
- `scripts/check_integrity.py` — repaired-freeze ancestry, path, scope, and routing guards;
- `tests/test_regressions.py` — permanent exact regressions;
- `verification/` — symbolic, independent adversarial, welfare, quantifier, and hostile-audit artifacts;
- `formal/` — repaired Lean proof-critical core and certificate;
- `theorem_certificates/` — Stage-4A and current claim-scope certificates;
- `references/` — bibliography sources;
- `docs/freeze_repaired/` — canonical repaired model/proposition/welfare/verification/contribution registers;
- `docs/REPRODUCIBILITY.md` — local and CI reproduction guide;
- `.github/workflows/verify.yml`, `.github/workflows/reproducibility.yml` — independent theory/formal and full-repository gates;
- `Makefile` — one-command build interface.

Pre-repair `docs/freeze/` records and pre-repair Stage-9/10 prose remain historical provenance only.

## 3. Build system

With Python, Lean/Lake, and LaTeX available:

```bash
python -m pip install -r requirements-dev.txt
lake update
lake exe cache get
make all
```

`make all` runs the Python/theory regressions, repaired integrity gate, explicit Lean target and placeholder audit, deterministic artifact generation, and LaTeX build.

Partial targets are `make verify-python`, `make verify-lean`, `make artifacts`, and `make paper`.

## 4. Verification / regression artifacts

Required repaired-theory artifacts include:

- `verification/baseline_checks.py`;
- `verification/robustness_checks.py` — numerical robustness only where so scoped;
- `verification/stage4a_repair_independent.py`;
- `verification/stage7_repaired_verify.py`;
- `verification/stage075a_scope_verify.py`;
- `verification/stage11b_astra_independent_audit.py` — hostile-audit provenance;
- `formal/DynamicTariffFormal.lean`;
- `tests/test_regressions.py`.

Permanent regressions include the exact strict-`R+` example, `h_0<h_M<h_F`, the threshold-gap example, architecture-insensitive threshold collapse, and the outside-domain H-only counterexample with exact advantage `23/10`.

No certified counterexample is deleted or reinterpreted as a theorem-domain result.

## 5. Theorem / claim-scope traceability

Canonical locations are:

- `theorem_certificates/stage4a_repair_certificates.md`;
- `theorem_certificates/current_scope.md`;
- `docs/STAGE_075A_REPAIRED_CERTIFICATION.md`;
- `formal/FORMAL_VERIFICATION_CERTIFICATE_REPAIRED.md`;
- `docs/freeze_repaired/PROPOSITION_SCOPE_REGISTER.md`;
- `docs/freeze_repaired/VERIFICATION_REGISTER.md`;
- `docs/freeze_repaired/WELFARE_BENCHMARK_REGISTER.md`;
- `docs/freeze_repaired/CONTRIBUTION_REGISTER.md`.

Headline paper statements must trace to these artifacts. Lean is described only as targeted proof-critical-core verification, not full-game certification.

## 6. Environment / dependencies

- Python CI: 3.12;
- Python dependency: `sympy==1.14.0`;
- Lean: 4.33.1;
- mathlib: v4.33.1, repaired formal certificate records resolved revision `0df444a360eaa60ab8c11dca51a86af692955474`;
- LaTeX: `latexmk` plus TeX Live recommended/extra/pictures and `lmodern`.

Lean and mathlib are pinned by `lean-toolchain` and `lakefile.lean`.

## 7. Figure / table pipeline

`scripts/generate_outputs.py` deterministically regenerates:

- `figures/threshold_phase.tex`;
- `tables/baseline_example.tex`.

Generated values come from repository source and must not be hand-edited. Any repaired-`R+` annotation added in Stage 10 must be sourced from the frozen registers or verification scripts rather than manual arithmetic.

## 8. CI / local-equivalent gate

The repaired Stage-8 closeout already established that the rebased integrity gate, Python regressions, Lean build, placeholder audit, LaTeX build, generated artifacts, and artifact upload can pass together. Stage-9 closeout requires the same two workflow families to remain green on the Stage-9 head.

A green build is infrastructure evidence only; it does not expand the frozen theorem scope.

## 9. Provenance locations

- repaired theory freeze: `docs/STAGE_08_THEORY_FREEZE.md`;
- repaired model/registers: `docs/freeze_repaired/`;
- change control: `docs/CHANGE_CONTROL.md`;
- reproducibility guide: `docs/REPRODUCIBILITY.md`;
- Stage-11B regression provenance: `docs/STAGE_11B_ASTRA_REFEREE_AUDIT.md` and `verification/stage11b_astra_independent_audit.py`;
- project/status SSOT: `ryotamatsuki/economic-theory-research-portfolio#30`.

## 10. Remaining blockers

No reproducibility blocker remains for Stage 10.

The existing pre-repair manuscript section prose is not re-certified by Stage 9 merely because it compiles. Stage 10 must revise the exposition against the repaired freeze before any manuscript-closeout/referee claim can be inherited.

## 11. Exact Stage-10 writing contract

Stage 10 is authorized only under all of the following constraints:

1. `docs/STAGE_08_THEORY_FREEZE.md` and `docs/freeze_repaired/` are authoritative;
2. the manuscript title is **Dynamic Tariff Choice for Generative AI: Integration, Commitment, and Welfare**;
3. the weak-participation convention at zero continuation surplus must be explicit wherever the binding L participation constraint is used;
4. provider continuation play must be described as global both-served / H-only / no-service comparison, not as an assumed both-served branch;
5. T1–T3 must be stated only for the quadratic baseline on strict `R+`, with `h_0<h_M<h_F` and the complete candidate interval `[h_0,h_F]` visible where relevant;
6. the `23/10` H-only counterexample must remain an explicit guard against global/all-positive-parameter wording;
7. arbitrary strict concavity and non-Uniform-CDF theorem claims are prohibited; common-curvature nonquadratic results are numerical robustness only;
8. W1 remains fixed-installed-base only; no global endogenous-welfare ranking may be inferred;
9. Lean/formal verification must be described as proof-critical-core only, with weak participation, full continuation optimization, the complete atomless game, mixed-existence proof, endogenous welfare comparison, and institutional interpretation outside full formal coverage;
10. all generated numerical objects must come from repository scripts when feasible;
11. literature metadata and institutional facts must be source-verified before citation;
12. pre-repair Stage-10 wording has no inherited certification: repaired Stage 10 must independently satisfy scope/integrity/build gates;
13. any theory change triggers `docs/CHANGE_CONTROL.md` rollback rather than being hidden in exposition;
14. `verify` and `reproducibility` workflows must remain green at Stage-10 closeout.

## Final routing

**REPRODUCIBILITY BASELINE READY — GO TO STAGE 10 PAPER BUILD / REPAIR.**
