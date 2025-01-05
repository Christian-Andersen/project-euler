import numpy as np


start = 10**12 + 7 * 10**10
step = 10**8


def f(start):
    total_discs = np.arange(start, start + step, dtype=np.uint64)
    blue_discs = np.multiply(total_discs, np.sqrt(1 / 2))
    where = np.isclose(blue_discs, blue_discs.round(), rtol=0).nonzero()[0]
    for total_disc in total_discs[where].tolist():
        blue_disc = int(total_disc * (0.5**0.5)) - 10
        while True:
            p = (blue_disc / total_disc) * ((blue_disc - 1) / (total_disc - 1))
            if p > 0.5:
                break
            if p == 0.5:
                print(total_disc, blue_disc)
            blue_disc += 1


while True:
    print(f"{start:,}")
    f(start)
    start += step
