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


dots = 40_000

# Insert your code here











# Do not edit the remaining code
print(f"dots = {dots:,}")
print(f"act = {act:.6f}")
print(f"est = {est:.6f}")
print(f"err = {err:.5%}")

plt.figure("mc_parabola.py")
plt.scatter(x_in, y_in, color="red", marker=".", s=0.5)
plt.scatter(x_out, y_out, color="blue", marker=".", s=0.5)
plt.title("$y=-x^2+4$")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
