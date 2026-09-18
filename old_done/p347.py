# Largest Integer Divisible by Two Primes
from numba import njit


@njit
def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    return all(x % i != 0 for i in range(2, int(x**0.5) + 1))


@njit
def m(p: int, q: int, n: int) -> int:
    x = p * q
    ps_power = 1
    maximum = x
    while True:
        x *= p
        ps_power += 1
        if x > n:
            break
        maximum = x
    x //= p
    ps_power -= 1
    while True:
        x *= q
        if x > n:
            x //= q
            if ps_power == 1:
                break
            x //= p
            ps_power -= 1
        else:
            maximum = max(maximum, x)
    return maximum


@njit
def main(n: int) -> int:
    primes = [i for i in range(n) if is_prime(i)]
    summed = 0
    for p in primes:
        for q in primes:
            if p == q:
                break
            if (p * q) > n:
                break
            summed += m(p, q, n)
    return summed


if __name__ == "__main__":
    print(main(10_000_000))
