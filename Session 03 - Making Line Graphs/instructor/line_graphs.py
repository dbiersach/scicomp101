# line_graphs.py

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10)

y1 = 2 * x - 5
y2 = -0.3 * x**2 + 15

plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)
plt.grid()
plt.show()
