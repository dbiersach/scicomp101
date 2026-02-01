#!/usr/bin/env python3
"""wave_superposition.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes  # for type hinting


def plot(ax: Axes) -> None:
    theta = np.linspace(0, 4 * np.pi, 1000)
    ax.plot(theta, 7 + 7 * np.sin(11 * theta) * np.cos(5 * theta), c="k", lw=2)
    ax.set_title("Superposition of Waves")


def main() -> None:
    plt.figure(Path(__file__).name, figsize=(8, 6))
    ax: Axes = plt.axes(projection="polar")
    plot(ax)
    plt.show()


if __name__ == "__main__":
    main()
