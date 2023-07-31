# numpy_arrays.py

import numpy as np

x = np.arange(5)
print(x)
print()

x = np.arange(1, 6)
print(x)
print(x * 2)
print(x**2)
print()

y = np.linspace(0, 2)
print(y)
print(y.size)
print(y.take(0))
print(y.take(-1))
print(np.sqrt(y))
