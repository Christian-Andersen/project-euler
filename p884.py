# Removing Cubes
from tqdm import trange
import numpy as np

CUBES = np.arange(10**6) ** 3

N = 10000
D = {}
for i in range(N):
    D[i] = CUBES[CUBES.searchsorted(i, side="right") - 1]


class cubic_base:
    def __init__(self) -> None:
        self.number = 20 * [0]

    def to_base_10(self):
        out = 0
        for base, mul in enumerate(self.number):
            out += mul * ((base + 1) ** 3)
        return out

    def add_one(self):
        self.number[0] += 1
        for base, mul in enumerate(self.number):
            if mul >= (base + 2) ** 3:
                self.number[base] = 0
                self.number[base + 1] += 1


def largest_cube_less_than(n: int) -> int:
    if n < N:
        return D[n]
    return CUBES[CUBES.searchsorted(n, side="right") - 1]


def d(x: int) -> int:
    count = 0
    while x != 0:
        x -= largest_cube_less_than(x)
        count += 1
    return count


def s(n: int) -> int:
    out = 0
    for i in range(n):
        out += d(i)
    return out


def main():
    x = cubic_base()
    for i in range(2, 250):
        x.add_one()
        # if i != x.to_base_10():
        print(i, x.number, x.to_base_10())
    return
    assert s(100) == 512
    n = 10**17
    print(s(n))


if __name__ == "__main__":
    main()
