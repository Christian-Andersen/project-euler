from tqdm import tqdm


def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


def rad(x):
    if is_prime(x):
        return x
    out = 1
    for i in range(2, int(x/2)+1):
        if x % i == 0:
            if is_prime(i):
                out = out * i
    return out


d = {}
for n in tqdm(range(1, 100_001)):
    d[n] = rad(n)
sorted_d = dict(sorted(d.items(), key=lambda item: item[1]))
print(list(sorted_d.keys())[10_000-1])
