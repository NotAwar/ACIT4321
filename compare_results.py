# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from diabatic_basis import (
    t_eval as t_diabatic,
    prob_01 as prob_diabatic,
    P_final as P_final_diabatic,
)
from adiabatic_basis import (
    t_eval as t_adiabatic,
    prob_transition_adiabatic,
    P_final_adiabatic,
)
from utils import analytical_probability
from config import W, a, hbar

# Compute analytical transition probability
P_analytical = analytical_probability(W=W, a=a, hbar=hbar)

# Print comparison of results
print(f"Numerical Transition Probability (Diabatic Basis): {P_final_diabatic:.6f}")
print(f"Numerical Transition Probability (Adiabatic Basis): {P_final_adiabatic:.6f}")
print(f"Analytical Transition Probability: {P_analytical:.6f}")

# Plot time-dependent probabilities from both bases
plt.figure(figsize=(10, 6))

# Diabatic Basis
plt.plot(t_diabatic, prob_diabatic, label="Diabatic Basis", color="blue")

# Adiabatic Basis
plt.plot(
    t_adiabatic,
    prob_transition_adiabatic,
    label="Adiabatic Basis",
    color="green",
    linestyle="--",
)

# Annotate the plot
plt.axvline(0, color="black", linestyle="--", linewidth=0.8, label="Avoided Crossing")
plt.xlabel("Time (t)", fontsize=14)
plt.ylabel("Transition Probability", fontsize=14)
plt.title("Transition Probabilities: Diabatic vs Adiabatic Basis", fontsize=16)
plt.legend(fontsize=12)
plt.grid()
plt.show()

# Bar plot to compare final probabilities
plt.figure(figsize=(8, 5))
plt.bar(
    ["Diabatic", "Adiabatic", "Analytical"],
    [P_final_diabatic, P_final_adiabatic, P_analytical],
    color=["blue", "green", "orange"],
)
plt.ylabel("Transition Probability", fontsize=14)
plt.title("Final Transition Probabilities: Diabatic vs Adiabatic Basis", fontsize=16)
plt.grid(axis="y")
plt.show()
