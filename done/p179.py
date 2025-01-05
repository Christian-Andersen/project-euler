from tqdm import trange
import numpy as np

N = 10**7

divisor_count = np.zeros(N + 1, dtype=np.uint32)

for i in trange(1, N):
    idxs = i * np.arange(1, int(N / i) + 1)
    divisor_count[idxs] += 1
count = 0
for i in range(N):
    if divisor_count[i] == divisor_count[i + 1]:
        count += 1
print(count)
