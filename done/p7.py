# 10001st Prime - Project Euler
from sympy.ntheory.generate import prime


def main():
    return prime(10_001)


if __name__ == "__main__":
    print(main())
