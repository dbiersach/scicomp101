#!/usr/bin/env -S uv run
"""limit_d_exp.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Calculate (e^x - 1) / x
x = np.linspace(-4, 4, 1000)
y = (np.exp(x) - 1) / x

# Plot the function
fig, ax = plt.subplots(num=Path(__file__).name, figsize=(10, 6))

ax.plot(x, y, "b-", linewidth=1.5, label=r"$f(x) = \dfrac{e^x - 1}{x}$")
ax.axhline(0, color="black", linewidth=0.5)
ax.axvline(0, color="black", linewidth=0.5)

# Mark the limit point at x=0, y=1
ax.plot(
    0,
    1,
    "ro",
    markersize=8,
    label=r"$\lim_{x \to 0} \dfrac{e^x - 1}{x} = 1$",
)

# Horizontal line at y=1
ax.axhline(1, color="red", linestyle="--", linewidth=1, alpha=0.5)

# ---- Labels and title ----
ax.set_xlabel(r"$x$", fontsize=12)
ax.set_ylabel(r"$y$", fontsize=12)
ax.set_title(
    r"Derivative of $e^x$ at the Origin: $\lim_{x \to 0} \dfrac{e^x - 1}{x} = 1$",
    fontsize=14,
)

# ---- Axis limits ----
ax.set_xlim(-4, 4)
ax.set_ylim(-1, 6)

# ---- Major ticks with 2 decimal places ----
ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda val, pos: f"{val:.2f}"))
ax.yaxis.set_major_locator(plt.MultipleLocator(1))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda val, pos: f"{val:.2f}"))

# ---- Minor ticks ----
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.25))

# ---- Grid ----
ax.grid(True, which="major", linestyle="-", linewidth=0.5, alpha=0.9)
ax.grid(True, which="minor", linestyle=":", linewidth=0.3, alpha=0.8)

# ---- Legend ----
ax.legend(loc="upper left", fontsize=10)

plt.tight_layout()
plt.show()
