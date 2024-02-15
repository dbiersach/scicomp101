# nyquist_unknown.py

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.ticker import AutoMinorLocator

# fmt: off
def f(x):
    return (np.sin(4 * np.pi * x) * np.sin(6 * np.pi * x)
        * np.sin(10 * np.pi * x) * np.sin(14 * np.pi * x))
# fmt: on


def main():
    a, b, n = (0, 210, 420)
    x = np.linspace(a, b, n + 1)
    y = f(x)

    plt.figure("nyquist_unknown.py")
    # fmt: off
    plt.plot(x, y, color="blue", marker="o", markersize=2,
        markerfacecolor="red", markeredgecolor="red")
    # fmt: on
    plt.title(f"Unknown Waveform ({n} Samples)")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.ylim(-1.1, 1.2)
    plt.axhline(y=0, color="lightgray")
    plt.gca().xaxis.set_minor_locator(AutoMinorLocator())
    plt.gca().yaxis.set_minor_locator(AutoMinorLocator())
    plt.show()


main()
