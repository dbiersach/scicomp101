#!/usr/bin/env -S uv run
"""plot_circle.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

radius = 250
theta = np.linspace(0, 2 * np.pi, 1000)
x = radius * np.cos(theta)
y = radius * np.sin(theta)

plt.figure(Path(__file__).name)
plt.plot(x, y)
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.title(f"$x^2 + y^2 = {radius}$")
plt.xlim(-300, 300)
plt.ylim(-300, 300)
plt.gca().set_aspect("equal")
plt.grid(True)
plt.show()
