#!/usr/bin/env -S uv run
"""olympic_rings.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

radius = 25.0
theta = np.linspace(0, 2 * np.pi, 1000)
x = radius * np.cos(theta)
y = radius * np.sin(theta)

x_offset = 0
y_offset = 0

plt.figure(Path(__file__).name)
plt.plot(x, y, color="black", linewidth=12)
plt.plot(x - x_offset, y, color="blue", linewidth=12)
plt.plot(x + x_offset, y, color="red", linewidth=12)
plt.plot(x - x_offset / 2, y - y_offset, color="yellow", linewidth=12)
plt.plot(x + x_offset / 2, y - y_offset, color="green", linewidth=12)
plt.title("The Olympic Rings")
plt.gca().set_aspect("equal")
plt.axis(False)
plt.show()
