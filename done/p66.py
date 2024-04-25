import decimal
from math import isclose
from functools import cache

decimal.getcontext().prec = 100
SQUARES = set(i**2 for i in range(100))


@cache
def h(n, a):
    if n == -2:
        return 0
    if n == -1:
        return 1
    return a[n]*h(n-1, a) + h(n-2, a)


@cache
def k(n, a):
    if n == -2:
        return 1
    if n == -1:
        return 0
    return a[n]*k(n-1, a) + k(n-2, a)


def get_continued_fraction(r, length):
    a = []
    for _ in range(length):
        r_floor = int(r)
        a.append(r_floor)
        diff = r - r_floor
        if isclose(diff, 0, rel_tol=0, abs_tol=1e-09):
            break
        r = decimal.Decimal(1)/diff
    return a


unsolved = list(range(2, 1_000+1))
largest = 0
for depth_power in range(1, 6):
    for D in unsolved.copy():
        if D in SQUARES:
            continue
        r = decimal.Decimal(D).sqrt()
        a = tuple(get_continued_fraction(r, 10**depth_power))
        for i in range(0, len(a)):
            x = h(i, a)
            y = k(i, a)
            if (x**2 - D*(y**2)) == 1:
                if x >= largest:
                    largest = x
                    print(D, x)
                unsolved.remove(D)
                break
