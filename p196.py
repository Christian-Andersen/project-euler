# Prime Triplets
from sympy import numer, prime, sieve
from sympy.ntheory import isprime
from tqdm import tqdm


def get_triangular_number(n: int) -> int:
    return (n * (n + 1)) // 2


def get_row(n: int) -> list[int]:
    return list(range(get_triangular_number(n - 1) + 1, get_triangular_number(n) + 1))


sieve.extend(max(get_row(7208785 + 2)) ** 0.5)


def primes_around(x: int, y: int, rows: list[list[int]]):
    numbers = {}
    for dx, dy in [
        (-1, -1),
        (1, -1),
        (-1, 1),
        (1, 1),
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]:
        try:
            number = rows[y + dy][x + dx]
            if isprime(number):
                numbers[(x + dx, y + dy)] = number
        except IndexError:
            pass
    return numbers


def get_prime_triplets(n: int) -> set[int]:
    prime_triplets = []
    rows = []
    for i in [-2, -1, 0, 1, 2]:
        rows.append(get_row(n + i))
    y = 2
    for x, i in enumerate(rows[y]):
        if not isprime(i):
            continue
        numbers = primes_around(x, y, rows)
        if len(numbers) >= 2:
            prime_triplets.append(i)
            prime_triplets += list(numbers.values())
        if len(numbers) == 1:
            new_x, new_y = list(numbers.keys())[0]
            new_numbers = primes_around(new_x, new_y, rows)
            if len(new_numbers) >= 2:
                prime_triplets.append(i)
                prime_triplets += list(new_numbers.values())
    return set(prime_triplets).intersection(rows[y])


def get_answer(n: int) -> int:
    return sum(get_prime_triplets(n))


def main() -> None:
    assert get_answer(10000) == 950007619
    print(get_answer(5678027) + get_answer(7208785))


if __name__ == "__main__":
    main()
