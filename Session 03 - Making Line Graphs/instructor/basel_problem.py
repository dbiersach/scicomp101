# basel_problem.py

import numpy as np
import matplotlib.pyplot as plt

# Insert your code here
n = 100_000
x = np.linspace(1, n, n)
y1 = np.cumsum(1 / x)
y2 = np.cumsum(1 / x**2)

p = y2.take(-1)
print(np.sqrt(6 * p))

# Do not edit the remaining code
plt.figure()
plt.plot(x, y1, label="1/x")
plt.plot(x, y2, label="1/x**2")
plt.title("Infinite Series")
plt.xlabel("Number of Terms")
plt.ylabel("Cummulative Sum")
plt.legend()
plt.show()
