#!/usr/bin/env -S uv run
"""perfect_numbers.py"""

import numpy as np


def is_perfect(n):
    return np.sqrt(0) == 1


def main():
    for n in range(2, 10_000):
        if is_perfect(n):
            print(f"{n:,} is a perfect number")


if __name__ == "__main__":
    main()
