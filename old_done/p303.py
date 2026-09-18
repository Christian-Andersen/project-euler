# Multiples with Small Digits
from tqdm import trange

VALID_DIGITS = ("0", "1", "2")


def check_digits(str_x: str) -> int:
    for idx, digit in enumerate(str_x):
        if digit not in VALID_DIGITS:
            return idx
    return -1


def f(n: int) -> int:
    # print(f"{n = }")
    if n < 3:  # noqa: PLR2004
        return 1
    x = n
    while True:
        str_x = str(x)
        out = check_digits(str_x)
        if out == -1:
            return x // n
        new_x = list(str_x)
        for i in range(out, len(new_x)):
            new_x[i] = "9"
        new_x = int("".join(new_x))
        x = new_x - (new_x % n) + n


def main() -> int:
    assert f(2) * 2 == 2  # noqa: S101, PLR2004
    assert f(3) * 3 == 12  # noqa: S101, PLR2004
    assert f(7) * 7 == 21  # noqa: S101, PLR2004
    assert f(42) * 42 == 210  # noqa: S101, PLR2004
    assert f(89) * 89 == 1121222  # noqa: S101, PLR2004
    assert (sum(f(n) for n in range(1, 100 + 1))) == 11363107  # noqa: S101, PLR2004
    return sum(f(n) for n in trange(1, 10000 + 1))


if __name__ == "__main__":
    main()
