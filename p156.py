# Counting Digits
from functools import lru_cache


@lru_cache(maxsize=1)
def f(n: int, d: int) -> int:
    if n == 0:
        if d == 0:
            return 1
        return 0
    return f(n - 1, d) + str(n).count(str(d))


for i in range(0, 10**15, 10):
    out = f(i, 1)
    if i < out:
        print("LARGER")
    elif i > out:
        print("SMALLER")
    else:
        print("EQUAL")
