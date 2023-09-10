from itertools import product
from math import log2


def f(n):
    counter = 0
    powers = [2**i for i in range(1, 1+int(log2(n)))]
    for multiples in product([0, 1, 2], repeat=len(powers)):
        x = sum([power*multiple for power, multiple in zip(powers, multiples)])
        if x > n:
            print('bigger')
        if (x <= n) and (x >= n-2):
            raise
            counter += 1
        else:
            print('too small')
    return counter


print(f(10**25))
