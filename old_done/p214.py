from functools import cache

from sympy import sieve

totients = [0, *list(sieve.totientrange(1, 40_000_000))]
print("Made Totients List")


@cache
def get_chain_length(n: int) -> int:
    if n == 1:
        return 1
    return 1 + get_chain_length(totients[n])


def main() -> int:
    total = 0
    for p in sieve.primerange(40_000_000):
        if get_chain_length(p) == 25:  # noqa: PLR2004
            print("FOUND", p)
            total += p
    return total


if __name__ == "__main__":
    main()
