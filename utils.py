# -*- coding: utf-8 -*-
import numpy as np


def analytical_probability(W, a, hbar=1.0):
    """
    Computes the analytical Landau-Zener transition probability.

    Parameters:
    - W: Coupling strength (real constant).
    - a: Slope of the linear term in epsilon.
    - hbar: Reduced Planck's constant (default is 1.0).

    Returns:
    - Transition probability as per Landau-Zener formula.
    """
    Gamma = (W**2) / (hbar * a)
    return 1 - np.exp(-2 * np.pi * Gamma)
