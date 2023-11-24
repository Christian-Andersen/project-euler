# Counting Block Combinations II
from functools import cache

M = 50


@cache
def ways(n: int, previous: tuple) -> int:
    global M
    assert len(previous) == M
    assert n >= 0
    if n == 0:
        return 1
    cut = previous[(-M+1):]
    if previous[-1] == True:
        if all(previous[-M:]):
            return ways(n-1, cut+(True,)) + ways(n-1, cut+(False,))
        else:
            return ways(n-1, cut+(True,))
    else:
        if n < M:
            return 1
        else:
            return ways(n-1, cut+(True,)) + ways(n-1, cut+(False,))


for n in range(1000):
    if ways(n, M*(False,)) >= 1_000_000:
        print(n)
        break
