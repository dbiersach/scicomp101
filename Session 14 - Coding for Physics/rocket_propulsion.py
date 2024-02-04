# rocket_propulsion.py

import numpy as np
import matplotlib.pyplot as plt

# Set simulation duration
tf = 5  # final time (secs)
ts = 200  # time steps
dt = tf / ts  # delta time

# Intialize arrays
t = np.zeros(ts)
m = np.zeros(ts)
a = np.zeros(ts)
v = np.zeros(ts)
s = np.zeros(ts)

# Set initial conditions
m[0] = 2.0  # initial mass = 2 kg
a[0] = 0.5  # inital accel = 0.5 m/s^2

# Calculate values at each next time step
# Insert your code here





# Do not edit the remaining code
# Display final distance
print(f"s = {s[-1]:.4f} m")

# Plot values over time
plt.figure("rocket_propulsion.py")
plt.plot(t, m, label="mass (kg)")
plt.plot(t, a, label="accel (m/s^2)")
plt.plot(t, v, label="velocity (m/s)")
plt.plot(t, s, label="distance (m)")
plt.title("Rocket Propulsion")
plt.xlabel("Seconds")
plt.ylabel("Amplitude")
plt.legend()
plt.grid()
plt.show()
