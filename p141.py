# Square Progressive Numbers
from fractions import Fraction
from tqdm import trange


N = 10**12


def is_progressive(x: int) -> bool:
    for d in range(1, x):
        q, r = divmod(x, d)
        a, b, c = sorted([d, q, r])
        if (a * c) == (b * b):
            return True
    return False


def f(n: int) -> int:
    out = 0
    for i in range(int(n**0.5)):
        if is_progressive(i**2):
            out += i**2
    return out


def get_squares() -> set[int]:
    return set(i**2 for i in range(10**6))


SQUARES = get_squares()


def get_progressives() -> set[int]:
    out = set()
    for a in range(1, 10**12):
        for b in range(a + 1, 10**12):
            c, denominator = (Fraction(b, a) * b).as_integer_ratio()
            if denominator != 1:
                continue
            number_1 = a * c + b
            number_2 = b * c + a
            if number_1 >= N:
                break
            out.add(number_1)
            if number_2 < N:
                out.add(number_2)
        print(a, "-", sum(SQUARES.intersection(out)))
    return out


def main():
    numbers = get_progressives().intersection(get_squares())
    print(sum(numbers))
    # assert f(100_000) == 124657


if __name__ == "__main__":
    main()
