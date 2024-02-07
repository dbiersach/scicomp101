# matrix_determinant.py

import numpy as np


def print_ndarray_info(name, a):
    print(f"Type of {name} is {type(a).__name__}")
    print(f"Number of dimensions of {name} = {a.ndim}")
    print(f"Shape of dimensions of {name} = {a.shape}")
    print(f"Length of {name} = {len(a)}")
    print(f"Size of {name} = {a.size}")
    print()


def main():
    a = np.array([[8, 3], [4, 2]])
    print(f"A = {a}\n")

    det_A = np.linalg.det(a)
    print(f"|A| = {det_A}")
    print(f"|A| = {np.round(det_A, 4)}\n")

    b = np.array(
        [
            [3, 4, 9, 8, -5, -2, 2, 7, 7, 4],
            [6, -10, -10, -10, -6, -10, 1, 0, -4, -5],
            [-4, -4, -4, 8, -5, 9, 4, 0, -4, 9],
            [-4, 6, -5, 8, 0, 3, 1, -4, -6, -6],
            [-6, -9, 9, 9, -2, 9, -5, -2, -2, -3],
            [-8, 0, 0, 0, 10, -3, 5, 0, -4, 9],
            [8, 4, 8, -9, 4, 8, -6, 1, 9, 2],
            [2, 1, -1, 4, -6, -10, 1, -6, 6, 7],
            [-6, -5, 4, -6, -5, -6, -10, -1, -2, 7],
            [1, 10, -10, -4, -8, 7, 5, -1, 6, -6],
        ]
    )
    print_ndarray_info("B", b)
    det_B = np.linalg.det(b)
    print(f"|B| = {det_B}")
    print(f"|B| = {det_B:,.0f}")


main()
