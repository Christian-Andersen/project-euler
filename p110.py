from fractions import Fraction
import numpy as np

def check_f(n:int) -> int:
    xs = []
    ys = []
    y = float('inf')
    x = n
    while x < y:
        x += 1
        frac = Fraction(1, n) - Fraction(1, x)
        if frac.numerator == 1:
            y = frac.denominator
            xs.append(x)
            ys.append(y)
    return xs, ys

def f(n:int) -> int:
    x = np.arange(n+1, 2*n + 1)
    return int(((n*x)%(x-n) == 0).sum())

def old_main():
    best = 0
    n = 2162160
    while True:
        out = f(n)
        if out > best:
            best = out
            print(n, best)
        n += 2162160

def main():
    print(check_f(1260))

if __name__=="__main__":
    main()
