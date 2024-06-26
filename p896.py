# Divisible Ranges
from sympy import primefactors


def is_divisible_range(n: list[int]) -> bool:
    return True  # TODO


def get_divisible_ranges(n: int) -> None:
    count = 0
    end_idx = n
    while True:
        end_idx += 1
        l = list(range(end_idx - n, end_idx))
        print(l)
        continue
        if is_divisible_range(l):
            count += 1
            print(count, l)


def main():
    n = 4
    get_divisible_ranges(n)


if __name__ == "__main__":
    main()
