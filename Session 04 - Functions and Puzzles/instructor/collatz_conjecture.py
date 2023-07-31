# collatz_conjecture.py

import numpy as np
import matplotlib.pyplot as plt
import numba


# Insert your code here
@numba.njit
def stop_time(n):
    c = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        c = c + 1
    return c


# Do not edit the remaining code
max_n = 1_000_000
x = np.arange(max_n)

f = np.vectorize(stop_time)
y = f(x)

plt.figure()
plt.hist(y, bins=500, color="blue")
plt.title(f"Collatz Conjecture (n < {max_n:,})")
plt.xlabel("Stopping Time")
plt.ylabel("Count")
plt.show()
