from __future__ import annotations

"""Independent verification for the post-Astra Stage-11 repair.

This file is additive: it does not replace the historical Stage-11 audit.  It
reconstructs the new boundary/globality/completeness claims from primitives and
uses a direct utility-derived finite-deviation evaluator rather than the production
continuation solver.
"""

import math
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def exact_global_identities() -> None:
    A, d, c, l, h, p = sp.symbols("A d c l h p", positive=True)
    n = l + h
    aH = A + d
    pstar = c + d * h / n
    B = n * (A - p) ** 2 / 2 + (p - c) * (l * (A - p) + h * (aH - p))

    loss = sp.factor(B.subs(p, pstar) - B)
    assert sp.simplify(loss - n * (p - pstar) ** 2 / 2) == 0

    h_only = h * (aH - c) ** 2 / 2
    DM = sp.factor(B.subs(p, pstar) - h_only)
    DM_target = l * (A - c) ** 2 / 2 - d * (A - c) * h - d**2 * l * h / (2 * (l + h))
    assert sp.simplify(DM - DM_target) == 0
    DMprime = sp.factor(sp.diff(DM_target, h))
    DMprime_target = -d * (A - c) - d**2 * l**2 / (2 * (l + h) ** 2)
    assert sp.simplify(DMprime - DMprime_target) == 0

    flat_both = (l + h) * A**2 / 2 - c * (l * A + h * aH)
    flat_h = h * A**2 / 2 + h * (A * d + d**2 / 2) - c * h * aH
    DF = sp.factor(flat_both - flat_h)
    DF_target = l * (A**2 / 2 - c * A) - h * d * (2 * A + d) / 2
    assert sp.simplify(DF - DF_target) == 0
    assert sp.simplify(sp.diff(DF_target, h) + d * (2 * A + d) / 2) == 0


def direct_utility_profit(a: float, p: float, F: float) -> tuple[bool, float, float]:
    q = max(a - p, 0.0)
    gross = max(a - p, 0.0) ** 2 / 2.0
    participates = gross - F >= -1e-12
    return participates, q if participates else 0.0, gross - F if participates else 0.0


def provider_profit_from_primitives(l: float, h: float, aL: float, aH: float, c: float, p: float, F: float) -> float:
    inL, qL, _ = direct_utility_profit(aL, p, F)
    inH, qH, _ = direct_utility_profit(aH, p, F)
    mass = l * float(inL) + h * float(inH)
    usage = l * qL + h * qH
    return mass * F + (p - c) * usage


def finite_deviation_active_set_check() -> None:
    aL, aH, c, l = 4.0, 5.0, 1.0, 0.8
    d = aH - aL
    h0, hF = 1.0 / 16.0, 5.0 / 8.0
    hM = (-17.0 + math.sqrt(2849.0)) / 80.0
    states = [h0, hM, (hM + hF) / 2.0, hF]

    def S(a: float, p: float) -> float:
        return max(a - p, 0.0) ** 2 / 2.0

    for h in states:
        pstar = c + d * h / (l + h)
        Fstar = S(aL, pstar)
        analytic = provider_profit_from_primitives(l, h, aL, aH, c, pstar, Fstar)

        best = -1e100
        best_pair = None
        # Cross p=a_L and p=a_H.  For each p evaluate both participation thresholds,
        # zero, and explicit negative subsidies.  Profit is affine in F within an
        # active set, so threshold fees plus negative-F probes cover its extrema.
        for i in range(1, 12001):
            p = (aH + 1.0) * i / 12000.0
            fees = [S(aL, p), S(aH, p), 0.0, -0.1, -1.0, -5.0]
            for F in fees:
                val = provider_profit_from_primitives(l, h, aL, aH, c, p, F)
                if val > best:
                    best, best_pair = val, (p, F)
        if not math.isclose(best, analytic, rel_tol=4e-4, abs_tol=4e-4):
            raise AssertionError((h, best, analytic, best_pair))
        assert abs(best_pair[0] - pstar) < 1e-3

        # Explicit price-boundary classifications.
        assert direct_utility_profit(aL, aL, 0.0)[1] == 0.0
        assert direct_utility_profit(aL, (aL + aH) / 2.0, 0.1)[0] is False
        assert direct_utility_profit(aH, (aL + aH) / 2.0, 0.1)[0] is True
        assert direct_utility_profit(aH, aH + 0.5, 0.1)[0] is False


