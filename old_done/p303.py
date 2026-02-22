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
    if n < 3:
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


def main():
    assert f(2) * 2 == 2
    assert f(3) * 3 == 12
    assert f(7) * 7 == 21
    assert f(42) * 42 == 210
    assert f(89) * 89 == 1121222
    assert (sum(f(n) for n in range(1, 100 + 1))) == 11363107
    answer = sum(f(n) for n in trange(1, 10000 + 1))
    return answer


if __name__ == "__main__":
    main()
