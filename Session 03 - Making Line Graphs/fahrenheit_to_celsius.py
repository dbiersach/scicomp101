# fahrenheit_to_celsius.py

import numpy as np
import matplotlib.pyplot as plt

k = np.linspace(0, 400)
f = 9 / 5 * (k - 273.15) + 32
c = 5 / 9 * (f - 32)

plt.figure()
plt.plot(k, f, label="Fahrenheit")
plt.plot(k, c, label="Celsius")
plt.grid()
plt.title("Scale Comparison")
plt.xlabel("Kelvin")
plt.ylabel("Temperature")
plt.legend()
plt.show()
