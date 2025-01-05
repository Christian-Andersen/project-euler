from math import gcd
from itertools import count
import sys

sys.set_int_max_str_digits(0)


def A(n: int) -> int:
    x = 0
    for k in range(1, 1_000_000):
        x = (10 * x) + 1
        if (x % n) == 0:
            return k
    print("Solution:", n)
    exit()


for n in count(1_000_000):
    if gcd(n, 10) == 1:
        print(n, A(n))
