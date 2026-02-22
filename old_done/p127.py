from math import gcd, prod
from functools import cache


def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if (x % i) == 0:
            return False
    return True


PRIMES = [i for i in range(120_000) if is_prime(i)]


@cache
def get_prime_factors(x):
    prime_factors = set()
    while x != 1:
        for p in PRIMES:
            div, mod = divmod(x, p)
            if mod == 0:
                x = div
                prime_factors.add(p)
    return prime_factors


def main():
    not_primes = [i for i in range(3, 120_000) if not is_prime(i)]
    total = 0
    for c in not_primes:
        for b in range(1 + (c // 2), c):
            if gcd(b, c) != 1:
                continue
            a = c - b
            if gcd(a, b) != 1:
                continue
            if gcd(a, c) != 1:
                continue
            if (
                prod(
                    get_prime_factors(a)
                    .union(get_prime_factors(b))
                    .union(get_prime_factors(c))
                )
                < c
            ):
                total += c
                print(c, total)
    return total


if __name__ == "__main__":
    main()
