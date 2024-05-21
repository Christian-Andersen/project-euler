from fractions import Fraction
from sympy import factorint


def f(n: int):
    xs = []
    ys = []
    y = float("inf")
    x = n
    while x < y:
        x += 1
        frac = Fraction(1, n) - Fraction(1, x)
        if frac.numerator == 1:
            y = frac.denominator
            xs.append(x)
            ys.append(y)
    return xs, ys


def main():
    print(len(f(2162160)[0]))


if __name__ == "__main__":
    main()
