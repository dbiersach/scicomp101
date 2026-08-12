#!/usr/bin/env -S uv run
"""
numpy_arrays_instructor.py
Demonstrate basic NumPy array operations and functionality.

This module introduces fundamental NumPy operations including creating arrays
with linspace, performing element-wise arithmetic operations, accessing array
properties, and applying mathematical functions to arrays.
"""

import numpy as np

# Create an array of 5 evenly spaced numbers between 1 and 5
x = np.linspace(1, 5, 5)
print(x)
print(len(x))
print()

# Demonstrate element-wise operations
print(x * 2)
print(x**2)
print()

# Use slicing to access parts of the array
print(x[3:])
print(x[:3])
print(x[2:4])
print(x[::2])
print(x[::-1])
print()

# Perform mathematical functions on arrays
y = np.linspace(0, 2)
print(y)
print(y.size)
print(y[0])
print(y[-1])
print(np.sqrt(y))
print()

# Demonstrate a vectorized scalar operation
z = np.linspace(-10, 10)
print(z)
print(np.abs(z))
print()

# Demonstrate a vectorized array operation
print(y * z + np.pi)
print()

# Demonstrate array conditional selection
print(np.where(z > 0))  # Indices where condition is True
print(z > 0)  # Boolean array
print(z[z > 0])  # Values where condition is True
