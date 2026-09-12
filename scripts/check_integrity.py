"""Repository-integrity checks against the Stage 8 freeze and Stage 10 manuscript."""
from __future__ import annotations

from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
FREEZE_SHA = "2597e82044ec94a58fad033227ea415e64af8c6d"

REQUIRED = [
    "docs/STAGE_08_THEORY_FREEZE.md",
    "docs/STAGE_09_REPRODUCIBILITY_SETUP.md",
    "docs/STAGE_10_EXPOSITION_MAP.md",
    "docs/STAGE_10_SOURCE_VERIFICATION.md",
    "docs/freeze/MODEL_REGISTER.md",
    "docs/freeze/PROPOSITION_SCOPE_REGISTER.md",
    "docs/freeze/WELFARE_BENCHMARK_REGISTER.md",
    "docs/freeze/VERIFICATION_REGISTER.md",
    "docs/freeze/CONTRIBUTION_REGISTER.md",
    "docs/CHANGE_CONTROL.md",
    "theorem_certificates/current_scope.md",
    "formal/FORMAL_VERIFICATION_CERTIFICATE.md",
    "formal/DynamicTariffFormal.lean",
    "verification/baseline_checks.py",
    "verification/robustness_checks.py",
    "scripts/generate_outputs.py",
    "tests/test_regressions.py",
    "paper/main.tex",
    "references/references.bib",
    "references/frontier.bib",
    "references/extra.bib",
    "sections/00_abstract.tex",
    "sections/01_introduction.tex",
    "sections/02_model.tex",
    "sections/03_equilibrium.tex",
    "sections/04_welfare.tex",
    "sections/05_robustness.tex",
    "sections/06_institutional.tex",
    "sections/07_related_literature.tex",
    "sections/08_discussion.tex",
    "sections/09_conclusion.tex",
    "sections/10_appendix.tex",
]

MANUSCRIPT_SECTIONS = [path for path in REQUIRED if path.startswith("sections/")]


def require_paths() -> None:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    assert not missing, f"missing reproducibility paths: {missing}"


def require_freeze_ancestor() -> None:
    result = subprocess.run(
        ["git", "merge-base", "--is-ancestor", FREEZE_SHA, "HEAD"],
        cwd=ROOT,
        check=False,
    )
    assert result.returncode == 0, "Stage 8 freeze SHA is not an ancestor of HEAD"


def require_scope_guards() -> None:
    scope = (ROOT / "docs/freeze/PROPOSITION_SCOPE_REGISTER.md").read_text(encoding="utf-8")
    verification = (ROOT / "docs/freeze/VERIFICATION_REGISTER.md").read_text(encoding="utf-8")
    formal = (ROOT / "formal/FORMAL_VERIFICATION_CERTIFICATE.md").read_text(encoding="utf-8")
    manuscript = "\n".join((ROOT / path).read_text(encoding="utf-8") for path in MANUSCRIPT_SECTIONS)
    assert "arbitrary concave demand" in scope
    assert "23/10" in verification
    assert "proof-critical" in formal.lower()
    assert "Stage 10 writing placeholder" not in manuscript
    assert "23/10" in manuscript
    assert "arbitrary concave demand" in manuscript
    assert "label{prop:T1}" in manuscript
    assert "label{prop:T2}" in manuscript
    assert "label{prop:T3}" in manuscript
    assert "label{prop:W1}" in manuscript
    assert "label{fig:threshold-phase}" in manuscript
    assert "label{tab:baseline-example}" in manuscript


def main() -> None:
    require_paths()
    require_freeze_ancestor()
    require_scope_guards()
    print("repository integrity checks: PASS")


if __name__ == "__main__":
    main()
