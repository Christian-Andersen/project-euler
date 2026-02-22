from tqdm import tqdm
import numpy as np

P = [[]]
for _ in range(9):
    new_P = []
    for i in range(1, 5):
        for j in P:
            new_P.append(j + [i])
    P = new_P
C = [[]]
for _ in range(6):
    new_C = []
    for i in range(1, 7):
        for j in C:
            new_C.append(j + [i])
    C = new_C

P = np.array(P, dtype=np.uint8).sum(axis=1)
C = np.array(C, dtype=np.uint8).sum(axis=1)
print(P.shape)
print(C.shape)


def main():
    games_count = 0
    wins_P = 0
    for score_P in tqdm(P):
        games_count += len(C)
        wins_P += (score_P > C).sum()
    return round(wins_P / games_count, 7)


if __name__ == "__main__":
    main()
