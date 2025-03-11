# Special Subset Sums: Optimum
import itertools


def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(
        itertools.combinations(s, r) for r in range(len(s) + 1)
    )


def is_good_set(A):
    for B in powerset(A):
        if not B:
            continue
        for C in powerset(set(A) - set(B)):
            if not C:
                continue
            if sum(B) == sum(C):
                return False
            if len(B) > len(C):
                if not (sum(B) > sum(C)):
                    return False
    return True


def solve(n):
    smallest = float("inf")
    for A in itertools.combinations(range(10 * n), n):
        if (A[0] + A[1]) <= A[-1]:
            continue
        if is_good_set(A):
            if sum(A) < smallest:
                smallest = sum(A)
                print(A, smallest)


def main():
    for n in range(7):
        solve(n)


if __name__ == "__main__":
    main()
