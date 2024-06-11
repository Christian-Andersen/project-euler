# Strong Repunits
from sympy import primefactors
from tqdm import trange


def to_int(length: int, base: int) -> int:
    """Given a number length*'1' in given base, convert to base 10"""
    ans = 0
    for i in range(length):
        ans += base**i
    return ans


def get_all_for_base(base: int, n: int) -> list[int]:
    out = []
    length = 0
    number = 0
    while True:
        number += base**length
        if number >= n:
            return out
        out.append(number)
        length += 1


def f(n: int) -> int:
    numbers = set()
    answers = {1}
    for base in range(2, n):
        out = get_all_for_base(base, n)
        previous_count = sum(answers)
        answers.update(numbers.intersection(out))
        new_count = sum(answers)
        numbers.update(out)
        if new_count != previous_count:
            print(base, new_count)
            print(primefactors(base))
            print()
    return sum(answers)


def main():
    assert f(1000) == 15864
    print(f(10**12))


if __name__ == "__main__":
    main()
