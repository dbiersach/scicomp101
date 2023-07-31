# prime_racer2.py

import numpy as np
from time import process_time


def is_prime():
    n = np.random.randint(100_000, 1_000_000)
    for i in range(2, int(np.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return 1


np.random.seed(2016)
c = 0

start_time: float = process_time()
for _ in range(10_000):
    c += is_prime()
elapsed_time: float = process_time() - start_time

print(f"Count of primes: {c}")
print(f"Elapsed time: {elapsed_time:.3f} s")
