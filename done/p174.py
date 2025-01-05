# Hollow Square Laminae II
from numba import njit


@njit
def number_of_ways():
    counter = 1000001 * [0]
    size = 0
    while True:
        size += 1
        for size_diff in range(2, size, 2):
            hole_size = size - size_diff
            tiles_used = size**2 - hole_size**2
            if tiles_used <= 1_000_000:
                counter[tiles_used] += 1
        if (size % 100_000) == 0:
            big_n = 10 * [0]
            for n in range(1, 11):
                for i in counter:
                    if i == n:
                        big_n[n - 1] += 1
            print(sum(big_n))


def main():
    number_of_ways()


if __name__ == "__main__":
    main()
