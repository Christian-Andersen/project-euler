import numpy as np

N = 2**30


n = np.arange((N)+1, dtype=np.uint32)
print('here1')
print(np.bitwise_xor(np.bitwise_xor(n, 2*n, dtype=np.uint32), 3*n, dtype=np.uint32))
