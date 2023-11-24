# Cube Digit Pairs
from itertools import combinations

squares = set(['01', '04', '09', '16', '25', '36', '49', '64', '81'])

digits = [str(i) for i in range(10)]
combs = set()
for i in combinations(digits, 6):
    if len(i) == 6:
        combs.add(i)
new_combs = set()
for comb in combs:
    if '6' in combs:
        if '9' not in comb:
            comb += ('9',)
    if '9' in comb:
        if '6' not in comb:
            comb += ('6',)
    new_combs.add(comb)
combs = list(new_combs)

counter = 0
for i in range(len(combs)):
    for j in range(i):
        comb_1 = combs[i]
        comb_2 = combs[j]
        if comb_1 == comb_2:
            continue
        numbers = set()
        for digit_1 in comb_1:
            for digit_2 in comb_2:
                numbers.add(digit_1+digit_2)
                numbers.add(digit_2+digit_1)
        if not (squares-numbers):
            counter += 1
print(counter)