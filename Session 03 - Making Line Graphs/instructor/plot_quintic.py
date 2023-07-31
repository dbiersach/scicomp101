# plot_quintic.py

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 12)
y = (x - 11) * (x - 5) * (x + 1) * (x + 4) * (x + 9)

plt.figure()
plt.plot(x, y)
plt.grid()
plt.show()
