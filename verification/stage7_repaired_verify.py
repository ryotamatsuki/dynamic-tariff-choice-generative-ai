#!/usr/bin/env python3
"""Stage 7 welfare/generality regression checks for the repaired R+ model.

This file verifies exact welfare identities, the fixed-installed-base
private/social metering wedge, and sign-indeterminacy of the restricted
architecture-commitment welfare comparison using examples that satisfy the
repaired strict R+ conditions.
"""

from __future__ import annotations

import sympy as sp


# ---------------------------------------------------------------------------
# Exact symbolic identities
# ---------------------------------------------------------------------------
a, c, p, l, h, d, mu = sp.symbols("a c p l h d mu", positive=True)
q = a - p
omega = sp.expand(a * q - q**2 / 2 - c * q)
omega_alt = sp.expand((a - c) ** 2 / 2 - (p - c) ** 2 / 2)
assert sp.simplify(omega - omega_alt) == 0

K, B, k = sp.symbols("K B k", positive=True)
CS = sp.integrate(B - k, (k, 0, B)) / K
assert sp.simplify(CS - B**2 / (2 * K)) == 0

n = l + h
x = h / n
pstar = c + d * x
mu_private = sp.simplify(n * pstar**2 / 2)
mu_social = sp.simplify(n * (c**2 - d**2 * x**2) / 2)
assert sp.simplify(mu_private - mu_social - d * h * pstar) == 0


def bisect_root(f, lo: float, hi: float, tol: float = 1e-13, iters: int = 300) -> float:
    flo, fhi = f(lo), f(hi)
    if abs(flo) <= tol:
        return lo
    if abs(fhi) <= tol:
        return hi
    assert flo * fhi < 0, (flo, fhi)
    for _ in range(iters):
        mid = (lo + hi) / 2.0
        fm = f(mid)
        if abs(fm) <= tol or hi - lo <= tol:
            return mid
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2.0


# ---------------------------------------------------------------------------
# Repaired strict R+ helpers
# ---------------------------------------------------------------------------
def metrics(aL: float, aH: float, c0: float,
            bL: float, KL: float, bH: float, KH: float):
    dd = aH - aL
    ll = bL / KL
    RF = (aH * aH - aL * aL) / 2.0
    h0 = bH / KH
    hF = (bH + RF) / KH

    def pp(hh: float) -> float:
        return c0 + dd * hh / (ll + hh)

    def pi_flat_both(hh: float) -> float:
        return (ll + hh) * aL * aL / 2.0 - c0 * (ll * aL + hh * aH)

    def pi_flat_h(hh: float) -> float:
        return hh * aH * aH / 2.0 - c0 * hh * aH

    def pi_meter_both(hh: float) -> float:
        px = pp(hh)
        return ((ll + hh) * (aL - px) ** 2 / 2.0
                + (px - c0) * (ll * (aL - px) + hh * (aH - px)))

    def pi_meter_h(hh: float) -> float:
        return hh * (aH - c0) ** 2 / 2.0

    rplus_checks = {
        "basic": 0 < c0 < aL < aH and KL > 0 and KH > 0 and bL > 0 and bH > 0,
        "l-interior": 0 < ll < 1,
        "dc-cutoff": dd * c0 < bH + RF < KH,
        "meter-price-interior": pp(hF) < aL,
        "flat-positive-h0": pi_flat_both(h0) > 0,
        "flat-positive-hF": pi_flat_both(hF) > 0,
        "flat-both-over-H": pi_flat_both(hF) > pi_flat_h(hF),
        "meter-both-over-H": pi_meter_both(hF) > pi_meter_h(hF),
    }
    assert all(rplus_checks.values()), rplus_checks

    def meter_fp(hh: float) -> float:
        return KH * hh - (bH + RF - dd * pp(hh))

    hM = bisect_root(meter_fp, h0, hF)
    assert h0 < hM < hF

    def om(aa: float, px: float) -> float:
        return (aa - c0) ** 2 / 2.0 - (px - c0) ** 2 / 2.0

    def welfare0(hh: float, px: float) -> float:
        return (bL * ll + bH * hh - KL * ll * ll / 2.0 - KH * hh * hh / 2.0
                + ll * om(aL, px) + hh * om(aH, px))

    mu_commit_social = welfare0(hM, pp(hM)) - welfare0(hF, 0.0)

    return {
        "l": ll,
        "h0": h0,
        "hM": hM,
        "hF": hF,
        "pM": pp(hM),
        "mu_commit_social": mu_commit_social,
        "flat_margin_hF": pi_flat_both(hF) - pi_flat_h(hF),
        "meter_margin_hF": pi_meter_both(hF) - pi_meter_h(hF),
    }


# Same primitives except K_H. Both examples satisfy repaired strict R+,
# but the restricted architecture-commitment welfare ranking reverses.
pos = metrics(2.5, 3.0, 0.5, 1.0, 4.0, 0.5, 16.0)
neg = metrics(2.5, 3.0, 0.5, 1.0, 4.0, 0.5, 8.0)
assert pos["mu_commit_social"] > 0
assert neg["mu_commit_social"] < 0

# Certified baseline remains inside repaired R+ and retains the headline ordering.
baseline = metrics(4.0, 5.0, 1.0, 16.0 / 5.0, 4.0, 0.5, 8.0)
assert abs(baseline["h0"] - 1.0 / 16.0) < 1e-12
assert abs(baseline["hF"] - 5.0 / 8.0) < 1e-12
assert baseline["h0"] < baseline["hM"] < baseline["hF"]

print("Stage 7 repaired welfare verification PASS")
print("positive R+ welfare threshold:", pos["mu_commit_social"])
print("negative R+ welfare threshold:", neg["mu_commit_social"])
print("baseline h0,hM,hF:", baseline["h0"], baseline["hM"], baseline["hF"])

# Stage 7.5A is a scope gate rather than a new mechanism stage. Importing this
# dedicated audit makes the existing CI Python gate execute its exact symbolic
# scope checks without changing the project's dependency set.
import stage075a_scope_verify  # noqa: E402,F401
