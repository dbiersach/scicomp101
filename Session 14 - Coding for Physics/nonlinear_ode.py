# nonlinear_ode.py

import numpy as np
import matplotlib.pyplot as plt


def dy(x, y):
    return y * np.cos(x)


def main():
    xf = 12 * np.pi  # final x value
    xs = 1000  # total steps across x-axis
    dx = xf / xs  # step size across x-axis

    x = np.zeros(xs)
    y1 = np.zeros(xs)
    y2 = np.zeros(xs)

    y1[0] = 1
    y2[0] = 1

    for i in range(xs - 1):
        x[i + 1] = x[i] + dx

        # Euler's Method
        y1[i + 1] = y1[i] + dy(x[i], y1[i]) * dx

        # 4th Order Runge-Kutta Method
        k1 = dy(x[i], y2[i])
        k2 = dy(x[i], y2[i] + k1 / 2 * dx)
        k3 = dy(x[i], y2[i] + k2 / 2 * dx)
        k4 = dy(x[i], y2[i] + k3 * dx)
        y2[i + 1] = y2[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6 * dx

    plt.figure("nonlinear_ode.py")
    plt.plot(x, y1, label="Euler")
    plt.plot(x, y2, label="RK4")
    plt.title("Nonlinear ODE")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.show()


main()
