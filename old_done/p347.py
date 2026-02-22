# Largest Integer Divisible by Two Primes
from numba import njit


@njit
def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if (x % i) == 0:
            return False
    return True


@njit
def M(p: int, q: int, N: int) -> int:
    x = p * q
    ps_power = 1
    maximum = x
    while True:
        x *= p
        ps_power += 1
        if x > N:
            break
        maximum = x
    x //= p
    ps_power -= 1
    while True:
        x *= q
        if x > N:
            x //= q
            if ps_power == 1:
                break
            x //= p
            ps_power -= 1
        else:
            maximum = max(maximum, x)
    return maximum


@njit
def main(N: int) -> int:
    PRIMES = [i for i in range(N) if is_prime(i)]
    summed = 0
    for p in PRIMES:
        for q in PRIMES:
            if p == q:
                break
            if (p * q) > N:
                break
            summed += M(p, q, N)
    return summed


if __name__ == "__main__":
    print(main(10_000_000))
