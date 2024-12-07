# -*- coding: utf-8 -*-
# Configuration for Landau-Zener Simulation

W = 1.0  # Coupling strength
a = 0.1  # Slope of epsilon
hbar = 1.0  # Reduced Planck's constant
tau0 = 10.0  # Time range factor
t_min = -tau0 / a  # Minimum time
t_max = tau0 / a  # Maximum time
