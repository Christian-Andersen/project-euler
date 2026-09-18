from itertools import count

import numpy as np


def main() -> int:
    solutions = np.zeros(10**6, dtype=np.uint8)

    for d in range(1, 600):
        for z in range((3 * d - 1), 0, -1):
            y = z + d
            x = y + d
            n = (x * x) - (y * y) - (z * z)
            assert n > 0  # noqa: S101
            if n >= 1_000_000:  # noqa: PLR2004
                continue
            solutions[n] += 1
        print(np.count_nonzero(solutions == 10))  # noqa: PLR2004
    for d in count(600):
        for z in range((3 * d - 1), 0, -1):
            y = z + d
            x = y + d
            n = (x * x) - (y * y) - (z * z)
            assert n > 0  # noqa: S101
            if n >= 1_000_000:  # noqa: PLR2004
                break
            solutions[n] += 1
        print(np.count_nonzero(solutions == 10))  # noqa: PLR2004
    return int(np.count_nonzero(solutions == 10))  # noqa: PLR2004


if __name__ == "__main__":
    main()
