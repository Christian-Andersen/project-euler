# Counting Block Combinations II
from functools import cache

M = 50


@cache
def ways(n: int, previous: tuple) -> int:
    assert len(previous) == M  # noqa: S101
    assert n >= 0  # noqa: S101
    if n == 0:
        return 1
    cut = previous[(-M + 1) :]
    if previous[-1]:
        if all(previous[-M:]):
            return ways(n - 1, (*cut, True)) + ways(n - 1, (*cut, False))
        return ways(n - 1, (*cut, True))
    if n < M:
        return 1
    return ways(n - 1, (*cut, True)) + ways(n - 1, (*cut, False))


def main() -> int | None:
    for n in range(1000):
        if ways(n, M * (False,)) >= 1_000_000:  # noqa: PLR2004
            return n
    return None


if __name__ == "__main__":
    main()
