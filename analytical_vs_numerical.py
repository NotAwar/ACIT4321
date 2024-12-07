# -*- coding: utf-8 -*-
import numpy as np
from utils import analytical_probability
from config import W, a, hbar
from diabatic_basis import P_final as P_final_diabatic

# Compute analytical transition probability
P_analytical = analytical_probability(W=W, a=a, hbar=hbar)

# Print comparison of analytical and numerical results
print(f"Numerical Transition Probability (Diabatic Basis): {P_final_diabatic:.6f}")
print(f"Analytical Transition Probability: {P_analytical:.6f}")

# Check consistency with the adiabatic theorem (W -> 0)
W_small = 0.01
P_analytical_small_W = analytical_probability(W=W_small, a=a, hbar=hbar)
print(f"Analytical Probability with W -> 0: {P_analytical_small_W:.6f}")
