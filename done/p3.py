# Largest Prime Factor
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if (x % i) == 0:
            return False
    return True


def get_lowest_factor(x):
    p = 2
    while True:
        if is_prime(p):
            if (x % p) == 0:
                return p
        p += 1


def main():
    n = 600851475143
    prime_factors = []
    while n != 1:
        p = get_lowest_factor(n)
        prime_factors.append(p)
        n = n // p
    return max(prime_factors)


if __name__ == "__main__":
    print(main())
