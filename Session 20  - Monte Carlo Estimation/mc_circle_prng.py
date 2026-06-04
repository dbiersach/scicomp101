#!/usr/bin/env -S uv run
"""mc_circle_prng.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

dots = 102_400

rng = np.random.default_rng(seed=2020)
x = rng.random(dots) * 2 - 1
y = rng.random(dots) * 2 - 1

d = x**2 + y**2

x_in = x[d <= 1.0]
y_in = y[d <= 1.0]
x_out = x[d > 1.0]
y_out = y[d > 1.0]

act_area = np.pi
est_area = np.count_nonzero(d <= 1.0) / dots * 4
err = np.abs((est_area - act_area) / act_area)

print(f"dots = {dots:,}")
print(f"act = {act_area:.6f}")
print(f"est = {est_area:.6f}")
print(f"err = {err:.5%}")

plt.figure(Path(__file__).name)
plt.scatter(x_in, y_in, color="red", marker=".", s=0.5)
plt.scatter(x_out, y_out, color="blue", marker=".", s=0.5)
plt.axis("equal")
plt.show()
