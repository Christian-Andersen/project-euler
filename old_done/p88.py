from math import prod


def up_factor(factors: set[tuple]) -> set[tuple]:
    # all tuples must be same length
    length = len(next(iter(factors)))
    for factor in factors:
        assert len(factor) == length  # noqa: S101
    new_factors = set()
    for factor in factors:
        for i in range(1, length):
            for j in range(i):
                multiplied = [factor[i] * factor[j]]
                rest = [factor[k] for k in range(length) if (k not in (i, j))]
                new_factors.add(tuple(sorted(multiplied + rest)))
    return new_factors


def factorize(x: int) -> tuple[int, ...]:
    if x == 1:
        return ()
    for i in range(2, x + 1):
        div, mod = divmod(x, i)
        if mod == 0:
            return (i, *factorize(div))
    return ()


def get_smallest_n(k: int) -> int:
    n = k
    while True:
        factors_set = set()
        factors_set.add(factorize(n))
        while True:
            for factors in factors_set:
                lhs = prod(factors)
                rhs = sum(factors) + (k - len(factors))
                if lhs == rhs:
                    return n
            factors_set = up_factor(factors_set)
            if not factors_set:
                break
        n += 1
    return n


def main() -> int:
    n_set = set()
    for k in range(2, 12_000 + 1):
        print(k)
        n_set.add(get_smallest_n(k))
    return sum(n_set)


if __name__ == "__main__":
    main()
