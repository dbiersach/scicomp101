# common_statistics.py

import numpy as np
import collections


def mean(s):
    return np.sum(s) / len(s)


def median(s):
    s.sort()
    i = len(s) // 2
    if len(s) % 2 == 1:
        return s[i]
    else:
        return (s[i - 1] + s[i]) / 2


def mode(s):
    c = collections.Counter(s)
    max_c = max(c.values())
    return [k for k, v in c.items() if v == max_c]


a = [] # An empty list
for _ in np.arange(30):
    a.append(np.random.randint(0, 100))

print(f"{a=}")
print(f"{mean(a)=}")
print(f"{median(a)=}")
print(f"{mode(a)=}")
