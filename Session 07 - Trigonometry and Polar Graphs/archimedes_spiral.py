#!/usr/bin/env -S uv run
"""archimedes_spiral.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad

# Sample points
n_points = 100_000

# Polar to Cartesian conversion for Archimedes Spiral
theta = np.linspace(0, 8 * np.pi, n_points)
x = theta * np.cos(theta)
y = theta * np.sin(theta)

# Perimeter (accumulate Cartesian distances)
dx = np.diff(x)
dy = np.diff(y)
perimeter_est = np.sum(np.hypot(dx, dy))

# Arc Length (integral)
arc_length = quad(lambda theta: np.sqrt(theta**2 + 1), 0, 8 * np.pi)[0]

print("Archimedes Spiral")
print(f"Number of points: {n_points:,}\n")
print("Estimated perimeter / arc length:")
print(f"Cartesian approximation: {perimeter_est:,.8f}")
print(f"Integral approximation : {arc_length:,.8f}\n")

# Plot using Polar coordinates
plt.figure(Path(__file__).name)
plt.subplot(projection="polar")
plt.plot(theta, theta, lw=3)
plt.title(
    r"Archimedes Spiral $\left(r=\theta,\;0\leq\theta\leq 8\pi\right)$"
    f"\nArc Length = {arc_length:.8f}"
)
plt.gca().set_aspect("equal")
plt.grid(True)
plt.tight_layout()
plt.show()
