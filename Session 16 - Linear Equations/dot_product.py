# dot_product.py

import numpy as np


def print_ndarray_info(name, a):
    print(f"Type of {name} is {type(a).__name__}")
    print(f"Number of dimensions of {name} = {a.ndim}")
    print(f"Shape of dimensions of {name} = {a.shape}")
    print(f"Length of {name} = {len(a)}")
    print(f"Size of {name} = {a.size}")
    print()


def main():
    theta1, theta2 = 1 / 4 * np.pi, 3 / 4 * np.pi

    v = np.array([np.cos(theta1), np.sin(theta1)])
    w = np.array([np.cos(theta2), np.sin(theta2)])

    print(f"{v = }\n{w = }\n")
    print_ndarray_info("v", v)
    print(f"{np.linalg.norm(v) = }")
    print(f"v + w = {np.round(np.add(v, w), 4)}")
    print(f"v dot w = {np.round(np.dot(v, w), 4)}")


main()
