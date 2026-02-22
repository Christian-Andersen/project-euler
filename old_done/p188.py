from numba import njit


@njit
def solve(a: int):
    x = 1
    for b in range(1, 10**6):
        temp_x = 1
        for _ in range(x):
            temp_x *= a
            temp_x %= 10**8
        x = temp_x
        x %= 10**8
        print(b, x)


def main():
    return solve(1777)


if __name__ == "__main__":
    main()
