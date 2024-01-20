# Pandigital Prime Sets
from itertools import permutations, product
import multiprocessing


def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if (x % i) == 0:
            return False
    return True


def get_sets(order: tuple) -> list:
    out = []
    for cut in product(range(2), repeat=8):
        l = []
        x = ''
        for i in range(8):
            x += order[i]
            if cut[i]:
                l.append(int(x))
                x = ''
        x += order[-1]
        l.append(int(x))
        for x in l:
            if not is_prime(x):
                break
        else:
            out.append(tuple(sorted(l)))
    return out


def main():
    digits = tuple(str(digit) for digit in range(1, 10))
    orders = permutations(digits)
    with multiprocessing.Pool() as pool:
        out = pool.map(get_sets, orders)
    print(len(set().union(*out)))


if __name__ == "__main__":
    main()
