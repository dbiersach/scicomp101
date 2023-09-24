# birthday_paradox.py

import numpy as np
import matplotlib.pyplot as plt
import numba


@numba.njit
def shared_birthdays(class_size):
    b = np.random.randint(0, 365, class_size)
    for i in range(b.size - 2):
        for j in range(i + 1, b.size):
            if b[i] == b[j]:
                return True
    return False


@numba.njit
def calc_probabilities():
    p = np.zeros(max_size)
    for c in range(max_size):
        n = 0
        for _ in range(total_classes):
            if shared_birthdays(c):
                n = n + 1
        p[c] = n / total_classes
    return p


print("This can take up to 30 seconds . . .")

total_classes = 10_000
max_size = 80

prob = calc_probabilities()
min_class_size = np.where(prob > 0.50)[0][0]

x = np.linspace(0, 80, 500)
y = 1.0 - np.exp(-(x**2) / 730)

plt.figure()
plt.step(    
    range(max_size),
    prob,
    color="black",
    linewidth=3,
    label="Estimated",
)
plt.plot(x, y, color="blue", label="Actual")
plt.legend()
plt.title(f"Birthday Paradox ({total_classes:,} classes)")
plt.xlabel("Class Size")
plt.ylabel("Probability")
plt.vlines(min_class_size, 0, prob[min_class_size], color="red")
plt.annotate(
    f"Min Class Size = {min_class_size}",
    xy=(min_class_size, prob[min_class_size]),
    xytext=(28, 0.45),
    arrowprops={"facecolor": "black"},
)
plt.show()
