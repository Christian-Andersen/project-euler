# Counting Block Combinations I
from functools import cache


@cache
def ways(n: int, previous: tuple[bool, bool, bool]) -> int:
    assert n >= 0
    if n == 0:
        return 1
    if previous[-1] == True:
        if (previous[-2] == True) and (previous[-3] == True):
            return ways(n-1, previous[-2:]+(True,)) + ways(n-1, previous[-2:]+(False,))
        else:
            return ways(n-1, previous[-2:]+(True,))
    else:
        if n < 3:
            return 1
        else:
            return ways(n-1, previous[-2:]+(True,)) + ways(n-1, previous[-2:]+(False,))


print(ways(50, (False, False, False)))
