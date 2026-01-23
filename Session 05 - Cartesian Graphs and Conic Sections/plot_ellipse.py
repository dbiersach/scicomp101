#!/usr/bin/env -S uv run

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

a, b = 250, 150
theta = np.linspace(0, 2 * np.pi)
x = a * np.cos(theta)
y = b * np.sin(theta)

plt.figure(Path(__file__).name)
plt.plot(x, y, "o-")  # 'o-' to see the individual points
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.title(rf"Ellipse: $\dfrac{{x^2}}{{{a}^2}} + \dfrac{{y^2}}{{{b}^2}} = 1$")
plt.xlim(-300, 300)
plt.ylim(-300, 300)
plt.gca().set_aspect("equal")
plt.grid(True)
plt.show()
