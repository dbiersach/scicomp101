# pells_equation.py

from math import floor, sqrt
import numba


@numba.njit
def pell_solution(n):
    x: int = 1
    while x < 70_000:
        x2: int = x * x
        y: int = 1
        y_max: int = floor(sqrt((x2 - 1) / n))
        while y <= y_max:
            y2: int = y * y
            if x2 - n * y2 == 1:
                return True, x, y
            y += 1
        x += 1
    return False, 0, 0


print(f"{'n':>4}{'x':>8}{'y':>8}")
print(f"{'='*3:>4}{'='*6:>8}{'='*6:>8}")

for i in range(2, 71):
    solution_exists, xs, ys = pell_solution(i)
    if solution_exists:
        print(f"{i:>4}{xs:>8}{ys:>8}")
    else:
        print(f"{i:>4}{'-':>8}{'-':>8}")