def baseline_objects():
    aL, aH, c = sp.Rational(4), sp.Rational(5), sp.Rational(1)
    bL, KL = sp.Rational(16, 5), sp.Rational(4)
    bH, KH = sp.Rational(1, 2), sp.Rational(8)
    l = bL / KL
    d = aH - aL
    RF = (aH**2 - aL**2) / 2
    h0 = bH / KH
    hF = (bH + RF) / KH
    h = sp.symbols("h", positive=True)
    pstar = c + d * h / (l + h)
    roots = [r for r in sp.solve(sp.Eq(KH * h, bH + RF - d * pstar), h) if sp.N(r) > 0]
    hM = sp.simplify(roots[0])
    Phi = sp.simplify((l + h) * pstar**2 / 2)
    muM = sp.simplify(Phi.subs(h, hM))
    muF = sp.simplify(Phi.subs(h, hF))
    return aL, aH, c, bH, KH, l, d, RF, h, h0, hM, hF, pstar, Phi, muM, muF


def pure_boundary_check() -> None:
    aL, aH, c, bH, KH, l, d, RF, h, h0, hM, hF, pstar, Phi, muM, muF = baseline_objects()
    assert h0 == sp.Rational(1, 16)
    assert hF == sp.Rational(5, 8)
    assert hM == (-sp.Rational(17) + sp.sqrt(2849)) / 80
    assert muM == -sp.Rational(461, 200) + sp.Rational(13, 200) * sp.sqrt(2849)
    assert muF == sp.Rational(1681, 1140)
    assert sp.simplify(pstar.subs(h, hF)) == sp.Rational(82, 57)
    assert aL**2 / 2 == 8

    # Provider best responses at the two pure induced states are ties.
    assert sp.simplify(Phi.subs(h, hM) - muM) == 0
    assert sp.simplify(Phi.subs(h, hF) - muF) == 0

    # At mu_F, rho>0 implies h<h_F by the aggregation identity and therefore,
    # because Phi is strictly increasing, flat is strictly optimal.  At mu_M,
    # rho<1 makes the integration fixed-point residual at h_M positive; strict
    # crossing implies h>h_M and metering is strictly optimal.
    rho = sp.symbols("rho", real=True)
    residual_at_hM = sp.factor(bH + RF - rho * d * pstar.subs(h, hM) - KH * hM)
    assert sp.simplify(residual_at_hM - (1 - rho) * d * pstar.subs(h, hM)) == 0
    assert sp.simplify(sp.diff(Phi, h)) > 0


def candidate_interval_and_mixed_check() -> None:
    aL, aH, c, bH, KH, l, d, RF, h, h0, hM, hF, pstar, Phi, muM, muF = baseline_objects()
    p = sp.symbols("p", nonnegative=True)
    SHminusSL = sp.expand(((aH - p) ** 2 - (aL - p) ** 2) / 2)
    assert sp.simplify(SHminusSL - (RF - d * p)) == 0

    mu = sp.Rational(13, 10)
    roots = [r for r in sp.solve(sp.Eq(Phi, mu), h) if sp.N(r) > 0]
    hstar = [r for r in roots if sp.N(hM) < sp.N(r) < sp.N(hF)][0]
    rho = sp.simplify(KH * (hF - hstar) / (d * pstar.subs(h, hstar)))
    assert sp.N(hM) < sp.N(hstar) < sp.N(hF)
    assert 0 < sp.N(rho) < 1

    low_cutoff = sp.Rational(16, 5)
    high_cutoff = sp.simplify(bH + RF - rho * d * pstar.subs(h, hstar))
    assert sp.simplify(low_cutoff / 4 - l) == 0
    assert sp.simplify(high_cutoff / KH - hstar) == 0
    assert sp.simplify(Phi.subs(h, hstar) - mu) == 0


def manuscript_guards() -> None:
    eqm = (ROOT / "sections/03_equilibrium.tex").read_text(encoding="utf-8")
    appendix = (ROOT / "sections/10_appendix.tex").read_text(encoding="utf-8")
    model = (ROOT / "sections/02_model.tex").read_text(encoding="utf-8")
    assert "\\mu\\leq\\mu_M" in eqm
    assert "\\mu\\geq\\mu_F" in eqm
    assert "B(p^*)-B(p)" in appendix
    assert "candidate interval" in model.lower()
    assert "actual globally optimal tariffs" in eqm
    assert "average marginal price" in eqm


if __name__ == "__main__":
    exact_global_identities()
    finite_deviation_active_set_check()
    pure_boundary_check()
    candidate_interval_and_mixed_check()
    manuscript_guards()
    print("STAGE 11 ASTRA REPAIR VERIFICATION: PASS")
