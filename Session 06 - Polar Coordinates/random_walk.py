# random_walk.py

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2017)
n = 10_000
x = np.zeros(n)
y = np.zeros(n)

# Insert your code here





# Do not edit the remaining code
plt.figure()
plt.plot(x, y)
plt.plot(x[0], y[0], color="green", marker="o")
plt.plot(x[-1], y[-1], color="red", marker="o")
plt.axis("equal")
plt.show()
