# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from config import W, a, hbar, t_min, t_max
from hamiltonian import hamiltonian, epsilon

# --- Rewriting the Hamiltonian in the Adiabatic Basis ---


# Compute the mixing angle θ(t)
def mixing_angle(t):
    """
    Compute the mixing angle θ(t) for the given time t.

    Parameters:
    - t: Time value.

    Returns:
    - Mixing angle θ(t).
    """
    eps = epsilon(t)  # Use the imported epsilon function
    return 0.5 * np.arctan2(W, eps)


# Transformation matrix U(t)
def transformation_matrix(t):
    """
    Construct the transformation matrix U(t) from the mixing angle.

    Parameters:
    - t: Time value.

    Returns:
    - 2x2 transformation matrix U(t).
    """
    theta = mixing_angle(t)
    return np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])


# Derivative of the transformation matrix dU/dt
def d_transformation_matrix(t):
    """
    Compute the derivative of the transformation matrix dU/dt.

    Parameters:
    - t: Time value.

    Returns:
    - 2x2 matrix representing dU/dt.
    """
    theta = mixing_angle(t)
    dtheta_dt = -0.5 * W * a / (epsilon(t) ** 2 + W**2)  # Reuse epsilon
    return np.array(
        [
            [-np.sin(theta) * dtheta_dt, -np.cos(theta) * dtheta_dt],
            [np.cos(theta) * dtheta_dt, -np.sin(theta) * dtheta_dt],
        ]
    )


# Adiabatic Hamiltonian H_adiabatic(t)
def adiabatic_hamiltonian(t):
    """
    Rewrite the Hamiltonian in the adiabatic basis.

    Parameters:
    - t: Time value.

    Returns:
    - 2x2 adiabatic Hamiltonian H_adiabatic(t).
    """
    H = hamiltonian(t)  # Use the reusable hamiltonian function
    U = transformation_matrix(t)
    dU_dt = d_transformation_matrix(t)
    return np.dot(U.T.conj(), np.dot(H, U)) - 1j * hbar * np.dot(U.T.conj(), dU_dt)


# --- Solving the Schrödinger Equation in the Adiabatic Basis ---


# Right-hand side of the Schrödinger equation
def schrodinger_rhs_adiabatic(t, psi):
    """
    Compute the right-hand side of the Schrödinger equation in the adiabatic basis.

    Parameters:
    - t: Time value.
    - psi: Quantum state vector at time t.

    Returns:
    - Time derivative of the quantum state vector.
    """
    H_ad = adiabatic_hamiltonian(t)
    return -1j * np.dot(H_ad, psi)


# --- Main Execution and Transition Probability Calculation ---

# Initial state in the adiabatic basis
psi0_adiabatic = np.array([1.0 + 0j, 0.0 + 0j])

# Time vector for evaluation
t_eval = np.linspace(t_min, t_max, 1000)

# Solve the Schrödinger equation
solution_adiabatic = solve_ivp(
    schrodinger_rhs_adiabatic,
    (t_min, t_max),
    psi0_adiabatic,
    t_eval=t_eval,
    rtol=1e-8,
    atol=1e-8,
)

# Extract time and solution
t = solution_adiabatic.t
psi_adiabatic = solution_adiabatic.y

# Compute the transition probability
prob_transition_adiabatic = np.abs(psi_adiabatic[1, :]) ** 2

# Plot the transition probability in the adiabatic basis
plt.figure(figsize=(10, 6))
plt.plot(
    t,
    prob_transition_adiabatic,
    label="Transition Probability (Adiabatic Basis)",
    color="green",
)
plt.axvline(0, color="black", linestyle="--", linewidth=0.8, label="Avoided Crossing")
plt.xlabel("Time (t)", fontsize=14)
plt.ylabel("Probability", fontsize=14)
plt.title("Transition Probability vs Time (Adiabatic Basis)", fontsize=16)
plt.legend(fontsize=12)
plt.grid()
plt.show()

# Final transition probability
P_final_adiabatic = prob_transition_adiabatic[-1]
print(f"Final Transition Probability (Adiabatic Basis): {P_final_adiabatic:.6f}")
