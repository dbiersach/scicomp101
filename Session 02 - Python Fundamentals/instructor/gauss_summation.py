# gauss_summation.py

import numpy as np

n = 10
x = np.linspace(1, n, n)
print(x)

y1 = np.cumsum(x)
print(y1)

y2 = x * (x + 1) / 2
print(y2)

print(np.array_equal(y1, y2))
