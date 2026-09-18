import sys

sys.set_int_max_str_digits(0)


def check_end(x: int) -> bool:
    s = set(str(x % 1000000000))
    if "0" in s:
        return False
    return len(s) == 9  # noqa: PLR2004


def check_start(x: int) -> bool:
    s = set(str(x)[:9])
    if "0" in s:
        return False
    return len(s) == 9  # noqa: PLR2004


def main() -> int:
    f_1 = f_2 = 1
    k = 2
    while True:
        f_1 += f_2
        f_2 += f_1
        k += 2
        if check_end(f_1) and check_start(f_1):
            return k - 1
        if check_end(f_2) and check_start(f_2):
            return k


if __name__ == "__main__":
    main()
