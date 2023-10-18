# circle_sampling.py

import numpy as np
import matplotlib.pyplot as plt

n = 10_000
t = np.linspace(0, 2 * np.pi, n)
r = np.sqrt(np.random.rand(n))
x = r * np.cos(t)
y = r * np.sin(t)

plt.figure("circle_sampling.py")
pixel_size = (72 / plt.gcf().dpi) ** 2
plt.scatter(x, y, s=pixel_size)
plt.title("Uniform Circle Sampling")
plt.axis("equal")
plt.show()
