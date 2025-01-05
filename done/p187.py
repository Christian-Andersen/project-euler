from tqdm import trange
import numpy as np

N = 10**8

primes = np.ones(int(N / 2), dtype=bool)
length = len(primes)
primes[[0, 1]] = False
for p in trange(2, length):
    if not primes[p]:
        continue
    primes[p * np.arange(2, np.ceil(length / p), dtype=np.uint32)] = False

primes = np.nonzero(primes)[0]
length_primes = len(primes)

count = 0
for i in trange(length_primes):
    for j in range(length_primes):
        product = primes[i] * primes[i + j]
        if product >= N:
            break
        count += 1
print(count)
