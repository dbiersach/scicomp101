# collatz_conjecture.py

import numpy as np
import matplotlib.pyplot as plt
import numba


# Insert your code here












# Do not edit the remaining code
def main():
    max_n = 1_000_000
    x = np.arange(max_n)
    f = np.vectorize(stop_time)
    y = f(x)
    plt.figure("collatz_conjecture.py")
    plt.hist(y, bins=500, color="blue")
    plt.title(f"Collatz Conjecture (n < {max_n:,})")
    plt.xlabel("Stopping Time")
    plt.ylabel("Count")
    plt.show()


main()
