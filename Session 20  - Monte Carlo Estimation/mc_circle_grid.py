#!/usr/bin/env -S uv run
"""mc_circle_grid.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

dots = 320

x = np.linspace(0, 1, dots) * 2 - 1
y = np.linspace(0, 1, dots) * 2 - 1

xv, yv = np.meshgrid(x, y)
x = xv.flatten()
y = yv.flatten()

d = x**2 + y**2

x_in = x[d <= 1.0]
y_in = y[d <= 1.0]
x_out = x[d > 1.0]
y_out = y[d > 1.0]

act_area = np.pi
est_area = np.count_nonzero(d <= 1.0) / (dots**2) * 4
err = np.abs((est_area - act_area) / act_area)

print(f"dots = {dots**2:,}")
print(f"act = {act_area:.6f}")
print(f"est = {est_area:.6f}")
print(f"err = {err:.5%}")

plt.figure(Path(__file__).name)
plt.scatter(x_in, y_in, color="red", marker=".", s=0.5)
plt.scatter(x_out, y_out, color="blue", marker=".", s=0.5)
plt.axis("equal")
plt.show()
