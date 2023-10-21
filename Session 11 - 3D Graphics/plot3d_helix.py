# plot3d_helix.py

import numpy as np
import matplotlib.pyplot as plt


theta = np.linspace(0, 20 * np.pi, 2000)  # poloidal angle
x = theta * np.cos(theta)
y = theta * np.sin(theta)
z = theta

plt.figure("plot3d_helix.py")
ax = plt.axes(projection="3d")
ax.view_init(azim=-45)
ax.figure.set_size_inches(10, 8)
ax.plot(x, y, z)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
plt.show()
