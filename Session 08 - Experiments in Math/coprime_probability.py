#!/usr/bin/env -S uv run
"""coprime_probability.py"""

import numpy as np

p = 1

print(f"Coprime Probability = {p:.2%}")
print(f"Hidden constant     = {np.sqrt(6 / p):.3f}")
