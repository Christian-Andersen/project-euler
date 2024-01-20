# Arithmetic Expressions
from itertools import permutations, product
import numpy as np

OPERATIONS = [np.add, np.subtract, np.multiply, np.divide]


def get_sols(a, b, c, d):
    targets = []
    for number_perm in permutations((a, b, c, d), 4):
        for operation_perm in product(OPERATIONS, repeat=3):
            target = number_perm[3]
            for i in range(3):
                target = operation_perm[i](target, number_perm[i])
            targets.append(target)
    for target in targets.copy():
        targets.append(-target)
    return set(float(i) for i in targets)


def main():
    start_value = 1
    best_largest = 0
    for d in range(1, 1_000):
        print(d)
        for c in range(start_value, d):
            for b in range(start_value, c):
                for a in range(start_value, b):
                    out = get_sols(a, b, c, d)
                    largest = 0
                    for i in range(1, 1_000_000):
                        if float(i) in out:
                            largest = i
                        else:
                            break
                    if largest > best_largest:
                        best_largest = largest
                        print(a, b, c, d, largest)


if __name__ == "__main__":
    main()
