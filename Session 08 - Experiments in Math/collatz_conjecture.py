#!/usr/bin/env -S uv run
"""collatz_conjecture.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from numba import njit


@njit
def stop_time(n):
    return 0


def main():
    max_n = 1_000_000
    x = np.arange(max_n)
    y = np.vectorize(stop_time)(x)
    plt.figure(Path(__file__).name)
    plt.hist(y, bins=500, color="blue")
    plt.title(f"Collatz Conjecture (n < {max_n:,})")
    plt.xlabel("Stopping Time")
    plt.ylabel("Count")
    plt.show()


if __name__ == "__main__":
    main()
