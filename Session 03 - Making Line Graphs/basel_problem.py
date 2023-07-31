# basel_problem.py

import numpy as np
import matplotlib.pyplot as plt

# Insert your code here


# Do not edit the remaining code
plt.figure()
plt.plot(x, y1, label="1/x")
plt.plot(x, y2, label="1/x**2")
plt.title("Infinite Series")
plt.xlabel("Number of Terms")
plt.ylabel("Cummulative Sum")
plt.legend()
plt.show()
