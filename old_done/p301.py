import numpy as np

N = 2**30


def main() -> np.ndarray:
    n = np.arange((N) + 1, dtype=np.uint32)
    return np.bitwise_xor(np.bitwise_xor(n, 2 * n, dtype=np.uint32), 3 * n, dtype=np.uint32)


if __name__ == "__main__":
    main()
