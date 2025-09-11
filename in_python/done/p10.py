# Summation of Primes
from sympy.ntheory.generate import primerange


def main():
    return sum(primerange(2_000_000))


if __name__ == "__main__":
    print(main())
