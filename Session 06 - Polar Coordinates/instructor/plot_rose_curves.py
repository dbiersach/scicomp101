# plot_rose_curves.py

import numpy as np
import matplotlib.pyplot as plt

# Insert your code here
t = np.linspace(0, 4 * np.pi, 1000)
r1 = 4 + 4 * np.cos(4 * t)
r2 = 3 + 3 * np.cos(4 * t + np.pi)
r3 = 5 + 5 * np.cos(3 / 2 * t)

# Do not edit the remaining code
plt.figure().add_subplot(projection="polar")
plt.plot(t, r1)
plt.plot(t, r2)
plt.plot(t, r3)
plt.show()
