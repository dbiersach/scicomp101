# plot_superposition.py

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 4 * np.pi, 1000)
r = 7 + 7 * np.sin(11 * t) * np.cos(5 * t)

plt.figure().add_subplot(projection="polar")
plt.plot(t, r, color="black")
plt.show()
