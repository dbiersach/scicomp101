# uniform_variance.py

import numpy as np


def trial(t):
    lo = np.random.randint(10_000)
    hi = lo + np.random.randint(100_000)
    s = np.random.randint(10_000, 200_000)
    r = np.random.randint(lo, hi, s)
    m, v = np.mean(r), np.var(r)
    magic = (hi - lo) ** 2 / v
    print(f"{t:>8}", end="")
    print(f"{lo:>9,}", end="")
    print(f"{hi:>9,}", end="")
    print(f"{s:>9,}", end="")
    print(f"{m:>14.3f}", end="")
    print(f"{v:>16.3f}", end="")
    print(f"{magic:>10.3f}")


print(f"{'Trial #':>8}", end="")
print(f"{'Lower':>9}", end="")
print(f"{'Upper':>9}", end="")
print(f"{'Size':>9}", end="")
print(f"{'Mean':>14}", end="")
print(f"{'Variance':>16}", end="")
print(f"{'Magic':>10}")

for n in np.arange(1, 16):
    trial(n)
