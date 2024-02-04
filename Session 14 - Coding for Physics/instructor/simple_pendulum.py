# simple_pendulum.py

import numpy as np
import matplotlib.pyplot as plt

# Set simulation duration
tf = 10  # final time (secs)
ts = 500  # time steps
dt = tf / ts  # delta time

# Intialize arrays
t = np.zeros(ts)
omega = np.zeros(ts)
theta = np.zeros(ts)

# Set initial conditions
theta[0] = np.deg2rad(45)
g = 9.81  # gravity (m/s^2)
l = 1.0  # pendulum length (m)

# Calculate omega and theta at each next time step
for i in range(ts - 1):
    t[i + 1] = t[i] + dt
    omega[i + 1] = omega[i] - g / l * np.sin(theta[i]) * dt
    theta[i + 1] = theta[i] + omega[i + 1] * dt

# Plot omega and theta over time
plt.figure("simple_pendulum.py")
(plot1,) = plt.plot(t, theta)
(plot2,) = plt.plot(t, omega)
plt.title("Simple Pendulum")
plt.xlabel("Time (s)")
plt.ylabel("Angular Displacement (rad)")
plt.twinx()
plt.ylabel("Angular Velocity (rad/s)")
legend_lines = [plot1, plot2]
legend_labels = [r"$\theta$", r"$\omega$"]
plt.legend(legend_lines, legend_labels)
plt.grid()
plt.show()
