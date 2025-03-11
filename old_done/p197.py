# A Recursively Defined Sequence
from decimal import Decimal
import math


def f(x: Decimal) -> Decimal:
    return math.floor(2 ** (Decimal("30.403243784") - x**2)) * (
        Decimal(10) ** Decimal(-9)
    )


def main():
    u = [Decimal(-1)]
    for n in range(1, 1000000000000):
        u.append(f(u[-1]))
        print(u[-1])
        return u[-1]


if __name__ == "__main__":
    main()
