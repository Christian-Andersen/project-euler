from fractions import Fraction
from itertools import product
from math import prod
import torch

D = 1_000_000_000
device = torch.device('cuda')
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

ds = []
for length in [9]:
    iters = product(list(range(1, 6)), repeat=length)
    sub_primes = primes[:(length+1)]
    for i in iters:
        d = prod([a**b for a, b in zip(sub_primes, i)])
        if d < D:
            ds.append(d)
ds.sort()


smallest = Fraction(15499, 94744)
nums = torch.arange(0, D, dtype=torch.int32).to(device=device)
for d in ds:
    d = torch.tensor(d).to(device=device)
    count = nums[1:d].gcd(d).eq(1).sum()
    count, d = count.item(), d.item()
    if Fraction(count, d-1) < smallest:
        print('d:', d, '\t', (count/(d-1)))
