from itertools import count


def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    return all(x % i != 0 for i in range(2, int(x**0.5) + 1))


def main() -> int | None:
    n = 2
    for p in count(3, 2):
        if not is_prime(p):
            continue
        n += 1
        r = ((p - 1) ** n + (p + 1) ** n) % (p**2)
        if r >= (10**10):
            print(n, p, r)
            return n
    return None


if __name__ == "__main__":
    main()
