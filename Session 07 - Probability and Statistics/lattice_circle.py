# lattice_circle.py

import numpy as np
import numba


@numba.njit
def lattice_points(r):
    c = 0
    # Insert your code here


    # Do not edit the remaining code
    return c


for radius in np.linspace(1000, 10000, 10):
    act = lattice_points(radius)
    est = int(np.pi * radius**2 + 2 * np.sqrt(2 * np.pi * radius))
    err = (est - act) / act
    print(
        f"Radius = {int(radius):>6,}"
        f"  Act Points = {act:>12,}"
        f"  Est Points = {est:>12,}"
        f"  % Rel. Err = {err:0.4%}"
    )
