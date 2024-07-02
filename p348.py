# Sum of a Square and a Cube
import numpy as np
from tqdm import tqdm

N = 100_000_000

r = np.arange(10000000)
SQUARES = r**2
CUBES = r**3


def get_palindromes() -> dict[int, int]:
    palindromes = set(range(10))
    for i in range(1, 7):
        for j in range(10 ** (i)):
            s = str(j).zfill(i)
            if s.endswith("0"):
                continue
            palindromes.add(int(s[::-1] + s))
            for k in range(10):
                palindromes.add(int(s[::-1] + str(k) + s))
            if 10 in palindromes:
                print(i, j, s)
                exit()
    return {i: 0 for i in palindromes if i < N}


def main():
    palindromes = get_palindromes()
    print("Got Palindromes")
    for i in tqdm(SQUARES):
        for j in CUBES:
            x = i + j
            if x >= N:
                break
            if x in palindromes:
                palindromes[x] += 1
    if l := [key for key, value in palindromes.items() if value == 4]:
        print(l)


if __name__ == "__main__":
    main()
