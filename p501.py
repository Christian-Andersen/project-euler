# Eight Divisors
from itertools import combinations, product
from math import prod
from sympy import sieve

sieve.extend(1000)
PRIMES = list(sieve._list)
NUMBERS = set()


def get_divisor_count(x: int) -> int:
    count = 2
    for i in range(2, x):
        if (x % i) == 0:
            count += 1
    return count


def eight_divisors_less_than(n: int) -> int:
    count = 0
    for i in range(n + 1):
        if get_divisor_count(i) == 8:
            count += 1
    print(n, count)
    return count


def check_powers(powers: tuple[int, ...]) -> int:
    global NUMBERS
    for i in combinations(range(len(PRIMES)), len(powers)):
        number = prod(PRIMES[i[j]] ** powers[j] for j in range(len(powers)))
        NUMBERS.add(number)
    return 0


def main():
    for prime_factor_count in range(8):
        for powers in product(range(1, 8), repeat=prime_factor_count):
            if prod((power + 1) for power in powers) == 8:
                check_powers(powers)
    print(sum(1 for i in NUMBERS if i <= 100))
    print(sum(1 for i in NUMBERS if i <= 1000))
    print(sum(1 for i in NUMBERS if i <= 10**6))
    return
    assert eight_divisors_less_than(100) == 10
    assert eight_divisors_less_than(1000) == 180
    assert eight_divisors_less_than(10**6) == 224427


if __name__ == "__main__":
    main()
