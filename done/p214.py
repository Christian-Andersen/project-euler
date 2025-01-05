from functools import cache
from sympy import sieve

totients = [0] + [i for i in sieve.totientrange(1, 40_000_000)]
print("Made Totients List")


@cache
def get_chain_length(n):
    if n == 1:
        return 1
    return 1 + get_chain_length(totients[n])


total = 0
for p in sieve.primerange(40_000_000):
    chain_length = get_chain_length(p)
    if get_chain_length(p) == 25:
        print("FOUND", p)
        total += p
print(total)
