#!/usr/bin/env -S uv run
"""basel_series_instructor.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Update the following code
n = 100_000
x = np.linspace(1, n, n)
y1 = np.cumsum(1 / x)
y2 = np.cumsum(1 / x**2)

# Calculate magic number
print(np.sqrt(6 * y2[-1]))

# Do not edit the remaining code
plt.figure(Path(__file__).name)
plt.plot(x, y1, label="1/x")
plt.plot(x, y2, label="1/x**2")
plt.title("Infinite Series")
plt.xlabel("Number of Terms")
plt.ylabel("Cumulative Sum")
plt.legend()
plt.show()
