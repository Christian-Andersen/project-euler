# Optimum Polynomial
import numpy as np


def f(n):
    return 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10


uns = [f(i) for i in range(1, 21)]

answer = 0
for i in range(10):
    x = list(range(1, i + 2))
    y = uns[: (i + 1)]
    assert len(x) == len(y)
    poly = np.polyfit(x, y, i).round().astype(int)
    pred = [np.polyval(poly, j) for j in range(1, len(x) + 1)]
    assert pred == y
    answer += np.polyval(poly, len(x) + 1)
print(answer)
