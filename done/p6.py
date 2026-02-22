# Sum Square Difference
def sum_of_the_squares(n):
    return sum(i**2 for i in range(1, n + 1))


def square_of_the_sums(n):
    return sum(i for i in range(1, n + 1)) ** 2


def difference(n):
    return abs(sum_of_the_squares(n) - square_of_the_sums(n))


def main():
    return difference(100)


if __name__ == "__main__":
    print(main())
