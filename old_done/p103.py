# Special Subset Sums: Optimum
import itertools
from collections.abc import Iterable


def powerset(iterable: Iterable) -> itertools.chain:
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))


def is_good_set(A: tuple[int, ...]) -> bool:  # noqa: N803
    for B in powerset(A):  # noqa: N806
        if not B:
            continue
        for C in powerset(set(A) - set(B)):  # noqa: N806
            if not C:
                continue
            if sum(B) == sum(C):
                return False
            if len(B) > len(C) and not (sum(B) > sum(C)):
                return False
    return True


def solve(n: int) -> None:
    smallest = float("inf")
    for A in itertools.combinations(range(10 * n), n):  # noqa: N806
        if (A[0] + A[1]) <= A[-1]:
            continue
        if is_good_set(A) and sum(A) < smallest:
            smallest = sum(A)
            print(A, smallest)


def main() -> None:
    for n in range(7):
        solve(n)


if __name__ == "__main__":
    main()
