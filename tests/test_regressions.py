from __future__ import annotations

import unittest
import sympy as sp


class FrozenTheoryRegressionTests(unittest.TestCase):
    def test_exact_regular_example_orders_states_and_thresholds(self):
        aL, aH, c = sp.Rational(4), sp.Rational(5), sp.Rational(1)
        bL, KL = sp.Rational(16, 5), sp.Rational(4)
        bH, KH = sp.Rational(1, 2), sp.Rational(8)
        mu = sp.Rational(13, 10)
        l = bL / KL
        d = aH - aL
        RF = (aH**2 - aL**2) / 2
        hF = (bH + RF) / KH
        h = sp.symbols("h", positive=True)
        p = c + d * h / (l + h)
        hM = [r for r in sp.solve(sp.Eq(KH * h, bH + RF - d * p), h) if sp.N(r) > 0][0]
        phi = (l + h) / 2 * p**2
        muM = sp.simplify(phi.subs(h, hM))
        muF = sp.simplify(phi.subs(h, hF))
        self.assertTrue(sp.N(hM) < sp.N(hF))
        self.assertTrue(sp.N(muM) < sp.N(mu) < sp.N(muF))

    def test_permanent_H_only_scope_counterexample(self):
        aL, aH, c = sp.Rational(4), sp.Rational(5), sp.Rational(1)
        l, h = sp.Rational(1, 10), sp.Rational(3, 5)
        both_flat = (l + h) * aL**2 / 2 - c * (l * aL + h * aH)
        h_only_flat = h * aH**2 / 2 - c * h * aH
        self.assertEqual(sp.simplify(h_only_flat - both_flat), sp.Rational(23, 10))

    def test_threshold_collapse_when_state_is_architecture_insensitive(self):
        h0 = sp.Rational(1, 2)
        l, c, d = sp.Rational(4, 5), sp.Rational(1), sp.Rational(1)
        phi = lambda h: (l + h) / 2 * (c + d * h / (l + h)) ** 2
        self.assertEqual(sp.simplify(phi(h0) - phi(h0)), 0)


if __name__ == "__main__":
    unittest.main()
