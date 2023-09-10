from itertools import count


def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if (x % i) == 0:
            return False
    return True


n = 2
for p in count(3, 2):
    if not is_prime(p):
        continue
    n += 1
    r = ((p-1)**n + (p+1)**n) % (p**2)
    if r >= (10**10):
        print(n, p, r)
        break
