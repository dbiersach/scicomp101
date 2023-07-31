# newton_sqrt.py

import numpy as np


def sqrt(x):
    low, high = 0, x
    est = (low + high) / 2
    n = 1
    while np.abs(est**2 - x) > 1e-10:
        if est**2 < x:
            low = est
        else:
            high = est
        est = (low + high) / 2
        n = n + 1
    return est


print(sqrt(168923.74))
