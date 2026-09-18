# Sum of a Square and a Cube
import sys

from tqdm import tqdm

N = 10**9


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
            if 10 in palindromes:  # noqa: PLR2004
                print(i, j, s)
                sys.exit()
    return {i: 0 for i in palindromes if i < N}


def main() -> int | None:
    palindromes = get_palindromes()
    print("Got Palindromes")
    squares = [i**2 for i in range(int(N ** (1 / 2)))]
    cubes = [i**3 for i in range(int(N ** (1 / 3)))]
    for i in tqdm(squares):
        for j in cubes:
            x = i + j
            if x >= N:
                break
            if x in palindromes:
                palindromes[x] += 1
    if matches := [key for key, value in palindromes.items() if value == 4]:  # noqa: PLR2004
        print(sum(matches))
        return sum(matches)
    return None


if __name__ == "__main__":
    main()
