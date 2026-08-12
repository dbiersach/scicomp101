#!/usr/bin/env -S uv run
"""euclid_gcd.py"""


def gcd(a, b):
    # TODO: Implement Euclid's algorithm here

    return b


def gcd_fast(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def main():
    a, b = 231, 182
    print(f"The GCD of {a} and {b} = {gcd(a, b)}")
    print(f"The GCD of {a} and {b} = {gcd_fast(a, b)}")


if __name__ == "__main__":
    main()
