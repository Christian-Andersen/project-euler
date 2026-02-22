# Maximum Product of Parts
from sympy import primefactors
from fractions import Fraction
from math import e


FACTORS = set([2, 5])
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
    if len(FACTORS.union(primefactors(m_n.denominator))) == 2:
        return True
    return False


def d(n: Fraction) -> Fraction:
    if is_terminating(m2(n)):
        return -n
    return n


def main():
    assert sum(d(Fraction(n)) for n in range(5, 100 + 1)) == 2438
    answer = sum(d(Fraction(n)) for n in range(5, N + 1))
    return answer


if __name__ == "__main__":
    main()
