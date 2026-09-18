# Maximum Product of Parts
from fractions import Fraction
from math import e

from sympy import primefactors

FACTORS = {2, 5}
N = 10000


def m(n: Fraction) -> Fraction:
    out = Fraction(0)
    for k in range(1, int(n + 1)):
        x = (n / k) ** k
        if x > out:
            out = x
        else:
            break
    return out


def m2(n: Fraction) -> Fraction:
    k = round(n / e)
    return (n / k) ** k


def is_terminating(m_n: Fraction) -> bool:
    return len(FACTORS.union(primefactors(m_n.denominator))) == 2  # noqa: PLR2004


def d(n: Fraction) -> Fraction:
    if is_terminating(m2(n)):
        return -n
    return n


def main() -> int | Fraction:
    assert sum(d(Fraction(n)) for n in range(5, 100 + 1)) == 2438  # noqa: S101, PLR2004
    return sum(d(Fraction(n)) for n in range(5, N + 1))


if __name__ == "__main__":
    main()
