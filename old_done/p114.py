# Counting Block Combinations I
from functools import cache


@cache
def ways(n: int, previous: tuple[bool, bool, bool]) -> int:
    assert n >= 0  # noqa: S101
    if n == 0:
        return 1
    if previous[-1]:
        if previous[-2] and previous[-3]:
            return ways(n - 1, (*previous[-2:], True)) + ways(n - 1, (*previous[-2:], False))
        return ways(n - 1, (*previous[-2:], True))
    if n < 3:  # noqa: PLR2004
        return 1
    return ways(n - 1, (*previous[-2:], True)) + ways(n - 1, (*previous[-2:], False))


def main() -> int:
    return ways(50, (False, False, False))


if __name__ == "__main__":
    main()
