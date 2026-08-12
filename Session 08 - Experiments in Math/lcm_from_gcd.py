#!/usr/bin/env -S uv run
"""lcm_from_gcd.py"""

import numpy as np

a = 447618
b = 2011835

lcm = 0

print(f"a = {a:,}")
print(f"b = {b:,}")
print(f"lcm(a, b) = {lcm:,}")
print(f"lcm(a, b) = {np.lcm(a, b):,}")
