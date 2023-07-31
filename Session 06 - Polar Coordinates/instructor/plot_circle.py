# plot_circle.py

import numpy as np
import matplotlib.pyplot as plt

# Insert your code here
r = 250
t = np.linspace(0, 2 * np.pi, 1000)
x = r * np.cos(t)
y = r * np.sin(t)

# Do not edit the remaining code
plt.figure()
plt.plot(x, y)
plt.grid()
plt.axis("equal")
plt.show()
