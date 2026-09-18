import numpy as np
from tqdm import tqdm, trange

N = 100_000_000

primes_bool = np.ones(N, dtype=bool)
length = len(primes_bool)
primes_bool[[0, 1]] = False
for p in trange(2, length):
    if not primes_bool[p]:
        continue
    primes_bool[p * np.arange(2, np.ceil(length / p), dtype=np.uint32)] = False
primes = np.nonzero(primes_bool)[0]
primes_set = set(primes)
# valid must be under a prime (1+x/1)=(x+1)
valid_numbers = primes - 1
# one below prime -> even -> has divisor 2
# this means that 2+(x/2) must be in primes
valid_numbers = valid_numbers[np.isin(2 + np.divide(valid_numbers, 2).round(), primes)]


def check(x: int) -> bool:
    divs, mods = np.divmod(x, np.arange(1, int(x**0.5) + 1))
    divisors_bool = np.equal(mods, 0)
    summed = 1 + np.nonzero(divisors_bool)[0] + divs[divisors_bool]
    return all(summ in primes_set for summ in summed)


def main() -> None:
    summed = 0
    for n in tqdm(valid_numbers):
        if check(n):
            summed += n
    print(summed)


if __name__ == "__main__":
    main()
