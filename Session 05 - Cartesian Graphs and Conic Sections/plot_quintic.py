#!/usr/bin/env -S uv run
"""plot_quintic.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 12, 100)
y = (x - 11) * (x - 5) * (x + 1) * (x + 4) * (x + 9)

plt.figure(Path(__file__).name)
plt.plot(x, y, c="springgreen", lw=2)
plt.title("$y=x^5-2x^4-120x^3+22x^2+2119x+1980$")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
