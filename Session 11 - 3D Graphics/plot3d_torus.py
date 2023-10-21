# plot3d_torus.py

import numpy as np
import matplotlib.pyplot as plt


radius_poloidal = 5
radius_toroidal = 25

u = np.linspace(0, 2 * np.pi, 60)  # Poloidal rotation
v = np.linspace(0, 2 * np.pi, 60)  # Toroidal rotation

x = np.outer(radius_toroidal + radius_poloidal * np.sin(u), np.cos(v))
y = np.outer(radius_toroidal + radius_poloidal * np.sin(u), np.sin(v))
z = np.outer(radius_poloidal * np.cos(u), np.ones_like(v))

plt.figure("plot3d_torus.py", constrained_layout=True)
ax = plt.axes(projection="3d")
ax.view_init(azim=132, elev=-144)
ax.figure.set_size_inches(10, 8)

ax.scatter(x, y, z, color="gold")
# ax.plot_surface(x, y, z, color="gold")

ax.set_xlim(-radius_toroidal, radius_toroidal)
ax.set_ylim(-radius_toroidal, radius_toroidal)
ax.set_zlim(-radius_toroidal, radius_toroidal)

plt.show()
