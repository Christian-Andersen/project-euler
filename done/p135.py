import numpy as np
from itertools import count

solutions = np.zeros(10**6, dtype=np.uint8)


for d in range(1, 600):
    for z in range((3*d - 1), 0, -1):
        y = z+d
        x = y+d
        n = (x*x)-(y*y)-(z*z)
        assert (n > 0)
        if n >= 1_000_000:
            continue
        solutions[n] += 1
    print(np.count_nonzero(solutions == 10))
for d in count(600):
    for z in range((3*d - 1), 0, -1):
        y = z+d
        x = y+d
        n = (x*x)-(y*y)-(z*z)
        assert (n > 0)
        if n >= 1_000_000:
            break
        solutions[n] += 1
    print(np.count_nonzero(solutions == 10))
