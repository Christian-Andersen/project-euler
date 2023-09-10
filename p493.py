from itertools import combinations

balls = 10*[0]+10*[1]+10*[2]+10*[3]+10*[4]+10*[5]+10*[6]

total = 0
for idx, sample in enumerate(combinations(balls, 20)):
    total += len(set(sample))
    if idx % 1_000_000 == 0:
        print(total/(idx+1))
