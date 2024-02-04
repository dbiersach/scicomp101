# prime_racer1.py

import numpy as np
import time


def is_prime(n):
    for factor in range(2, n):
        if n % factor == 0:
            return False
    return True


def main():
    np.random.seed(2016)
    num_primes = 0

    start_time = time.process_time()
    for _ in range(100_000):
        n = np.random.randint(1_000, 10_000)
        if is_prime(n):
            num_primes += 1
    elapsed_time = time.process_time() - start_time

    print(f"Number of primes found: {num_primes:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}")


main()
