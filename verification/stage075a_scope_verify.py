#!/usr/bin/env python3
"""Stage 7.5A scope/quantifier regression checks for the repaired theory.

This script does not create a broader theorem. It verifies algebra that underlies
strict R+ endpoint propagation, T1/T2 scope, the Stage-7 fixed-base welfare
identity, and the retained exact scope counterexample.
"""

import sympy as sp

# Symbols and baseline objects.
aL, c, d, l, h, KH, bH = sp.symbols(
    "aL c d l h KH bH", positive=True
)
aH = aL + d
n = l + h
RF = sp.expand((aH**2 - aL**2) / 2)
pB = sp.simplify(c + d * h / n)

# Metered both-served and H-only continuation profits.
piMB = sp.expand(
    n * (aL - pB) ** 2 / 2
    + (pB - c) * (l * (aL - pB) + h * (aH - pB))
)
piMH = sp.expand(h * (aH - c) ** 2 / 2)
Dmeter = sp.simplify(piMH - piMB)

# The repaired Stage-4R endpoint argument requires rival-minus-both profit to
# increase with h. Verify the exact derivative formula recorded in Stage 4R.
expected_Dmeter_prime = sp.simplify(
    d * (d * l**2 + 2 * (aL - c) * (h + l) ** 2)
    / (2 * (h + l) ** 2)
)
assert sp.simplify(sp.diff(Dmeter, h) - expected_Dmeter_prime) == 0

# Flat H-only minus both-served derivative equals R_F > 0.
piFB = sp.expand(n * aL**2 / 2 - c * (l * aL + h * aH))
piFH = sp.expand(h * aH**2 / 2 - c * h * aH)
Dflat = sp.expand(piFH - piFB)
assert sp.simplify(sp.diff(Dflat, h) - RF) == 0

# Repaired metered fixed-point residual is strictly decreasing once positivity
# assumptions are imposed; verify the exact derivative identity.
g = sp.simplify(bH + RF - d * pB - KH * h)
assert sp.simplify(sp.diff(g, h) - (-KH - d**2 * l / n**2)) == 0

# Provider gross metering gain and its derivative.
Phi = sp.simplify(n * pB**2 / 2)
Phi_prime_expected = sp.simplify(
    (c * n + d * h) * (c * n + d * h + 2 * d * l) / (2 * n**2)
)
assert sp.simplify(sp.diff(Phi, h) - Phi_prime_expected) == 0

# Stage-7 fixed-installed-base welfare threshold identity.
muW = sp.simplify(n * (c**2 - d**2 * (h / n) ** 2) / 2)
assert sp.simplify(Phi - muW - d * h * pB) == 0

# Exact repaired baseline endpoint evidence.
Q = sp.Rational
aL0, aH0, c0 = Q(4), Q(5), Q(1)
l0, h00, hF0 = Q(4, 5), Q(1, 16), Q(5, 8)
d0 = aH0 - aL0

def pstar(hh):
    return sp.simplify(c0 + d0 * hh / (l0 + hh))

def flat_both(hh):
    return sp.simplify((l0 + hh) * aL0**2 / 2 - c0 * (l0 * aL0 + hh * aH0))

def flat_honly(hh):
    return sp.simplify(hh * aH0**2 / 2 - c0 * hh * aH0)

def meter_both(hh):
    pp = pstar(hh)
    return sp.simplify(
        (l0 + hh) * (aL0 - pp) ** 2 / 2
        + (pp - c0) * (l0 * (aL0 - pp) + hh * (aH0 - pp))
    )

def meter_honly(hh):
    return sp.simplify(hh * (aH0 - c0) ** 2 / 2)

assert pstar(hF0) == Q(82, 57)
assert flat_both(h00) == Q(271, 80)
assert sp.simplify(flat_both(h00) - flat_honly(h00)) == Q(467, 160)
assert sp.simplify(flat_both(hF0) - flat_honly(hF0)) == Q(31, 80)
assert sp.simplify(meter_both(hF0) - meter_honly(hF0)) == Q(3533, 2280)

# Permanent out-of-domain guard.
l_bad, h_bad = Q(1, 10), Q(3, 5)
pi_both_bad = sp.simplify((l_bad + h_bad) * aL0**2 / 2 - c0 * (l_bad * aL0 + h_bad * aH0))
pi_h_bad = sp.simplify(h_bad * aH0**2 / 2 - c0 * h_bad * aH0)
assert sp.simplify(pi_h_bad - pi_both_bad) == Q(23, 10)

print("Stage 7.5A scope/quantifier verification: PASS")
print("R+ metered active-set derivative:", sp.factor(expected_Dmeter_prime))
print("Phi_h:", sp.factor(Phi_prime_expected))
print("fixed-base welfare wedge:", sp.factor(d * h * pB))
print("baseline p_B(h_F):", pstar(hF0))
print("outside-R+ H-only flat advantage:", Q(23, 10))
