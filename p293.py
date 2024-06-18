# Pseudo-Fortunate Numbers
from sympy import primefactors, sieve, nextprime
from tqdm import trange


def is_admissible(x: int) -> bool:
    for i, j in zip(primefactors(x), sieve):
        if i != j:
            return False
    return True


def main():
    pseudo_fortunate_numbers = set()
    for i in trange(2, 10**9):
        if is_admissible(i):
            pseudo_fortunate_numbers.add(nextprime(i + 1) - i)  # type: ignore


if __name__ == "__main__":
    main()
