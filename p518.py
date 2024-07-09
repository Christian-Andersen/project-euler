# Prime Triples and Geometric Sequences
import numpy as np
from sympy import sieve
from tqdm import tqdm


def S(n: int) -> int:
    sieve.extend(n)
    primes = np.array([i for i in sieve._list if i < n])
    squares = {}
    for b in primes:
        x = (b + 1) ** 2
        squares[x] = b
    answer = 0
    for i, c in tqdm(enumerate(primes), total=len(primes)):
        for j in range(i):
            a = primes[j]
            x = (a + 1) * (c + 1)
            if x in squares:
                answer += a + squares[x] + c
    return answer


def main():
    assert S(100) == 1035
    print(S(10**8))


if __name__ == "__main__":
    main()
