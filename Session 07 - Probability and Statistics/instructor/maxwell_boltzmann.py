# maxwell_boltzmann.py

import numpy as np
import matplotlib.pyplot as plt


def pdf(x, a):
    return np.sqrt(2 / np.pi) * x**2 / a**3 * np.exp((-(x**2)) / (2 * a**2))


x = np.linspace(0, 20, 500)

plt.figure()
plt.plot(x, pdf(x, 1), label="a = 1")
plt.plot(x, pdf(x, 2), label="a = 2")
plt.plot(x, pdf(x, 3), label="a = 5")
plt.title("Maxwell-Boltzmann PDF")
plt.xlabel("x")
plt.ylabel("P(x)")
plt.legend()
plt.grid()
plt.show()
