# Modular Inverses
from tqdm import trange
from sympy import isprime, sieve


N = 10**4
sieve.extend(N)


def I(n: int) -> int:
    if isprime(n):
        return 1
    for dif in range(2, n):
        if ((dif**2) % n) == 1:
            return n - dif
    return 0


def main():
    answers = set()
    numbers = set(range(3, 2 * N + 1))
    new_numbers = set()
    for number in numbers:
        if isprime(number):
            answers.add(1)
        else:
            new_numbers.add(number)
    numbers = new_numbers
    for dif in range(2, N):
        x = dif**2
        new_numbers = set()
        for number in numbers:
            if x % number == 1:
                answers.add(number - dif)
            else:
                new_numbers.add(number)
        numbers = new_numbers
        print(dif, len(numbers))
    assert I(7) == 1
    assert I(15) == 11
    assert I(100) == 51
    sum(I(n) for n in trange(3, 2 * (N) + 1))


if __name__ == "__main__":
    main()
