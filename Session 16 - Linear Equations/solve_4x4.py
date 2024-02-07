# solve_4x4.py

import numpy as np

# Create the coefficients matrix
coeffs = np.array()

# Create the values vector
vals = np.array()

# Use matrix algebra to solve the system of equations
print(np.linalg.inv(coeffs) @ vals)
