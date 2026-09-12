from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def main() -> None:
    main_tex = read("paper/main.tex")
    intro = read("sections/01_introduction_repaired.tex")
    model = read("sections/02_model.tex")
    eqm = read("sections/03_equilibrium.tex")
    welfare = read("sections/04_welfare.tex")
    robust = read("sections/05_robustness.tex")
    inst = read("sections/06_institutional.tex")
    lit = read("sections/07_related_literature_repaired.tex")
    appendix = read("sections/10_appendix.tex")
    architecture = read("docs/STAGE_10_FIGURE_TABLE_ARCHITECTURE.md")

    assert "Integration, Commitment, and Welfare" in main_tex
    assert "Model Improvement" not in main_tex
    assert "01_introduction_repaired" in main_tex
    assert "07_related_literature_repaired" in main_tex

    assert "\\mathcal R^+" in intro
    assert "\\mathcal R^+" in model
    assert "\\mathcal R^+" in eqm
    assert "\\mathcal R^+" in robust
    assert "zero continuation surplus" in model
    assert "V_F" in model and "V_M" in model
    assert "h_0<h_M<h_F" in eqm
    assert "23/10" in robust and "23/10" in appendix
    assert "fixed installed" in welfare.lower() or "fixed-installed" in welfare.lower()
    assert "not sign-definite" in welfare
    assert "numerical robustness only" in robust
    assert "does not guarantee" in robust
    assert "model interpretation" in inst.lower()
    assert "not claimed as new" in lit
    assert "threshold figure" in architecture

    print("Stage 10 manuscript scope gate: PASS")


if __name__ == "__main__":
    main()
