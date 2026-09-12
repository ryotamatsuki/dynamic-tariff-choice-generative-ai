#!/usr/bin/env python3
"""Independent Stage-4A repair certification.

No production verification module is imported. The evaluator reconstructs
quadratic continuation payoffs directly from primitives, implements the repaired
weak-participation convention, enumerates both-served / H-only / no-service
continuations, and searches the full rational-expectations candidate-state
interval.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

TOL = 1e-10


@dataclass(frozen=True)
class Par:
    aL: float
    aH: float
    c: float
    bL: float
    KL: float
    bH: float
    KH: float
    mu: float

    @property
    def d(self) -> float:
        return self.aH - self.aL

    @property
    def l(self) -> float:
        return self.bL / self.KL

    @property
    def RF(self) -> float:
        return (self.aH**2 - self.aL**2) / 2.0

    @property
    def h0(self) -> float:
        return self.bH / self.KH

    @property
    def hF(self) -> float:
        return (self.bH + self.RF) / self.KH


def q(a: float, p: float) -> float:
    return max(a - p, 0.0)


def S(a: float, p: float) -> float:
    x = max(a - p, 0.0)
    return x * x / 2.0


def both_profit(p: float, l: float, h: float, P: Par) -> float:
    # Weak participation: the L mass accepts at F=S_L(p).
    F = S(P.aL, p)
    return (l + h) * F + (p - P.c) * (
        l * q(P.aL, p) + h * q(P.aH, p)
    )


def honly_profit(p: float, h: float, P: Par) -> float:
    F = S(P.aH, p)
    return h * (F + (p - P.c) * q(P.aH, p))


def flat_candidates(l: float, h: float, P: Par) -> dict[str, float]:
    return {
        "both": both_profit(0.0, l, h, P),
        "H-only": honly_profit(0.0, h, P),
        "no-service": 0.0,
    }


def p_both_unconstrained(l: float, h: float, P: Par) -> float:
    if l + h <= 0.0:
        return 0.0
    return P.c + P.d * h / (l + h)


def meter_candidates(l: float, h: float, P: Par) -> tuple[dict[str, float], float]:
    if l + h <= 0.0:
        pb = 0.0
        both = 0.0
    else:
        # Exact constrained maximum of the both-served expression.  On the
        # repaired regular region pb<aL, so this clipping is only for off-path
        # continuation completeness.
        pb = min(p_both_unconstrained(l, h, P), P.aL)
        both = both_profit(pb, l, h, P)

    ph = P.c  # unique H-only optimum when h>0; payoff is zero when h=0.
    return {
        "both": both,
        "H-only": honly_profit(ph, h, P),
        "no-service": 0.0,
    }, pb


def argmax_dict(values: dict[str, float]) -> tuple[list[str], float]:
    best = max(values.values())
    return [k for k, v in values.items() if abs(v - best) <= 1e-9], best


def global_flat(l: float, h: float, P: Par) -> tuple[list[str], float]:
    return argmax_dict(flat_candidates(l, h, P))


def global_meter(l: float, h: float, P: Par) -> tuple[list[str], float, float]:
    values, pb = meter_candidates(l, h, P)
    acts, value = argmax_dict(values)
    return acts, value, pb


def rent_H(active: str, p: float, P: Par) -> float:
    if active == "both":
        return S(P.aH, p) - S(P.aL, p)
    if active in ("H-only", "no-service"):
        return 0.0
    raise ValueError(active)


def bisect(f, lo: float, hi: float, n: int = 250) -> float:
    flo, fhi = f(lo), f(hi)
    assert flo * fhi <= 0.0, (lo, hi, flo, fhi)
    for _ in range(n):
        mid = (lo + hi) / 2.0
        fm = f(mid)
        if abs(fm) < 1e-14 or hi - lo < 1e-14:
            return mid
        if flo * fm <= 0.0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2.0


def scan_roots(f, lo: float, hi: float, N: int = 5000) -> list[float]:
    roots: list[float] = []
    x0, y0 = lo, f(lo)
    for i in range(1, N + 1):
        x1 = lo + (hi - lo) * i / N
        y1 = f(x1)
        if abs(y1) < 1e-9:
            r = x1
        elif y0 * y1 < 0.0:
            r = bisect(f, x0, x1)
        else:
            r = None
        if r is not None and all(abs(r - z) > 1e-6 for z in roots):
            roots.append(r)
        x0, y0 = x1, y1
    return roots


def main() -> None:
    P = Par(4.0, 5.0, 1.0, 16 / 5, 4.0, 0.5, 8.0, 1.3)

    assert abs(P.l - 0.8) < TOL
    assert abs(P.h0 - 1 / 16) < TOL
    assert abs(P.hF - 5 / 8) < TOL

    # Repaired R+: every rational-expectations H state lies in [h0,hF].
    assert P.c * P.d < P.bH + P.RF < P.KH
    assert p_both_unconstrained(P.l, P.hF, P) < P.aL

    # Strict active-set dominance on the complete candidate-state interval.
    for i in range(1001):
        h = P.h0 + (P.hF - P.h0) * i / 1000
        af, _ = global_flat(P.l, h, P)
        am, _, pm = global_meter(P.l, h, P)
        assert af == ["both"], (h, af, flat_candidates(P.l, h, P))
        assert am == ["both"], (h, am, meter_candidates(P.l, h, P)[0])
        assert pm < P.aL + 1e-12

    # Architecture-specific integration maps, using the global direct-payoff
    # continuation rather than production formulas.
    def rF(h: float) -> float:
        acts, _ = global_flat(P.l, h, P)
        assert acts == ["both"]
        return rent_H("both", 0.0, P)

    def rM(h: float) -> float:
        acts, _, pm = global_meter(P.l, h, P)
        assert acts == ["both"]
        return rent_H("both", pm, P)

    rootsF = scan_roots(
        lambda h: (P.bH + rF(h)) / P.KH - h, P.h0, P.hF
    )
    rootsM = scan_roots(
        lambda h: (P.bH + rM(h)) / P.KH - h, P.h0, P.hF
    )
    assert len(rootsF) == 1, rootsF
    assert len(rootsM) == 1, rootsM

    hF = rootsF[0]
    hM = rootsM[0]
    assert abs(hF - P.hF) < 1e-7
    assert P.h0 < hM < hF

    def gain(h: float) -> float:
        _, vf = global_flat(P.l, h, P)
        _, vm, _ = global_meter(P.l, h, P)
        return vm - vf

    muM, muF = gain(hM), gain(hF)
    assert muM < P.mu < muF

    # Candidate-deviation audit in the strict gap.
    assert gain(hF) - P.mu > 0.0
    assert gain(hM) - P.mu < 0.0

    # Unique architecture-indifference state and unique supporting mix.
    hstar = bisect(lambda h: gain(h) - P.mu, hM, hF)
    _, _, pstar = global_meter(P.l, hstar, P)
    rho = P.KH * (hF - hstar) / (P.d * pstar)
    assert hM < hstar < hF
    assert 0.0 < rho < 1.0

    # H-only/no-service expectations imply zero H continuation rent and hence
    # h0.  Both-served strictly dominates those active sets there, so they do
    # not generate a hidden pure rational-expectations equilibrium on R+.
    af0, _ = global_flat(P.l, P.h0, P)
    am0, _, _ = global_meter(P.l, P.h0, P)
    assert af0 == ["both"] and am0 == ["both"]

    # Permanent exact outside-region counterexample.
    P2 = Par(4.0, 5.0, 1.0, 0.1, 1.0, 0.6, 1.0, 0.0)
    fb = both_profit(0.0, 0.1, 0.6, P2)
    fh = honly_profit(0.0, 0.6, P2)
    assert abs((fh - fb) - 2.3) < 1e-12

    # Off-path continuation-completeness stress.  The direct evaluator returns
    # a finite global candidate at arbitrary installed masses and never treats
    # a failure/NaN as an unprofitable deviation.
    for l in (0.0, 0.03, 0.1, 0.8, 1.0):
        for h in (0.0, 0.02, 0.09, 0.14, 0.6, 1.0, 2.0):
            af, vf = global_flat(l, h, P)
            am, vm, pm = global_meter(l, h, P)
            assert af and am
            assert math.isfinite(vf) and math.isfinite(vm) and math.isfinite(pm)

    print("stage4a repair independent audit: PASS")
    print(f"h0={P.h0:.12f} hM={hM:.12f} hF={hF:.12f}")
    print(f"muM={muM:.12f} mu={P.mu:.12f} muF={muF:.12f}")
    print(f"h*={hstar:.12f} p*={pstar:.12f} rho*={rho:.12f}")
    print(f"outside-R H-only flat advantage={fh - fb:.12f}")


if __name__ == "__main__":
    main()
