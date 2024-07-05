# Idempotents
from time import perf_counter
from numba import njit


@njit
def m(n: int) -> int:
    # print(n, end="\r")
    for i in range(n - 1, -1, -1):
        if ((i**2) % n) == i:
            return i
    return -1


@njit
def main():
    answer = 0
    for n in range(1, (10**7) + 1):
        if n % 100000 == 0:
            print(100 * n / 10**7, "%")
        answer += m(n)
    print(answer)


if __name__ == "__main__":
    start_time = perf_counter()
    main()
    print(perf_counter() - start_time)
