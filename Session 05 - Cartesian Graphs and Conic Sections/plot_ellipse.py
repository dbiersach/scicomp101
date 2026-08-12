#!/usr/bin/env -S uv run
"""plot_ellipse.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Ellipse parameters
a, b = 250, 150

x = np.linspace(0, a, 1000)
y = b * np.sqrt(1 - (x**2 / a**2))

plt.figure(Path(__file__).name)
plt.plot(x, y)
plt.plot(x, -y)
plt.plot(-x, y)
plt.plot(-x, -y)
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.title(rf"Ellipse: $\dfrac{{x^2}}{{{a}^2}}+\dfrac{{y^2}}{{{b}^2}}=1$")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-a - 50, a + 50)
plt.ylim(-b - 50, b + 50)
plt.gca().set_aspect("equal")
plt.grid(True)
plt.show()
