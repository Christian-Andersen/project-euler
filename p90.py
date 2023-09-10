from copy import deepcopy


def can_write(s1: set, s2: set) -> bool:
    if 6 in s1:
        s1.add(9)
    if 9 in s1:
        s1.add(6)
    if 6 in s2:
        s2.add(9)
    if 9 in s2:
        s2.add(6)
    if not all([i in s1.union(s2) for i in [0, 1, 2, 3, 4, 5, 6, 8]]):
        return False
    boo = False
    if 0 in s1:
        if 4 in s2:
            boo = True
    if 0 in s2:
        if 4 in s1:
            boo = True
    if not boo:
        return False
    boo = False
    if 0 in s1:
        if 9 in s2:
            boo = True
    if 0 in s2:
        if 9 in s1:
            boo = True
    if not boo:
        return False
    boo = False
    if 1 in s1:
        if 6 in s2:
            boo = True
    if 1 in s2:
        if 6 in s1:
            boo = True
    if not boo:
        return False
    boo = False
    if 2 in s1:
        if 5 in s2:
            boo = True
    if 2 in s2:
        if 5 in s1:
            boo = True
    if not boo:
        return False
    boo = False
    if 3 in s1:
        if 6 in s2:
            boo = True
    if 3 in s2:
        if 6 in s1:
            boo = True
    if not boo:
        return False
    boo = False
    if 4 in s1:
        if 9 in s2:
            boo = True
    if 4 in s2:
        if 9 in s1:
            boo = True
    if not boo:
        return False
    boo = False
    if 6 in s1:
        if 4 in s2:
            boo = True
    if 6 in s2:
        if 4 in s1:
            boo = True
    if not boo:
        return False
    boo = False
    if 8 in s1:
        if 1 in s2:
            boo = True
    if 8 in s2:
        if 1 in s1:
            boo = True
    if not boo:
        return False
    return True


sets = set()
for a in range(10):
    for b in range(a):
        for c in range(b):
            for d in range(c):
                for e in range(d):
                    for f in range(e):
                        sets.add((a, b, c, d, e, f))


sets = [set(i) for i in sets]
sets_copy = deepcopy(sets)
ways = []
for idx1 in range(len(sets)):
    for idx2 in range(len(sets)):
        if can_write(sets[idx1], sets[idx2]):
            ways.append(
                tuple(sorted([tuple(sets_copy[idx1]), tuple(sets_copy[idx2])])))
out = sorted(set(ways))
for i in out:
    print(i)
print(len(out))
