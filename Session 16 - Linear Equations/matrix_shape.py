# matrix_shape.py

import numpy as np


def print_ndarray_info(name, a):
    print(f"Type of {name} is {type(a).__name__}")
    print(f"Number of dimensions of {name} = {a.ndim}")
    print(f"Shape of dimensions of {name} = {a.shape}")
    print(f"Length of {name} = {len(a)}")
    print(f"Size of {name} = {a.size}")
    print()


def main():
    a = np.array([[4, 5, 8], [1, 9, 7]])
    b = np.array([[2, 4], [6, 1], [5, 9]])

    print(f"A = {a}\nB = {b}\n")

    print_ndarray_info("A", a)
    print_ndarray_info("B", b)


main()
