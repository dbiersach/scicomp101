# mc_parabola.py

import numpy as np
import matplotlib.pyplot as plt
from numba import float64, vectorize


@vectorize([float64(float64, float64)], nopython=True)
def halton(n, p):
    h, f = 0, 1
    while n > 0:
        f = f / p
        h += (n % p) * f
        n = int(n / p)
    return h


# Insert your code here

dots = 40_000

x = halton(np.arange(dots), 2) * 4 - 2
y = halton(np.arange(dots), 3) * 5

d = 4 - x**2 - y

x_in = x[d >= 0.0]
y_in = y[d >= 0.0]
x_out = x[d < 0.0]
y_out = y[d < 0.0]

act = 32 / 3
est = np.count_nonzero(d <= 1.0) / dots * 20
err = np.abs((est - act) / act)

# Do not edit the remaining code
print(f"dots = {dots:,}")
print(f"act = {act:.6f}")
print(f"est = {est:.6f}")
print(f"err = {err:.5%}")

plt.figure()
plt.scatter(x_in, y_in, color="red", marker=".", s=0.5)
plt.scatter(x_out, y_out, color="blue", marker=".", s=0.5)
plt.show()
