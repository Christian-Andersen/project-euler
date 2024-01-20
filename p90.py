# Cube Digit Pairs
from itertools import combinations

# All squares under 100 ('00' not included)
squares = set(['01', '04', '09', '16', '25', '36', '49', '64', '81'])

# Get all the possible cubes you can make
digits = [str(i) for i in range(10)]
combs = set()
for i in combinations(digits, 6):
    if len(i) == 6:
        combs.add(i)
# Add the letters 9 or 6 as required
new_combs = set()
for comb in combs:
    if '6' in combs:
        comb += ('9',)
    if '9' in comb:
        comb += ('6',)
    new_combs.add(comb)
combs = list(new_combs)

counter = 0
# iterate over all combinations
for i, j in combinations(range(len(combs)), 2):
    comb_1 = combs[i]
    comb_2 = combs[j]
    numbers = set()
    for digit_1 in comb_1:
        for digit_2 in comb_2:
            numbers.add(digit_1+digit_2)
            numbers.add(digit_2+digit_1)
    if not (squares-numbers):
        counter += 1
print(counter)
