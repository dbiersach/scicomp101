# pendulum.py

import numpy as np
import matplotlib.pyplot as plt

g = 9.81  # gravity (m/s^2)
l = 1.0  # pendulum length (m)
tf = 10  # final time (s)

ts = 500  # time steps
dt = tf / ts  # delta t

t = np.zeros(ts)
omega = np.zeros(ts)
theta = np.zeros(ts)

theta[0] = np.deg2rad(10)

for i in range(ts - 1):
    t[i + 1] = t[i] + dt
    omega[i + 1] = omega[i] - g / l * theta[i] * dt
    theta[i + 1] = theta[i] + omega[i] * dt

plt.figure()
plt.plot(t, theta, label=r"$\theta$")
plt.plot(t, omega, label=r"$\omega$")
plt.title("Simple Pendulum")
plt.xlabel("Seconds")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
