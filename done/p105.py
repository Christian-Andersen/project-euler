from itertools import combinations
import multiprocessing


def check_set(s: list[int]) -> int:
    for comb_size_b in range(1, len(s) + 1):
        for comb_size_c in range(1, comb_size_b + 1):
            for comb_b in combinations(s, comb_size_b):
                for comb_c in combinations(s, comb_size_c):
                    if not set(comb_b).intersection(set(comb_c)):
                        if sum(comb_b) == sum(comb_c):
                            return 0
                        if len(comb_b) > len(comb_c):
                            if sum(comb_b) <= sum(comb_c):
                                return 0
    return sum(s)


if __name__ == "__main__":
    with open("./0105_sets.txt", "r") as f:
        sets = [[int(i) for i in line.strip().split(",")] for line in f.readlines()]
    with multiprocessing.Pool() as pool:
        results = pool.map(check_set, sets)
    print(sum(results))
