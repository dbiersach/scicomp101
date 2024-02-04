# plot3d_surface.py

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator


def f(x, y):
    return np.sin(np.sqrt(x**2 + y**2))


def main():
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)

    x, y = np.meshgrid(x, y)
    z = f(x, y)

    plt.figure("plot3d_surface.py", constrained_layout=True)
    plt.axes(projection="3d")
    plt.gcf().set_size_inches(10, 8)

    surf = plt.gca().plot_surface(
        x, y, z, cmap=cm.coolwarm, linewidth=0, antialiased=False
    )
    plt.colorbar(surf, ax=plt.gca(), shrink=0.5, aspect=5)

    plt.gca().zaxis.set_major_locator(LinearLocator(10))
    plt.gca().zaxis.set_major_formatter("{x:.02f}")

    plt.show()


main()
