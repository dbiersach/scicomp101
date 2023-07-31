# coprime_probability.py

import numpy as np

n = 1_000_000
a = np.random.randint(1, n, size=n)
b = np.random.randint(1, n, size=n)

c = np.gcd(a, b)
p = np.sum(c == 1) / c.size

print(p)
print(np.sqrt(6 / p))
