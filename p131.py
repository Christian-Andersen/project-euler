from numba import njit
import torch

device = torch.device('cuda')


@njit
def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if (x % i) == 0:
            return False
    return True


primes = [i for i in range(10**6) if is_prime(i)]
primes = torch.tensor(primes).to(device=device)
cubes = torch.pow(torch.arange(1, 10**6), 3).to(device=device)
n = torch.arange(1000).unsqueeze(-1).to(device=device)
n += 1
counter = 0
for i in range(10**6):
    lhs = n.pow(3).add(n.pow(2).mul(primes))
    for line in lhs:
        counter += torch.isin(line, cubes, assume_unique=True).sum()
    n += 1000
    if (i % 1) == 0:
        print(i, counter.item())
