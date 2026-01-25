#!/usr/bin/env -S uv run
"""limit_conjugate.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Calculate sqrt(x^2 + x) - x for positive x
x = np.linspace(0.0, 50, 1000)
y = np.sqrt(x**2 + x) - x

# Plot the function
fig, ax = plt.subplots(num=Path(__file__).name, figsize=(10, 6))

ax.plot(x, y, "b-", linewidth=1.5, label=r"$f(x) = \sqrt{x^2 + x} - x$")
ax.axhline(0, color="black", linewidth=0.5)
ax.axvline(0, color="black", linewidth=0.5)

# Mark the limit value y = 1/2
ax.plot(
    50,
    0.5,
    "ro",
    markersize=8,
    label=r"$\lim_{x \to \infty} \left(\sqrt{x^2 + x} - x\right) = \dfrac{1}{2}$",
)

# Horizontal asymptote at y = 1/2
ax.axhline(0.5, color="red", linestyle="--", linewidth=1, alpha=0.5)

# ---- Labels and title ----
ax.set_xlabel(r"$x$", fontsize=12)
ax.set_ylabel(r"$y$", fontsize=12)
ax.set_title(
    r"A Radical Difference Limit: $\lim_{x \to \infty} \left(\sqrt{x^2 + x} - x\right) = \dfrac{1}{2}$",
    fontsize=14,
)

# ---- Axis limits ----
ax.set_xlim(0, 50)
ax.set_ylim(0, 1)

# ---- Major ticks with 2 decimal places ----
ax.xaxis.set_major_locator(plt.MultipleLocator(10))
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda val, pos: f"{val:.2f}"))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.25))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda val, pos: f"{val:.2f}"))

# ---- Minor ticks ----
ax.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.05))

# ---- Grid ----
ax.grid(True, which="major", linestyle="-", linewidth=0.5, alpha=0.9)
ax.grid(True, which="minor", linestyle=":", linewidth=0.3, alpha=0.8)

# ---- Legend ----
ax.legend(loc="upper right", fontsize=10)

plt.tight_layout()
plt.show()
