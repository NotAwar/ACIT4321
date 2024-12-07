# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from config import W, a, hbar, t_min, t_max

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
