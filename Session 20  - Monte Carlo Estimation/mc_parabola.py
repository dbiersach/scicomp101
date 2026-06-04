#!/usr/bin/env -S uv run
"""mc_parabola.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from numba import float64, vectorize


@vectorize([float64(float64, float64)], nopython=True)
def halton(n, p):
    h, f = 0, 1
    while n > 0:
        f = f / p
        h += (n % p) * f
        n = int(n / p)
    return h


def main():
    dots = 1

    x = halton(np.arange(dots), 2)
    y = halton(np.arange(dots), 3)

    d = 0

    x_in = x[d >= 0.0]
    y_in = y[d >= 0.0]
    x_out = x[d < 0.0]
    y_out = y[d < 0.0]

    act_area = 1
    est_area = np.count_nonzero(d >= 0.0) / dots
    err = np.abs((est_area - act_area) / act_area)

    print(f"dots = {dots:,}")
    print(f"act = {act_area:.6f}")
    print(f"est = {est_area:.6f}")
    print(f"err = {err:.5%}")

    plt.figure(Path(__file__).name)
    plt.scatter(x_in, y_in, color="red", marker=".", s=0.5)
    plt.scatter(x_out, y_out, color="blue", marker=".", s=0.5)
    plt.title("$y=-x^2+4$")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


if __name__ == "__main__":
    main()
