# Tribonacci Non-divisors


def main():
    factors = set(range(1, 100, 2))
    l = [1, 1, 1]
    for _ in range(1000):
        l.append(l[-3] + l[-2] + l[-1])
    for i in l:
        factors = [j for j in factors if (i % j != 0)]
    print(factors)


if __name__ == "__main__":
    main()
