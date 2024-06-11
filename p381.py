# (prime-k) Factorial
from sympy import isprime
from tqdm import trange


def factorial_mod(x: int, m: int) -> int:
    ans = 1
    for i in trange(1, x + 1):
        ans = (ans * i) % m
    return ans


def s(p: int) -> int:
    previous_factorial = factorial_mod(p - 5, p)
    ans = previous_factorial
    for k in [4, 3, 2, 1]:
        previous_factorial = (previous_factorial * (p - k)) % p
        ans = (ans + previous_factorial) % p
    return ans


def s_sum(n: int) -> int:
    return sum(s(p) for p in range(n, 5 - 1, -1) if isprime(p))


def main():
    assert s(7) == 4
    assert s_sum(100) == 480
    print(s_sum(10**8))


if __name__ == "__main__":
    main()
