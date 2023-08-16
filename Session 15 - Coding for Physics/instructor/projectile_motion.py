# projectile_motion.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

range = 400  # m
t = np.radians(45)  # 45 degree launch angle
g = 9.81  # m/s^2
v0 = np.sqrt(range * g / np.sin(2 * t))  # initial velocity (m/s)

x = np.linspace(0, 600, 200)
y = np.tan(t) * x - (g / (2 * v0**2 * np.cos(t) ** 2)) * x**2

plt.figure()
plt.plot(x, y)
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.gca().add_patch(Rectangle((395, 0), 10, 2, color="red"))
plt.show()
