#!/usr/bin/env -S uv run
"""limit_exp.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Calculate (1+x)^(1/x)
x = np.linspace(-1, 5, 1000)
y = (1 + x) ** (1 / x)

# Plot the function
fig, ax = plt.subplots(num=Path(__file__).name, figsize=(10, 6))

ax.plot(x, y, "b-", linewidth=1.5, label=r"$f(x) = (1+x)^{1/x}$")
ax.axhline(0, color="black", linewidth=0.5)
ax.axvline(0, color="black", linewidth=0.5)

# Mark the limit point at x=0, y=e
ax.plot(
    0,
    np.e,
    "ro",
    markersize=8,
    label=rf"$\lim_{{x \to 0}} (1+x)^{{1/x}} = e \approx {np.e:.4f}$",
)

# Horizontal line at y=e
ax.axhline(np.e, color="red", linestyle="--", linewidth=1, alpha=0.5)


# ---- Labels and title ----
ax.set_xlabel(r"$x$", fontsize=12)
ax.set_ylabel(r"$y$", fontsize=12)
ax.set_title(
    r"The Limit Definition of $e$: $\lim_{x \to 0} (1+x)^{1/x} = e$",
    fontsize=14,
)

# ---- Axis limits ----
ax.set_xlim(-1, 5)
ax.set_ylim(0, 4)

# ---- Major ticks with 2 decimal places ----
ax.xaxis.set_major_locator(plt.MultipleLocator(1))
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda val, pos: f"{val:.2f}"))
ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda val, pos: f"{val:.2f}"))

# ---- Minor ticks ----
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.25))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.1))

# ---- Grid ----
ax.grid(True, which="major", linestyle="-", linewidth=0.5, alpha=0.9)
ax.grid(True, which="minor", linestyle=":", linewidth=0.3, alpha=0.8)

# ---- Legend ----
ax.legend(loc="upper right", fontsize=10)

plt.tight_layout()
plt.show()
