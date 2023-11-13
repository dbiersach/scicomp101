# nuclear_decay.py

import numpy as np
import matplotlib.pyplot as plt

tau = 5_730  # half-life in years
tf = 40_000  # time (final) in years
ts = 100  # time steps
dt = tf / ts  # delta t

t = np.zeros(ts)
n = np.zeros(ts)
n[0] = 100  # initial % concentration

for i in range(ts - 1):
    t[i + 1] = t[i] + dt
    n[i + 1] = n[i] - n[i] / tau * dt

plt.figure("nuclear_decay.py")
plt.plot(t, n)
plt.title("Carbon-14 Decay")
plt.xlabel("Time (years)")
plt.ylabel("% Concentration")
plt.show()
