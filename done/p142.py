# Perfect Square Collection
from numba import njit


@njit
def main():
    squares_list = [i**2 for i in range(1, 10**6)]
    squares = set(squares_list)
    squares_list = squares_list[:10000]
    z = 0
    while True:
        z += 1
        for d1 in squares_list:
            if (z + z + d1) not in squares:
                continue
            for d2 in squares_list:
                if (d1 + d2) not in squares:
                    continue
                if (z + z + d1 + d2) not in squares:
                    continue
                if (z + z + d1 + d1 + d2) not in squares:
                    continue
                x = z + d1 + d2
                y = z + d1
                print(x, y, z, x + y + z)


if __name__ == "__main__":
    main()
