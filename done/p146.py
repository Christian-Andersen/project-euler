# Investigating a Prime Pattern
from sympy import sieve, isprime
from tqdm import trange

N = 150_000_000
sieve.extend(N)


def is_special(x: int) -> bool:
    x_squared = x**2
    for i in [1, 3, 7, 9, 13, 27]:
        if not isprime(x_squared + i):
            return False
    for i in [11, 17, 19, 21, 23]:
        if isprime(x_squared + i):
            return False
    return True


def sum_up_to(n: int) -> int:
    answers = []
    for i in trange(10, n, 10):
        if is_special(i):
            answers.append(i)
            print(i)
    return sum(answers)


def main():
    assert sum_up_to(1_000_000) == 1242490
    print(sum_up_to(N))


if __name__ == "__main__":
    main()
