# Pythagorean Tiles
from math import gcd
from numba import njit


@njit
def main():
    counter = 0
    for m in range(1, 100_000_000):
        for n in range(1, m):
            if ((m % 2) == 1) and ((n % 2) == 1):
                continue
            if gcd(m, n) != 1:
                continue
            a_prim = m**2 - n**2
            b_prim = 2 * m * n
            c_prim = m**2 + n**2
            if (a_prim + b_prim + c_prim) >= 100_000_000:
                break
            k = 0
            while True:
                k += 1
                a = k * a_prim
                b = k * b_prim
                c = k * c_prim
                if (a + b + c) >= 100_000_000:
                    break
                square_area = c**2
                hole_area = square_area - 2 * a * b
                hole_side = round(hole_area**0.5)
                assert (hole_side**2) == hole_area
                if (c % hole_side) == 0:
                    counter += 1
    print(counter)


main()
