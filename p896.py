from copy import deepcopy


def is_reducible(l: list[set[int]]) -> bool:
    """Takes in a list of sets, checks if we can remove in such a way all sets get to empty"""
    if not l:
        return True
    smallest = (-1, float("inf"))
    for idx, s in enumerate(l):
        len_s = len(s)
        if len_s == 0:
            return False
        if len_s <= smallest[1]:
            smallest = (idx, len_s)
    if smallest[1] == 1:
        removed = l.pop(smallest[0]).pop()
        for s in l:
            s.discard(removed)
        return is_reducible(l)
    outcomes = []
    for option in l[smallest[0]]:
        new_l = deepcopy(l)
        for s in new_l:
            s.discard(option)
        outcomes.append(is_reducible(new_l))
    return any(outcomes)


def get_divisible_ranges(n: int) -> None:
    count = 0
    end_idx = n
    while True:
        print(end_idx)
        end_idx += 1
        l = [set() for i in range(n)]
        for i in range(end_idx - n, end_idx):
            for j in range(1, n + 1):
                if (i % j) == 0:
                    l[j - 1].add(i)
        if is_reducible(l):
            count += 1
            print(count, end_idx - n)
            input()


def main():
    n = 36
    get_divisible_ranges(n)


if __name__ == "__main__":
    main()
