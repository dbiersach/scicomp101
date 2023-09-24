# circle_area.py

import numpy as np

n = 1_000_000

x = np.linspace(0, 1, n)
y = np.sqrt(1 - x**2)

a = np.sum(y) / n

print(a * 4)
