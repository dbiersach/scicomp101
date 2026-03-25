#!/usr/bin/env -S uv run
"""identify_element.py"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


def fit_linear(x, y):
    m = len(x) * np.sum(x * y) - np.sum(x) * np.sum(y)
    m = m / (len(x) * np.sum(x**2) - np.sum(x) ** 2)
    b = (np.sum(y) - m * np.sum(x)) / len(x)
    return m, b


def main():
    # Load data
    file_name = "gas.csv"
    data = np.genfromtxt(file_name, delimiter=",")

    temperature = data[:, 0] + 273.15  # 1st column to kelvin
    volume = data[:, 1] / 1000  # 2nd column to meters cubed

    # Calculate line of best fit
    slope, yint = fit_linear(temperature, volume)

    p = 2.0 * 101_325  # Convert 2.0 atm (given) to pascals
    r = 8.31446261815324  # Gas constant (SI units)
    n = p / r * slope  # Moles of gas (rearrange ideal gas law equation)

    m_sample = 50  # (given) grams
    atomic_mass = m_sample / n  # sample mass divided by number of moles

    # Plot data and line of best fit
    plt.figure(Path(__file__).name)
    plt.scatter(temperature, volume, color="red")
    t = np.linspace(0, 500)
    plt.plot(t, slope * t + yint)
    plt.title(f"Unknown Gas ({atomic_mass:.3f}u)")
    plt.xlabel(r"Temperature $(\degree K)$")
    plt.ylabel("Volume ($m^3$)")
    plt.show()


if __name__ == "__main__":
    main()
