# -*- coding: utf-8 -*-
import numpy as np
from config import W, a


# Define epsilon as a function of time
def epsilon(t):
    return a * t


# Define the Hamiltonian
def hamiltonian(t):
    eps = epsilon(t)
    return np.array([[-eps / 2, W / 2], [W / 2, eps / 2]])
