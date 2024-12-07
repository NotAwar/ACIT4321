# -*- coding: utf-8 -*-
import unittest
import numpy as np
from hamiltonian import hamiltonian, epsilon
from utils import analytical_probability


class TestLandauZener(unittest.TestCase):
    def test_hamiltonian(self):
        """Test if Hamiltonian is constructed correctly."""
        t = 0
        H = hamiltonian(t)
        self.assertEqual(H.shape, (2, 2))
        self.assertAlmostEqual(H[0, 1], 0.5)  # W/2

    def test_analytical_probability(self):
        """Test the analytical probability function."""
        W, a, hbar = 1.0, 0.1, 1.0
        expected = 1 - np.exp(-2 * np.pi * (W**2) / (hbar * a))
        computed = analytical_probability(W, a, hbar)
        self.assertAlmostEqual(computed, expected, places=6)


if __name__ == "__main__":
    unittest.main()
