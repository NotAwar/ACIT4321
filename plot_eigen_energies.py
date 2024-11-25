# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# Define parameters
W = 1.0  # Coupling strength
a = 0.1  # Slope of epsilon
tau0 = 10.0  # Time range factor

# Time range
t_min = -tau0 / a
t_max = tau0 / a
t_values = np.linspace(t_min, t_max, 1000)

# Compute eigen-energies
epsilon = a * t_values
E_plus = 0.5 * np.sqrt(epsilon**2 + W**2)
E_minus = -0.5 * np.sqrt(epsilon**2 + W**2)

# Plot eigen-energies
plt.figure(figsize=(10, 6))
plt.plot(t_values, E_plus, label="E+", color="blue")
plt.plot(t_values, E_minus, label="E-", color="red")
plt.axhline(0, color="black", linestyle="--", linewidth=0.8)
plt.axvline(0, color="black", linestyle="--", linewidth=0.8)
plt.xlabel("Time (t)", fontsize=14)
plt.ylabel("Energy (E)", fontsize=14)
plt.title("Time-Dependent Eigen-Energies", fontsize=16)
plt.legend(fontsize=12)
plt.grid()
plt.show()
