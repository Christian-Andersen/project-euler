from numba import njit


@njit
def main():
    n = 1
    while True:
        n += 1
        solutions = 1
        for x in range(n + 1, 2 * n):
            y = round(x * n / (x - n))
            if (x * n) == (y * (x - n)):
                solutions += 1
            continue
        if solutions >= 1000:
            print(n)
            return n


if __name__ == "__main__":
    main()
