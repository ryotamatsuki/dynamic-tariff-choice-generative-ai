"""Stage 9 repository-integrity checks against the Stage 8 freeze."""
from __future__ import annotations

from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
FREEZE_SHA = "2597e82044ec94a58fad033227ea415e64af8c6d"

REQUIRED = [
    "docs/STAGE_08_THEORY_FREEZE.md",
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
]


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
    assert "arbitrary concave demand" in scope
    assert "23/10" in verification
    assert "PROOF-CRITICAL CORE" in formal


def main() -> None:
    require_paths()
    require_freeze_ancestor()
    require_scope_guards()
    print("repository integrity checks: PASS")


if __name__ == "__main__":
    main()
