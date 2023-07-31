# archimedes_spiral.py

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10 * np.pi, 1000)

plt.figure().add_subplot(projection="polar")
plt.plot(t, t)
plt.show()
