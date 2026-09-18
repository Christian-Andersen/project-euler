# Sum Square Difference
def sum_of_the_squares(n: int) -> int:
    return sum(i**2 for i in range(1, n + 1))


def square_of_the_sums(n: int) -> int:
    return sum(i for i in range(1, n + 1)) ** 2


def difference(n: int) -> int:
    return abs(sum_of_the_squares(n) - square_of_the_sums(n))


def main() -> int:
    return difference(100)


if __name__ == "__main__":
    print(main())
