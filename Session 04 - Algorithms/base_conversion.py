#!/usr/bin/env -S uv run
"""
base_conversion.py

Illustrate binary to/from decimal conversion.

Includes both manual implementations for learning purposes and
Pythonic built-in alternatives for real-world use.
"""

import numpy as np


def binary_to_decimal(b):
    # Reverse string 'b' because the
    # LSB must be in first position
    b = b[::-1]
    sum = 0
    for position in range(len(b)):
        weight = pow(2, position)
        digit = int(b[position])
        sum += digit * weight
    return sum


def decimal_to_binary(d):
    b = ""
    while d > 0:
        b += str(d % 2)
        d = int(d / 2)
    # Reverse string 'b' because the
    # LSB must be in first position
    b = b[::-1]
    return b


def main():
    # Call our hand-crafted function
    b = "1011001"
    d = binary_to_decimal(b)
    print(f"{b} in binary = {d:,} in decimal")

    # Call our hand-crafted function
    d = 113
    b = decimal_to_binary(d)
    print(f"{d:,} in decimal = {b} in binary")

    print()

    # Better to call the built-in integer constructor
    b = "1011001"
    d = int(b, 2)
    print(f"{b} in binary = {d:,} in decimal")

    # Better to call numpy's built-in base converter
    d = 113
    b = np.base_repr(d, base=2)
    print(f"{d:,} in decimal = {b} in binary")


if __name__ == "__main__":
    main()
