# nyquist_known.py

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import AutoMinorLocator

a, b, n = (0, 20, 640)
x = np.linspace(a, b, n + 1)
y = np.sin(4 / 5 * np.pi * x)

plt.figure("nyquist_known.py")
# fmt: off
plt.plot(x, y, color="blue", marker="o", markersize=2,
    markerfacecolor="red", markeredgecolor="red")
# fmt: on
plt.title(r"$y=\sin(\frac{4}{5}\pi x)$" f" ({n} Samples)")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim(-1.1, 1.2)
plt.axhline(y=0, color="lightgray")
plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
plt.show()
