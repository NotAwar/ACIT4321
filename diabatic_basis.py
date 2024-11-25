# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Parameters
W = 1.0  # Coupling strength
a = 0.1  # Slope of epsilon
hbar = 1.0  # Planck's constant (set to 1 for simplicity)
tau0 = 10.0  # Time range factor

# Time range
t_min = -tau0 / a
t_max = tau0 / a


# Define epsilon as a function of time
def epsilon(t):
    return a * t


# Define the Hamiltonian
def hamiltonian(t):
    eps = epsilon(t)
    return np.array([[-eps / 2, W / 2], [W / 2, eps / 2]])


# Right-hand side of the Schrödinger equation
def schrodinger_rhs(t, psi):
    H = hamiltonian(t)
    return -1j * np.dot(H, psi)


# Initial state (complex array)
psi0 = np.array([1.0 + 0j, 0.0 + 0j])

# Time vector for evaluation
t_eval = np.linspace(t_min, t_max, 1000)

# Solve the Schrödinger equation
solution = solve_ivp(
    schrodinger_rhs, (t_min, t_max), psi0, t_eval=t_eval, rtol=1e-8, atol=1e-8
)

# Extract time and state vectors
t = solution.t
psi = solution.y

# Calculate transition probability to the (0, 1)-state
prob_01 = np.abs(psi[1, :]) ** 2

# Plot the transition probability
plt.figure(figsize=(10, 6))
plt.plot(t, prob_01, label="Transition Probability (0, 1)", color="blue")
plt.axvline(0, color="black", linestyle="--", linewidth=0.8, label="Avoided Crossing")
plt.xlabel("Time (t)", fontsize=14)
plt.ylabel("Probability", fontsize=14)
plt.title("Transition Probability vs Time (Diabatic Basis)", fontsize=16)
plt.legend(fontsize=12)
plt.grid()
plt.show()

# Transition probability at final time
P_final = prob_01[-1]
print(f"Final Transition Probability P(0 -> 1): {P_final:.6f}")
