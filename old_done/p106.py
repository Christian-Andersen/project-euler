# Special Subset Sums: Meta-testing
import numpy as np


def get_subsets(n):
    subsets = []
    for i in range(3**n):
        s = str(np.base_repr(i, 3)).zfill(4)
        loc_1 = s.find("1")
        loc_2 = s.find("2")
        if loc_1 == -1:
            continue
        loc_2 = s.find("2")
        if loc_2 == -1:
            continue
        if loc_2 < loc_1:
            continue
        subsets.append(s)
    return subsets


def check_fixed_size(n: int) -> int:
    subsets = get_subsets(n)
    count = 0
    for subset in subsets:
        if subset.count("1") != subset.count("2"):
            continue
        if subset.count("1") == 1:
            continue
        idxs_1 = []
        idxs_2 = []
        for idx, i in enumerate(subset):
            if i == "1":
                idxs_1.append(idx)
            elif i == "2":
                idxs_2.append(idx)
        for i, j in zip(idxs_1, idxs_2):
            if j < i:
                break
        else:
            continue
        count += 1
    return count


assert check_fixed_size(4) == 1
assert check_fixed_size(7) == 70


def main():
    return check_fixed_size(12)


if __name__ == "__main__":
    main()
