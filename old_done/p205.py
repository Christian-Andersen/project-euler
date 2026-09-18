import numpy as np
from tqdm import tqdm

P = [[]]
for _ in range(9):
    P = [[*j, i] for i in range(1, 5) for j in P]
C = [[]]
for _ in range(6):
    C = [[*j, i] for i in range(1, 7) for j in C]

P = np.array(P, dtype=np.uint8).sum(axis=1)
C = np.array(C, dtype=np.uint8).sum(axis=1)
print(P.shape)
print(C.shape)


def main() -> float:
    games_count = 0
    wins_p = 0
    for score_p in tqdm(P):
        games_count += len(C)
        wins_p += (score_p > C).sum()
    return round(wins_p / games_count, 7)


if __name__ == "__main__":
    main()
