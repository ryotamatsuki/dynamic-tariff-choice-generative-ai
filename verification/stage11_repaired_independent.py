from __future__ import annotations

"""Independent repaired Stage-11 referee attack checks.

This script deliberately reconstructs the highest-risk claims from primitives rather
than importing the production solver.  It is not a proof of the complete game; it
provides reproducible adversarial checks that complement the analytic certificates.
"""

import math

import sympy as sp


def assert_close(x: float, y: float, tol: float = 2e-4) -> None:
    if not math.isclose(x, y, rel_tol=tol, abs_tol=tol):
        raise AssertionError(f"{x} != {y} within {tol}")


def baseline_exact_checks() -> None:
    aL, aH, c = sp.Rational(4), sp.Rational(5), sp.Rational(1)
    bL, KL = sp.Rational(16, 5), sp.Rational(4)
    bH, KH = sp.Rational(1, 2), sp.Rational(8)
    l = sp.simplify(bL / KL)
    d = aH - aL
    RF = sp.simplify((aH**2 - aL**2) / 2)
    h0 = sp.simplify(bH / KH)
    hF = sp.simplify((bH + RF) / KH)

    h = sp.symbols("h", positive=True)
    pstar = c + d * h / (l + h)
    fixed_point = sp.Eq(KH * h, bH + RF - d * pstar)
    positive_roots = [r for r in sp.solve(fixed_point, h) if sp.N(r) > 0]
    assert len(positive_roots) == 1
    hM = sp.simplify(positive_roots[0])
    assert sp.simplify(hM - h0) > 0
    assert sp.simplify(hF - hM) > 0

    phi = sp.simplify((l + h) * pstar**2 / 2)
    muM = sp.simplify(phi.subs(h, hM))
    muF = sp.simplify(phi.subs(h, hF))
    assert sp.N(muM) < sp.Rational(13, 10) < sp.N(muF)

    assert h0 == sp.Rational(1, 16)
    assert hF == sp.Rational(5, 8)
    assert hM == (-sp.Rational(17) + sp.sqrt(2849)) / 80
    assert muM == -sp.Rational(461, 200) + sp.Rational(13, 200) * sp.sqrt(2849)
    assert muF == sp.Rational(1681, 1140)


def endpoint_propagation_identities() -> None:
    aL, c, d, l, h = sp.symbols("aL c d l h", positive=True)
    aH = aL + d
    p = c + d * h / (l + h)

    flat_both = (l + h) * aL**2 / 2 - c * (l * aL + h * aH)
    flat_h_only = h * aH**2 / 2 - c * h * aH
    d_flat_gap = sp.factor(sp.diff(flat_both - flat_h_only, h))
    assert sp.simplify(d_flat_gap + d * (2 * aL + d) / 2) == 0

    metered_both = (
        (l + h) * (aL - p) ** 2 / 2
        + (p - c) * (l * (aL - p) + h * (aH - p))
    )
    metered_h_only = h * (aH - c) ** 2 / 2
    d_metered_gap = sp.factor(sp.diff(metered_both - metered_h_only, h))
    target = -d * (2 * (aL - c) * (h + l) ** 2 + d * l**2) / (2 * (h + l) ** 2)
    assert sp.simplify(d_metered_gap - target) == 0


def direct_continuation_attack() -> None:
    """Enumerate participation regimes and a dense finite price-deviation grid."""
    aL, aH, c = 4.0, 5.0, 1.0
    l = 0.8
    d = aH - aL
    h0, hF = 1.0 / 16.0, 5.0 / 8.0
    hM = (-17.0 + math.sqrt(2849.0)) / 80.0
    states = [h0, hM, (hM + hF) / 2.0, hF]

    def s(a: float, p: float) -> float:
        return max(a - p, 0.0) ** 2 / 2.0

    def q(a: float, p: float) -> float:
        return max(a - p, 0.0)

    for h in states:
        flat_both = (l + h) * s(aL, 0.0) - c * (l * q(aL, 0.0) + h * q(aH, 0.0))
        flat_h = h * (s(aH, 0.0) - c * q(aH, 0.0))
        assert flat_both > max(flat_h, 0.0)

        pstar = c + d * h / (l + h)
        both_star = (
            (l + h) * s(aL, pstar)
            + (pstar - c) * (l * q(aL, pstar) + h * q(aH, pstar))
        )
        h_only_global = h * (aH - c) ** 2 / 2.0
        assert 0.0 < pstar < aL
        assert both_star > max(h_only_global, 0.0)

        # Search the full economically relevant p-range, deliberately crossing
        # p=a_L where the low-use active set disappears.
        best = -1e100
        best_p = None
        n = 25000
        for i in range(1, n + 1):
            p = aH * i / n
            ql, qh = q(aL, p), q(aH, p)
            both = (l + h) * s(aL, p) + (p - c) * (l * ql + h * qh)
            h_only = h * (s(aH, p) + (p - c) * qh)
            value = max(both, h_only, 0.0)
            if value > best:
                best, best_p = value, p
        assert_close(best, both_star)
        assert abs(best_p - pstar) < 5e-4


def strict_concavity_scope_attack() -> None:
    """An admissible nonbaseline counterexample to arbitrary-concavity scope."""
    p = sp.symbols("p", real=True)
    aL, aH = sp.Rational(3), sp.Rational(9, 2)
    rL, rH = sp.Rational(1), sp.Rational(2)
    c = sp.Rational(1)
    l, h = sp.Rational(4, 5), sp.Rational(1, 5)

    qL = (aL - p) / rL
    qH = (aH - p) / rH
    SL = (aL - p) ** 2 / (2 * rL)
    SH = (aH - p) ** 2 / (2 * rH)
    both = sp.expand((l + h) * SL + (p - c) * (l * qL + h * qH))
    pstar = sp.solve(sp.Eq(sp.diff(both, p), 0), p)[0]

    rent_flat = sp.simplify(SH.subs(p, 0) - SL.subs(p, 0))
    rent_metered = sp.simplify(SH.subs(p, pstar) - SL.subs(p, pstar))
    flat_both = sp.simplify(both.subs(p, 0))
    metered_both = sp.simplify(both.subs(p, pstar))
    h_only_metered = sp.simplify(h * (aH - c) ** 2 / (2 * rH))

    assert pstar == sp.Rational(15, 16)
    assert rent_flat == sp.Rational(9, 16)
    assert rent_metered == sp.Rational(1071, 1024)
    assert rent_metered > rent_flat
    assert flat_both == sp.Rational(33, 20)
    assert metered_both == sp.Rational(1281, 640)
    assert h_only_metered == sp.Rational(49, 80)
    assert metered_both > h_only_metered


def permanent_scope_guard() -> None:
    aL, aH, c = sp.Rational(4), sp.Rational(5), sp.Rational(1)
    l, h = sp.Rational(1, 10), sp.Rational(3, 5)
    flat_both = (l + h) * aL**2 / 2 - c * (l * aL + h * aH)
    flat_h = h * aH**2 / 2 - c * h * aH
    assert sp.simplify(flat_h - flat_both) == sp.Rational(23, 10)


if __name__ == "__main__":
    baseline_exact_checks()
    endpoint_propagation_identities()
    direct_continuation_attack()
    strict_concavity_scope_attack()
    permanent_scope_guard()
    print("STAGE 11 REPAIRED INDEPENDENT CHECKS: PASS")
