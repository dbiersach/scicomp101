# plot_trajectory.py

import numpy as np
import matplotlib.pyplot as plt


def fit_linear(x, y):
    m = len(x) * np.sum(x * y) - np.sum(x) * np.sum(y)
    m = m / (len(x) * np.sum(x**2) - np.sum(x) ** 2)
    b = (np.sum(y) - m * np.sum(x)) / len(x)
    return m, b


# Read experiment data from data file
data = np.genfromtxt("ray.csv", delimiter=",")
t = data[:, 0]  # time in nanoseconds
h = data[:, 1]  # height in centimeters

# Calculate line of best fit
slope, yint = fit_linear(t, h)

# Insert your code here

# Calculate origination height and initial velocity
oh = (slope * 1e9 / 100) * (0.1743 / 1e3) / 1000
c = 29.98  # speed of light in cm/ns
v = slope / c

# Do not edit the remaining code
print(f"Slope = {slope:.4f} cm/ns")
print(f"Velocity = {v:.2f} c")
print(f"Origination Height = {oh:,.2f} km")

plt.figure()
plt.scatter(t, h)
plt.plot(t, slope * t + yint, color="red", linewidth=2)
plt.title("Secondary Cosmic Ray Trajectory")
plt.xlabel("Time (ns)")
plt.ylabel("Height (cm)")
plt.grid()
plt.show()
