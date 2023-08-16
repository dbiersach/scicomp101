# random_straws.py

import numpy as np

# Insert your code here


# Do not edit the remaining code
trials = 1_000_000
straws = 0

for _ in np.arange(trials):
    straws += run_trial()

print(straws / trials)
print(np.e)
