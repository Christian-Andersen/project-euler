from fractions import Fraction
import torch

def check_f(n:int) -> int:
    count = 0
    y = float('inf')
    x = n
    while x < y:
        x += 1
        frac = Fraction(1, n) - Fraction(1, x)
        if frac.numerator == 1:
            y = frac.denominator
            count += 1
    return count

def f(n:int) -> int:
    x = torch.arange(n+1, 2*n + 1, device=torch.device("cuda"))
    return int(((n*x)%(x-n) == 0).sum())

def main():
    best = 0
    n = 5040
    while True:
        out = f(n)
        if out > best:
            best = out
            print(n, best)
        n += 5040

if __name__=="__main__":
    main()
