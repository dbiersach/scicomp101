# herons_method.py


def sqrt(s):
    x = s / 2
    while x**2 - s > 1e-10:
        x = (s / x + x) / 2
    return x


print(sqrt(168923.74))
