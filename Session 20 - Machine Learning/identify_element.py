# identify_element.py

import numpy as np
import matplotlib.pyplot as plt


def fit_linear(x, y):
    m = len(x) * np.sum(x * y) - np.sum(x) * np.sum(y)
    m = m / (len(x) * np.sum(x**2) - np.sum(x) ** 2)
    b = (np.sum(y) - m * np.sum(x)) / len(x)
    return m, b


# Read experiment data from data file
data = np.genfromtxt("gas.csv", delimiter=",")

# Convert experiment data to SI units
temperature = data[:, 0] + 273.15  # 1st column to kelvin
volume = data[:, 1] / 1000  # 2nd column to meters cubed

# Calculate line of best fit
slope, yint = fit_linear(temperature, volume)

# Apply Ideal gas law
p = 2.0 * 101_325  # Convert 2.0 atm (given) to pascals
r = 8.31446261815324  # Gas constant (SI units)
n = p / r * slope  # Moles of gas (rearrange ideal gas law equation)

# Calculate atomic mass of sample using number of moles
m_sample = 50  # (given) grams
molar_mass = m_sample / n  # sample mass divided by number of moles

plt.figure()
plt.scatter(temperature, volume, color="red")
t = np.linspace(0, 500)
plt.plot(t, slope * t + yint)
plt.title(f"Unknown Gas ({molar_mass:.3f}u)")
plt.xlabel("Temperature (K)")
plt.ylabel("Volume (m^3)")
plt.show()
