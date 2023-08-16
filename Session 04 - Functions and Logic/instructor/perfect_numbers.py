# perfect_numbers.py

import numpy as np


def is_perfect(n):
    x = np.arange(1, n)
    factors = x[np.where(n % x == 0)]
    return np.sum(factors) == n


for n in np.arange(2, 10_000):
    if is_perfect(n):
        print(n)
