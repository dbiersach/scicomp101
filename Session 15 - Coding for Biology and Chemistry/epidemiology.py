# epidemiology.py

import numpy as np
import matplotlib.pyplot as plt

# Set simulation duration
tf = 10  # time final (simulate 10 months of the disease)
ts = 100  # time steps (tally compartments ~twice a week)
dt = tf / ts  # delta t

# Intialize arrays
t = np.zeros(ts)  # Time stamps
s = np.zeros(ts)  # Number of susceptible people
i = np.zeros(ts)  # Number of infected people
r = np.zeros(ts)  # Number of recovered people

# Set initial conditions
s[0] = 1000  # Initial tally of susceptible people
i[0] = 1  # Intial tally of infected people
beta = 0.003  # Infection rate
delta = 1  # Recovery rate

# Calculate S-I-R populations at each next time step
for n in range(ts - 1):
    t[n + 1] = t[n] + dt
    s[n + 1] = s[n] + (-beta * s[n] * i[n]) * dt
    i[n + 1] = i[n] + (beta * s[n] * i[n] - delta * i[n]) * dt
    r[n + 1] = r[n] + (delta * i[n]) * dt

# Plot S-I-R compartment populations over time
plt.plot(t, s, linewidth=2, label="Susceptible")
plt.plot(t, i, linewidth=2, label="Infected")
plt.plot(t, r, linewidth=2, label="Recovered")
plt.title("Epidemiology (Kermack-McKendrick)")
plt.xlabel("Time (months)")
plt.ylabel("Population")
plt.legend()
plt.show()
