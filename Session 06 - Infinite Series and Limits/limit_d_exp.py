#!/usr/bin/env -S uv run
"""limit_d_exp.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Calculate (e^x - 1) / x
x = np.linspace(-4, 4, 1000)
y = (np.exp(x) - 1) / x

# Plot the function
plt.figure(Path(__file__).name, figsize=(10, 6))
plt.plot(x, y, "b-", linewidth=1.5, label=r"$f(x) = \dfrac{e^x - 1}{x}$")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)

# Mark the limit point at x=0, y=1
plt.plot(
    0,
    1,
    "ro",
    markersize=8,
    label=r"$\lim_{x \to 0} \dfrac{e^x - 1}{x} = 1$",
)
plt.axhline(1, color="red", linestyle="--", linewidth=1, alpha=0.5)

# Set title, labels, and limits
plt.title(
    r"Derivative of $e^x$ at the Origin: $\lim_{x \to 0} \dfrac{e^x - 1}{x} = 1$",
    fontsize=14,
)
plt.xlabel(r"$x$", fontsize=12)
plt.ylabel(r"$y$", fontsize=12)
plt.xlim(-4, 4)
plt.ylim(-1, 6)
plt.gca().xaxis.set_major_locator(plt.MultipleLocator(1))
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda val, pos: f"{val:.2f}"))
plt.gca().yaxis.set_major_locator(plt.MultipleLocator(1))
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda val, pos: f"{val:.2f}"))
plt.gca().xaxis.set_minor_locator(plt.MultipleLocator(0.25))
plt.gca().yaxis.set_minor_locator(plt.MultipleLocator(0.25))
plt.grid(True, which="major", linestyle="-", linewidth=0.5, alpha=0.9)
plt.grid(True, which="minor", linestyle=":", linewidth=0.3, alpha=0.8)
plt.legend(loc="upper left", fontsize=10)
plt.tight_layout()
plt.show()
