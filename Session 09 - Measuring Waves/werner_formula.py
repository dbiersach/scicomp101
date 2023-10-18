# werner_formula.py

import numpy as np
import matplotlib.pyplot as plt

a = 0.8
b = 0.5

x = np.linspace(-3 * np.pi, 3 * np.pi, 100)

f1 = np.sin(a * x)
f2 = np.sin(b * x)

# Insert your code here



# Do not edit the remaining code
plt.figure()
plt.plot(x, f1, label="f1")
plt.plot(x, f2, label="f2")
plt.plot(x, f3, label="f3")
plt.plot(x, f4, color="grey", linestyle="dotted", marker="o", label="f4")
plt.legend()
plt.grid()
plt.show()
