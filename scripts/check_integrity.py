"""Repository-integrity checks against the repaired Stage 8 freeze.

Manuscript files are retained for provenance until Stage 9/10 are rerun; this gate
certifies the current theory/reproducibility inputs, not the stale manuscript prose.
"""
from __future__ import annotations

from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]
FREEZE_SHA = "c9e43c99d9deb56bad52637024b9dab7b3673aee"

REQUIRED = [
    "docs/STAGE_08_THEORY_FREEZE.md",
    "docs/freeze_repaired/MODEL_REGISTER.md",
    "docs/freeze_repaired/PROPOSITION_SCOPE_REGISTER.md",
    "docs/freeze_repaired/WELFARE_BENCHMARK_REGISTER.md",
    "docs/freeze_repaired/VERIFICATION_REGISTER.md",
    "docs/freeze_repaired/CONTRIBUTION_REGISTER.md",
    "docs/CHANGE_CONTROL.md",
    "theorem_certificates/current_scope.md",
    "theorem_certificates/stage4a_repair_certificates.md",
    "docs/STAGE_075A_REPAIRED_CERTIFICATION.md",
    "formal/FORMAL_VERIFICATION_CERTIFICATE_REPAIRED.md",
    "formal/DynamicTariffFormal.lean",
    "verification/baseline_checks.py",
    "verification/stage4a_repair_independent.py",
    "verification/stage7_repaired_verify.py",
    "verification/stage075a_scope_verify.py",
    "verification/stage11b_astra_independent_audit.py",
    "paper/main.tex",
]


def require_paths() -> None:
    missing = [path for path in REQUIRED if not (ROOT / path).exists()]
    assert not missing, f"missing repaired-freeze paths: {missing}"


def require_freeze_ancestor() -> None:
    result = subprocess.run(
        ["git", "merge-base", "--is-ancestor", FREEZE_SHA, "HEAD"],
        cwd=ROOT,
        check=False,
    )
    assert result.returncode == 0, "repaired Stage 8 freeze declaration is not an ancestor of HEAD"


def require_scope_guards() -> None:
    scope = (ROOT / "docs/freeze_repaired/PROPOSITION_SCOPE_REGISTER.md").read_text(encoding="utf-8")
    verification = (ROOT / "docs/freeze_repaired/VERIFICATION_REGISTER.md").read_text(encoding="utf-8")
    formal = (ROOT / "formal/FORMAL_VERIFICATION_CERTIFICATE_REPAIRED.md").read_text(encoding="utf-8")
    stage8 = (ROOT / "docs/STAGE_08_THEORY_FREEZE.md").read_text(encoding="utf-8")
    status = (ROOT / "STATUS.md").read_text(encoding="utf-8")

    assert "strict `R+`" in scope
    assert "arbitrary strict concavity" in scope
    assert "23/10" in verification
    assert "PROOF-CRITICAL CORE" in formal
    assert "THEORY FROZEN" in stage8
    assert "rerun/rebase Stage 9" in status


def main() -> None:
    require_paths()
    require_freeze_ancestor()
    require_scope_guards()
    print("repaired Stage 8 repository integrity checks: PASS")


if __name__ == "__main__":
    main()
