# Three Consecutive Digital Sum Limit
from itertools import product


def base_case() -> dict[tuple[int, int, int], int]:
    d = {}
    for i in range(1, 10):
        for j in range(10):
            for k in range(10):
                if (i + j + k) <= 9:
                    d[(i, j, k)] = 1
    return d


def f(d: dict[tuple[int, int, int], int]) -> dict[tuple[int, int, int], int]:
    new_d = {}
    if not d:
        return base_case()
    for i in range(10):
        for j in range(10):
            old_sum = 0
            for key, value in d.items():
                if (key[1] == i) and (key[2] == j):
                    old_sum += value
            for k in range(10):
                if (i + j + k) <= 9:
                    new_d[(i, j, k)] = old_sum
    return new_d


def check_number(t: tuple[int, ...]) -> bool:
    for i in range(len(t) - 2):
        if sum(t[i : i + 3]) > 9:
            return False
    return True


def g(n: int):
    count = 0
    for t in product(range(10), repeat=n):
        if check_number(t):
            count += 1
    return count


def main():
    d = {}
    for i in range(3, 21):
        d = f(d)
        print(i, sum(d.values()))
    return sum(d.values())


if __name__ == "__main__":
    main()
