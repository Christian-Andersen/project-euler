# Maximising a Weighted Product
import numpy as np
from numba import njit


@njit
def p(x, m):
    return np.prod(np.power(x, (1 + np.arange(m))))


@njit
def main():
    summed = 0
    for m in range(2, 15 + 1):
        lr = 2**-20
        d = 0
        best = 0
        while True:
            d += lr
            s = np.linspace(1 - d, 1 + d, m)
            if (s <= 0).any():
                break
            product = p(s, m)
            if product > best:
                best = product
        print(m, int(best))
        summed += int(best)
    print(summed)
    return summed


if __name__ == "__main__":
    main()
