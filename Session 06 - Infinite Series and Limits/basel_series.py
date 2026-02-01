#!/usr/bin/env -S uv run
"""basel_series.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Update the following code
n = 1
x = np.zeros(1)
y1 = np.zeros(1)
y2 = np.zeros(1)

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
