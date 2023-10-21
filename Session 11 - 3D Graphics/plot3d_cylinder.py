# plot3d_cylinder.py

import numpy as np
import matplotlib.pyplot as plt

radius, height = 10, 50

u = np.linspace(0, height, 30)
v = np.linspace(0, 2 * np.pi, 30)  # toroidal angle

# Insert your code here
x = 
y = 
z = 

# Do not edit the remaining code
plt.figure("plot3d_cylinder.py")
ax = plt.axes(projection="3d")
ax.set_aspect("equal")
ax.figure.set_size_inches(10, 8)

ax.plot_surface(x, y, z, color="red")

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

ax.set_xlim(-height, height)
ax.set_ylim(-height, height)
ax.set_zlim(0, height)

plt.show()
