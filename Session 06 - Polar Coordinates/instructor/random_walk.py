# random_walk.py

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2017)
n = 10_000
x = np.zeros(n)
y = np.zeros(n)

# Insert your code here
for i in range(1, n):
    t = 2 * np.pi * np.random.rand()
    x[i] = x[i - 1] + np.cos(t)
    y[i] = y[i - 1] + np.sin(t)

# Do not edit the remaining code
plt.figure()
plt.plot(x, y)
plt.plot(x[0], y[0], color="green", marker="o")
plt.plot(x[-1], y[-1], color="red", marker="o")
plt.axis("equal")
plt.show()
