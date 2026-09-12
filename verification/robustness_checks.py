"""Deterministic Stage-7.5A robustness checks.

The general-CDF checks support the integration-ordering sufficient conditions.
The nonquadratic checks are NUMERICAL ROBUSTNESS ONLY and are not a proof for
all concave demand systems.
"""

from __future__ import annotations

import math
from typing import Callable


def bisect_fixed_point(T: Callable[[float], float], lo: float, hi: float) -> float:
    flo = T(lo) - lo
    fhi = T(hi) - hi
    assert flo >= 0 and fhi <= 0
    for _ in range(120):
        mid = (lo + hi) / 2
        fm = T(mid) - mid
        if fm > 0:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def golden_max(f: Callable[[float], float], lo: float, hi: float) -> tuple[float, float]:
    ratio = (math.sqrt(5.0) - 1.0) / 2.0
    x1 = hi - ratio * (hi - lo)
    x2 = lo + ratio * (hi - lo)
    f1, f2 = f(x1), f(x2)
    for _ in range(200):
        if hi - lo < 1e-12:
            break
        if f1 > f2:
            hi, x2, f2 = x2, x1, f1
            x1 = hi - ratio * (hi - lo)
            f1 = f(x1)
        else:
            lo, x1, f1 = x1, x2, f2
            x2 = lo + ratio * (hi - lo)
            f2 = f(x2)
    x = (lo + hi) / 2.0
    return x, f(x)


def cdf_checks() -> None:
    # Baseline economic parameters. H-cost heterogeneity is varied through G.
    l, c, d = 0.8, 1.0, 1.0
    gross_flat_cutoff = 5.0 / 8.0

    cdfs: dict[str, Callable[[float], float]] = {
        "uniform": lambda z: min(max(z, 0.0), 1.0),
        "z^2": lambda z: min(max(z, 0.0), 1.0) ** 2,
        "sqrt(z)": lambda z: math.sqrt(min(max(z, 0.0), 1.0)),
        "smoothstep": lambda z: (
            3 * min(max(z, 0.0), 1.0) ** 2
            - 2 * min(max(z, 0.0), 1.0) ** 3
        ),
    }

    for name, G in cdfs.items():
        hF = G(gross_flat_cutoff)

        def T(h: float) -> float:
            p = c + d * h / (l + h)
            z = (5.0 - p) / 8.0
            return G(z)

        hM = bisect_fixed_point(T, 0.0, hF)
        assert 0.0 < hM < hF < 1.0
        print(f"CDF {name:10s}: h_M={hM:.10f} < h_F={hF:.10f}")


def demand(a: float, p: float, r: int) -> float:
    return max(a - p, 0.0) ** (1.0 / (r - 1))


def indirect_surplus(a: float, p: float, r: int) -> float:
    z = max(a - p, 0.0)
    return (r - 1.0) / r * z ** (r / (r - 1.0))


def power_utility_checks() -> None:
    # v_j(q)=a_j q-q^r/r. These are robustness examples, not general proof.
    aL, aH, c = 4.0, 5.0, 1.0
    l, bH, KH = 0.8, 0.5, 8.0

    for r in (2, 3, 4):
        def flat_profit(h: float) -> float:
            F = indirect_surplus(aL, 0.0, r)
            return (
                (l + h) * F
                - c * (l * demand(aL, 0.0, r) + h * demand(aH, 0.0, r))
            )

        def metered_optimum(h: float) -> tuple[float, float]:
            def profit(p: float) -> float:
                F = indirect_surplus(aL, p, r)
                q = l * demand(aL, p, r) + h * demand(aH, p, r)
                return (l + h) * F + (p - c) * q

            return golden_max(profit, 0.0, aL - 1e-9)

        RF = indirect_surplus(aH, 0.0, r) - indirect_surplus(aL, 0.0, r)
        hF = (bH + RF) / KH

        def integration_map(h: float) -> float:
            p, _ = metered_optimum(h)
            rent = indirect_surplus(aH, p, r) - indirect_surplus(aL, p, r)
            return (bH + rent) / KH

        hM = bisect_fixed_point(integration_map, 0.0, hF)
        assert 0.0 < hM < hF < 1.0

        def psi(h: float) -> float:
            _, metered_profit = metered_optimum(h)
            return metered_profit - flat_profit(h)

        grid = [hM + (hF - hM) * i / 40 for i in range(41)]
        values = [psi(x) for x in grid]
        assert all(values[i + 1] > values[i] - 1e-9 for i in range(len(values) - 1))

        print(
            f"power r={r}: h_M={hM:.10f} < h_F={hF:.10f}; "
            f"Psi increasing on deterministic grid"
        )


def main() -> None:
    cdf_checks()
    power_utility_checks()
    print("robustness checks: PASS (scope as documented)")


if __name__ == "__main__":
    main()
