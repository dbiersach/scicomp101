#!/usr/bin/env -S uv run
"""lcm_from_gcd_instructor.py"""

import numpy as np

a = 447618
b = 2011835

lcm = a * b // np.gcd(a, b)

print(f"a = {a:,}")
print(f"b = {b:,}")
print(f"lcm(a, b) = {lcm:,}")
print(f"lcm(a, b) = {np.lcm(a, b):,}")
