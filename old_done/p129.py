import sys
from itertools import count
from math import gcd

sys.set_int_max_str_digits(0)


def A(n: int) -> int:  # noqa: N802
    x = 0
    for k in range(1, 1_000_000):
        x = (10 * x) + 1
        if (x % n) == 0:
            return k
    print("Solution:", n)
    sys.exit()


def main() -> int | None:
    for n in count(1_000_000):
        if gcd(n, 10) == 1:
            print(n, A(n))
            return A(n)
    return None


if __name__ == "__main__":
    main()
