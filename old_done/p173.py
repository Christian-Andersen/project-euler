from numba import njit


@njit
def main():
    counter = 0
    size = 0
    while True:
        size += 1
        for size_diff in range(2, size, 2):
            hole_size = size - size_diff
            tiles_used = size**2 - hole_size**2
            if tiles_used <= 1_000_000:
                counter += 1
        if (size % 100_000) == 0:
            print(counter)
            return counter


if __name__ == "__main__":
    main()
