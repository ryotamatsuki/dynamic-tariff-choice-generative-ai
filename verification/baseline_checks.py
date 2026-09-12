"""Exact/symbolic regression checks for the frozen baseline model.

These checks reproduce proof-critical algebra used by Stage 4R/4A/7.5A.
They are regression tests, not a substitute for the independent Stage-4A audit.
"""

import sympy as sp


def main() -> None:
    l, h, c, d = sp.symbols("l h c d", positive=True)

    phi = (l + h) / 2 * (c + d * h / (l + h)) ** 2
    phi_h = sp.factor(sp.diff(phi, h))
    expected = (
        (c * (l + h) + d * h)
        * (c * (l + h) + d * h + 2 * d * l)
        / (2 * (l + h) ** 2)
    )
    assert sp.simplify(phi_h - expected) == 0

    # Exact open-set example from Stage 4R/4A.
    aL = sp.Rational(4)
    aH = sp.Rational(5)
    c0 = sp.Rational(1)
    bL = sp.Rational(16, 5)
    KL = sp.Rational(4)
    bH = sp.Rational(1, 2)
    KH = sp.Rational(8)
    mu = sp.Rational(13, 10)

    l0 = sp.simplify(bL / KL)
    d0 = aH - aL
    RF = sp.simplify((aH**2 - aL**2) / 2)
    hF = sp.simplify((bH + RF) / KH)
    assert l0 == sp.Rational(4, 5)
    assert hF == sp.Rational(5, 8)

    x = sp.symbols("x", real=True)
    p = c0 + d0 * x / (l0 + x)
    roots = sp.solve(sp.Eq(KH * x, bH + RF - d0 * p), x)
    hM = [r for r in roots if sp.N(r) > 0][0]
    expected_hM = (sp.sqrt(2849) - 17) / 80
    assert sp.simplify(hM - expected_hM) == 0
    assert bool(sp.N(hM) < sp.N(hF))

    phi0 = sp.simplify((l0 + x) / 2 * (c0 + d0 * x / (l0 + x)) ** 2)
    muM = sp.simplify(phi0.subs(x, hM))
    muF = sp.simplify(phi0.subs(x, hF))
    assert bool(sp.N(muM) < sp.N(mu) < sp.N(muF))

    hstar_roots = sp.solve(sp.Eq(phi0, mu), x)
    hstar = [r for r in hstar_roots if sp.N(r) > 0][0]
    expected_hstar = 3 * (sp.sqrt(65) - 1) / 40
    assert sp.simplify(hstar - expected_hstar) == 0
    assert bool(sp.N(hM) < sp.N(hstar) < sp.N(hF))

    pstar = sp.simplify((c0 + d0 * x / (l0 + x)).subs(x, hstar))
    rho = sp.simplify(KH * (hF - hstar) / (d0 * pstar))
    assert bool(0 < sp.N(rho) < 1)

    # Permanent scope guard: outside regular region R, H-only flat can dominate.
    l_bad = sp.Rational(1, 10)
    h_bad = sp.Rational(3, 5)
    both_flat = sp.simplify(
        (l_bad + h_bad) * aL**2 / 2
        - c0 * (l_bad * aL + h_bad * aH)
    )
    h_only_flat = sp.simplify(h_bad * aH**2 / 2 - c0 * h_bad * aH)
    assert sp.simplify(h_only_flat - both_flat) == sp.Rational(23, 10)
    assert h_only_flat > both_flat

    print("baseline symbolic checks: PASS")
    print(f"h_M={sp.N(hM, 12)} h_F={sp.N(hF, 12)}")
    print(f"mu_M={sp.N(muM, 12)} mu={sp.N(mu, 12)} mu_F={sp.N(muF, 12)}")
    print(f"h*={sp.N(hstar, 12)} p*={sp.N(pstar, 12)} rho*={sp.N(rho, 12)}")
    print(f"scope counterexample H-only advantage={h_only_flat - both_flat}")


if __name__ == "__main__":
    main()
