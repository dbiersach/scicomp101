# circle_area.py

import numpy as np

n = 1_000_000
dx = 1 / n

x = np.arange(0, 1, dx)
y = np.sqrt(1 - x**2)

a = np.sum(y) * dx
print(a * 4)
