# random_straws.py

import numpy as np


# Insert your code here
def run_trial():
    total_length = 0.0
    num_straws = 0
    while total_length <= 1.0:
        total_length += 1 - np.random.rand()
        num_straws += 1
    return num_straws


# Do not edit the remaining code
trials = 1_000_000
straws = 0

for _ in np.arange(trials):
    straws += run_trial()

print(straws / trials)
print(np.e)
