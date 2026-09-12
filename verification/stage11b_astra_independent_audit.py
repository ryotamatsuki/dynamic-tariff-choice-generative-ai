#!/usr/bin/env python3
"""Independent hostile Stage-11B evaluator for dynamic-tariff-choice-generative-ai.

This file is intentionally separate from verification/baseline_checks.py and
verification/robustness_checks.py. It reconstructs continuation payoffs from
primitive utility/surplus functions, enumerates active sets, searches fixed
points, and tests nonquadratic demand systems.

Tie convention used *only for this computational audit*: a task participates
when its continuation utility is exactly zero. The manuscript currently needs
to state such a convention explicitly if it wants the exact fixed-fee maxima.

No production verification code is imported.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Callable, List, Tuple


EPS = 1e-9


def golden_max(f: Callable[[float], float], lo: float, hi: float,
               iters: int = 250) -> Tuple[float, float]:
    """Derivative-free bounded maximization; independent of repo solvers."""
    phi = (math.sqrt(5.0) - 1.0) / 2.0
    x1 = hi - phi * (hi - lo)
    x2 = lo + phi * (hi - lo)
    f1, f2 = f(x1), f(x2)
    for _ in range(iters):
        if hi - lo < 1e-13:
            break
        if f1 >= f2:
            hi, x2, f2 = x2, x1, f1
            x1 = hi - phi * (hi - lo)
            f1 = f(x1)
        else:
            lo, x1, f1 = x1, x2, f2
            x2 = lo + phi * (hi - lo)
            f2 = f(x2)
    x = (lo + hi) / 2.0
    return x, f(x)


def bisect_root(f: Callable[[float], float], lo: float, hi: float,
                iters: int = 250) -> float:
    flo, fhi = f(lo), f(hi)
    if abs(flo) < 1e-13:
        return lo
    if abs(fhi) < 1e-13:
        return hi
    if flo * fhi > 0:
        raise ValueError(f"root not bracketed: f(lo)={flo}, f(hi)={fhi}")
    for _ in range(iters):
        mid = (lo + hi) / 2.0
        fm = f(mid)
        if abs(fm) < 1e-13 or hi - lo < 1e-13:
            return mid
        if flo * fm <= 0:
            hi, fhi = mid, fm
        else:
            lo, flo = mid, fm
    return (lo + hi) / 2.0


def scan_roots(f: Callable[[float], float], lo: float, hi: float,
               n: int = 3000) -> List[float]:
    roots: List[float] = []
    x0, y0 = lo, f(lo)
    for i in range(1, n + 1):
        x1 = lo + (hi - lo) * i / n
        y1 = f(x1)
        if math.isfinite(y0) and math.isfinite(y1):
            if abs(y1) < 1e-10:
                r = x1
            elif y0 * y1 < 0:
                r = bisect_root(f, x0, x1)
            else:
                r = None
            if r is not None and all(abs(r - z) > 1e-6 for z in roots):
                roots.append(r)
        x0, y0 = x1, y1
    return roots


class TypeUtility:
    choke_price: float

    def q(self, p: float) -> float:
        raise NotImplementedError

    def surplus(self, p: float) -> float:
        raise NotImplementedError


@dataclass(frozen=True)
class QuadraticType(TypeUtility):
    a: float

    @property
    def choke_price(self) -> float:
        return self.a

    def q(self, p: float) -> float:
        return max(self.a - p, 0.0)

    def surplus(self, p: float) -> float:
        z = max(self.a - p, 0.0)
        return z * z / 2.0


@dataclass(frozen=True)
class CubicType(TypeUtility):
    """v(q)=a q-q^2/2-eta q^3/3, eta>0."""
    a: float
    eta: float

    @property
    def choke_price(self) -> float:
        return self.a

    def q(self, p: float) -> float:
        if p >= self.a:
            return 0.0
        e = self.eta
        return (-1.0 + math.sqrt(1.0 + 4.0 * e * (self.a - p))) / (2.0 * e)

    def surplus(self, p: float) -> float:
        q = self.q(p)
        v = self.a * q - q * q / 2.0 - self.eta * q ** 3 / 3.0
        return v - p * q


@dataclass(frozen=True)
class LogInverseDemandType(TypeUtility):
    """Primitive v(q)=(q/k)[1+ln(A/q)], q>0; v'(q)=ln(A/q)/k.

    With nonnegative p, q(p)=A exp(-k p), and S(p)=q(p)/k.
    v is strictly concave because v''(q)=-1/(kq)<0.
    """
    A: float
    k: float

    @property
    def choke_price(self) -> float:
        return 100.0

    def q(self, p: float) -> float:
        return self.A * math.exp(-self.k * max(p, 0.0))

    def surplus(self, p: float) -> float:
        return self.q(p) / self.k


@dataclass(frozen=True)
class Continuation:
    active: str
    p: float
    F: float
    gross_profit: float
    rent_L: float
    rent_H: float


def direct_profit(active: str, p: float, l: float, h: float,
                  L: TypeUtility, H: TypeUtility, c: float) -> Continuation:
    """Direct payoff from primitive demands; activation cost is excluded."""
    qL, qH = L.q(p), H.q(p)
    SL, SH = L.surplus(p), H.surplus(p)

    if active == "both":
        if SH + 1e-12 < SL:
            return Continuation(active, p, float("nan"), -math.inf, 0.0, 0.0)
        F = SL
        gross = (l + h) * F + (p - c) * (l * qL + h * qH)
        return Continuation(active, p, F, gross, 0.0, SH - SL)

    if active == "H-only":
        if SH <= SL + 1e-12:
            return Continuation(active, p, float("nan"), -math.inf, 0.0, 0.0)
        F = SH
        gross = h * (F + (p - c) * qH)
        return Continuation(active, p, F, gross, 0.0, 0.0)

    if active == "no-service":
        return Continuation(active, p, 0.0, 0.0, 0.0, 0.0)

    raise ValueError(active)


def global_flat(l: float, h: float, L: TypeUtility, H: TypeUtility,
                c: float) -> Continuation:
    candidates = [
        direct_profit("both", 0.0, l, h, L, H, c),
        direct_profit("H-only", 0.0, l, h, L, H, c),
        direct_profit("no-service", 0.0, l, h, L, H, c),
    ]
    return max(candidates, key=lambda z: z.gross_profit)


def global_metered(l: float, h: float, L: TypeUtility, H: TypeUtility,
                   c: float) -> Continuation:
    hi_both = max(EPS * 10.0, L.choke_price - 1e-8)

    def pb(p: float) -> float:
        return direct_profit("both", p, l, h, L, H, c).gross_profit

    p_b, _ = golden_max(pb, EPS, hi_both)
    both = direct_profit("both", p_b, l, h, L, H, c)

    hi_h = min(max(H.choke_price - 1e-8, 2.0 * c + 10.0), 100.0)

    def ph(p: float) -> float:
        return direct_profit("H-only", p, l, h, L, H, c).gross_profit

    N = 1500
    best_i, best_v = 1, -math.inf
    for i in range(1, N):
        p = EPS + (hi_h - EPS) * i / N
        val = ph(p)
        if val > best_v:
            best_i, best_v = i, val
    lo = EPS + (hi_h - EPS) * max(best_i - 3, 0) / N
    hi = EPS + (hi_h - EPS) * min(best_i + 3, N) / N
    p_h, _ = golden_max(ph, lo, hi)
    honly = direct_profit("H-only", p_h, l, h, L, H, c)

    no = direct_profit("no-service", max(H.choke_price, L.choke_price),
                       l, h, L, H, c)
    return max([both, honly, no], key=lambda z: z.gross_profit)


def architecture_gain(l: float, h: float, L: TypeUtility, H: TypeUtility,
                      c: float) -> Tuple[float, Continuation, Continuation]:
    f = global_flat(l, h, L, H, c)
    m = global_metered(l, h, L, H, c)
    return m.gross_profit - f.gross_profit, f, m


def integration_residual(h: float, architecture: str, l: float,
                         bH: float, KH: float,
                         L: TypeUtility, H: TypeUtility, c: float) -> float:
    cont = global_flat(l, h, L, H, c) if architecture == "flat" else \
           global_metered(l, h, L, H, c)
    return (bH + cont.rent_H) / KH - h


def integration_roots(architecture: str, l: float, bH: float, KH: float,
                      L: TypeUtility, H: TypeUtility, c: float) -> List[float]:
    return scan_roots(
        lambda h: integration_residual(h, architecture, l, bH, KH, L, H, c),
        0.0, 1.0, n=4000
    )


def baseline_audit() -> None:
    print("\n=== BASELINE: independent direct-payoff audit ===")
    L, H = QuadraticType(4.0), QuadraticType(5.0)
    c, l, bH, KH, mu = 1.0, 0.8, 0.5, 8.0, 1.3

    roots_F = integration_roots("flat", l, bH, KH, L, H, c)
    roots_M = integration_roots("metered", l, bH, KH, L, H, c)
    assert len(roots_F) == 1 and len(roots_M) == 1
    hF, hM = roots_F[0], roots_M[0]
    assert 0.0 < hM < hF < 1.0

    muM = architecture_gain(l, hM, L, H, c)[0]
    muF = architecture_gain(l, hF, L, H, c)[0]
    assert muM < mu < muF

    hstar = bisect_root(
        lambda h: architecture_gain(l, h, L, H, c)[0] - mu,
        hM, hF
    )
    mstar = global_metered(l, hstar, L, H, c)
    rho = KH * (hF - hstar) / ((H.a - L.a) * mstar.p)
    assert 0.0 < rho < 1.0

    print(f"h_M={hM:.12f}, h_F={hF:.12f}")
    print(f"mu_M={muM:.12f}, mu={mu:.12f}, mu_F={muF:.12f}")
    print(f"h*={hstar:.12f}, p*(h*)={mstar.p:.12f}, rho*={rho:.12f}")

    for tag, h in [("h_M", hM), ("h*", hstar), ("h_F", hF)]:
        gain, f, m = architecture_gain(l, h, L, H, c)
        assert f.active == "both" and m.active == "both"
        print(tag, "flat=", f, "metered=", m, "gain=", gain)

    assert architecture_gain(l, hF, L, H, c)[0] > mu
    assert architecture_gain(l, hM, L, H, c)[0] < mu

    h0 = bH / KH
    gain0, f0, m0 = architecture_gain(l, h0, L, H, c)
    assert h0 < hM
    assert f0.active == "both" and m0.active == "both"
    print(f"zero-rent H state h0={h0:.12f}: flat active={f0.active}, "
          f"meter active={m0.active}, gain={gain0:.12f}")


def active_set_boundary_audit() -> None:
    print("\n=== ACTIVE-SET boundary audit ===")
    L, H, c = QuadraticType(4.0), QuadraticType(5.0), 1.0

    def diff_flat(l: float, h: float) -> float:
        both = direct_profit("both", 0.0, l, h, L, H, c).gross_profit
        ho = direct_profit("H-only", 0.0, l, h, L, H, c).gross_profit
        return ho - both

    def diff_meter(l: float, h: float) -> float:
        def f_h(p: float) -> float:
            return direct_profit("H-only", p, l, h, L, H, c).gross_profit

        def f_b(p: float) -> float:
            return direct_profit("both", p, l, h, L, H, c).gross_profit

        _, piH = golden_max(f_h, EPS, H.a - 1e-8)
        _, piB = golden_max(f_b, EPS, L.a - 1e-8)
        return piH - piB

    for l in (0.1, 0.8):
        flat_root = bisect_root(lambda h: diff_flat(l, h), 1e-8, 2.0)
        meter_root = bisect_root(lambda h: diff_meter(l, h), 1e-8, 2.0)
        print(f"l={l}: flat both/H-only switch h={flat_root:.12f}; "
              f"meter both/H-only switch h={meter_root:.12f}")

    l, h = 0.1, 0.6
    both = direct_profit("both", 0.0, l, h, L, H, c).gross_profit
    ho = direct_profit("H-only", 0.0, l, h, L, H, c).gross_profit
    assert abs((ho - both) - 2.3) < 1e-10
    print(f"outside-R point (l=.1,h=.6): H-only flat advantage={ho-both:.12f}")

    for h in (0.07, 0.09, 0.11, 0.14, 0.15):
        f = global_flat(0.1, h, L, H, c)
        m = global_metered(0.1, h, L, H, c)
        print(f"h={h:.2f}: flat={f.active}, metered={m.active}")


def nonquadratic_audit() -> None:
    print("\n=== NONQUADRATIC robustness and counterexample audit ===")

    L, H = CubicType(4.0, 0.1), CubicType(5.0, 0.1)
    c, l, bH, KH = 1.0, 0.8, 0.5, 8.0
    f_roots = integration_roots("flat", l, bH, KH, L, H, c)
    m_roots = integration_roots("metered", l, bH, KH, L, H, c)
    assert len(f_roots) == 1 and len(m_roots) == 1
    hF, hM = f_roots[0], m_roots[0]
    gains = [architecture_gain(l, hM + (hF-hM)*i/80, L, H, c)[0]
             for i in range(81)]
    assert hM < hF
    assert all(gains[i+1] > gains[i] - 1e-8 for i in range(len(gains)-1))
    assert global_flat(l, hF, L, H, c).active == "both"
    assert global_metered(l, hM, L, H, c).active == "both"
    print(f"common cubic eta=.1: h_M={hM:.12f}<h_F={hF:.12f}; "
          f"Psi endpoints=({gains[0]:.12f},{gains[-1]:.12f})")

    L2 = QuadraticType(4.0)
    H2 = LogInverseDemandType(A=5.0, k=0.6)
    c2, l2, bH2, KH2 = 1.85, 0.8, 0.5, 25.0/6.0
    f2 = integration_roots("flat", l2, bH2, KH2, L2, H2, c2)
    m2 = integration_roots("metered", l2, bH2, KH2, L2, H2, c2)
    assert len(f2) == 1 and len(m2) == 1
    hF2, hM2 = f2[0], m2[0]
    assert hM2 > hF2
    gf, ff, mf = architecture_gain(l2, hF2, L2, H2, c2)
    gm, fm, mm = architecture_gain(l2, hM2, L2, H2, c2)
    assert ff.active == mf.active == fm.active == mm.active == "both"
    assert L2.q(0.0) < H2.q(0.0)
    assert L2.surplus(0.0) < H2.surplus(0.0)
    assert mf.rent_H > (H2.surplus(0.0)-L2.surplus(0.0))
    print("strictly concave crossing-demand counterexample:")
    print(f"  flat q_L={L2.q(0):.6f}<q_H={H2.q(0):.6f}; "
          f"S_L={L2.surplus(0):.6f}<S_H={H2.surplus(0):.6f}")
    print(f"  h_F={hF2:.12f}<h_M={hM2:.12f} (ordering reverses)")
    print(f"  metered p at h_F={mf.p:.12f}; flat H-rent="
          f"{H2.surplus(0)-L2.surplus(0):.12f}; "
          f"metered H-rent={mf.rent_H:.12f}")
    print(f"  Psi(h_F)={gf:.12f}, Psi(h_M)={gm:.12f}")


def quadratic_welfare(l: float, h: float, aL: float, aH: float, c: float,
                      bL: float, KL: float, bH: float, KH: float,
                      p: float, mu: float) -> float:
    def omega(a: float) -> float:
        return ((a-c)**2 - (p-c)**2) / 2.0
    return (bL*l + bH*h - KL*l*l/2.0 - KH*h*h/2.0
            + l*omega(aL) + h*omega(aH) - mu)


def welfare_sign_audit() -> None:
    print("\n=== WELFARE sign-reversal audit (mu=0) ===")
    examples = [
        dict(name="M-welfare-higher", aL=5.0, aH=5.5, c=2.0,
             l=0.8, bL=3.2, KL=4.0, bH=4.0, KH=10.0),
        dict(name="F-welfare-higher", aL=5.0, aH=6.5, c=0.25,
             l=0.75, bL=3.0, KL=4.0, bH=1.0, KH=10.0),
    ]
    signs = []
    for e in examples:
        L, H = QuadraticType(e["aL"]), QuadraticType(e["aH"])
        hF = integration_roots("flat", e["l"], e["bH"], e["KH"], L, H, e["c"])[0]
        hM = integration_roots("metered", e["l"], e["bH"], e["KH"], L, H, e["c"])[0]
        f = global_flat(e["l"], hF, L, H, e["c"])
        m = global_metered(e["l"], hM, L, H, e["c"])
        assert f.active == "both" and m.active == "both"
        WF = quadratic_welfare(e["l"], hF, e["aL"], e["aH"], e["c"],
                               e["bL"], e["KL"], e["bH"], e["KH"], 0.0, 0.0)
        WM = quadratic_welfare(e["l"], hM, e["aL"], e["aH"], e["c"],
                               e["bL"], e["KL"], e["bH"], e["KH"], m.p, 0.0)
        diff = WM-WF
        signs.append(math.copysign(1.0, diff))
        print(f"{e['name']}: h_M={hM:.12f}, h_F={hF:.12f}, "
              f"W_M-W_F={diff:.12f}, p_M={m.p:.12f}")
    assert signs[0] > 0 and signs[1] < 0


def main() -> None:
    baseline_audit()
    active_set_boundary_audit()
    nonquadratic_audit()
    welfare_sign_audit()
    print("\nSTAGE11B INDEPENDENT AUDIT NUMERICS: PASS")


if __name__ == "__main__":
    main()
