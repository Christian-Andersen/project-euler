# Pseudo Square Root
from sympy import isprime


def check_sqrt(x: int, sqrt_x: int) -> bool:
    if (sqrt_x**2) <= x:
        if ((sqrt_x + 1) ** 2) > x:
            return True
    return False


def get_sqrt_floor(x: int) -> int:
    print(x)
    """returns the floor of the square root"""
    sqrt_x = int(x**0.5)
    while not check_sqrt(x, sqrt_x):
        sqrt_x += x // sqrt_x
        print(sqrt_x)
    return sqrt_x
    while True:
        sqrt_x -= 100000000000000
        print(x - (sqrt_x**2))


def psr(x: int) -> int:
    """returns the largest int that does not exceed the square root"""
    y = get_sqrt_floor(x)
    while True:
        if (x % y) == 0:
            return y
        y -= 1


def main():
    for j in range(100000):
        i = 10**j
        sqrt_i = get_sqrt_floor(i)
        if not check_sqrt(i, sqrt_i):
            print(i, sqrt_i)
            exit()
    assert psr(12) == 3
    assert psr(3102) == 47
    prod = 1
    for i in range(1, 190):
        if isprime(i):
            prod *= i
    print(psr(prod))


if __name__ == "__main__":
    main()
