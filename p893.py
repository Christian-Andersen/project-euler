# Matchsticks
from itertools import product

from tqdm import tqdm

operations = [
    ("1", 2),
    ("2", 5),
    ("3", 5),
    ("4", 4),
    ("5", 5),
    ("6", 6),
    ("7", 3),
    ("8", 7),
    ("9", 6),
    ("0", 6),
    ("+", 2),
    ("*", 2),
]

N = 10**6
depth = 0
l = [0] + (N * [float("inf")])


def solve(expression: str) -> int | None:
    try:
        return eval(expression)
    except SyntaxError:
        return None
    except Exception as e:
        raise e


def fill_d():
    global depth
    depth += 1
    for i in tqdm(product(operations, repeat=depth), total=len(operations) ** depth):
        expression, sticks = zip(*i)
        if expression[-1] in ["+", "*"]:
            continue
        expression = "".join(expression)
        if "**" in expression:
            continue
        n = solve(expression)
        if n is None:
            continue
        if n > N:
            continue
        l[n] = min(l[n], sum(sticks))


def main():
    for _ in range(100):
        fill_d()
        print(sum(l))


if __name__ == "__main__":
    main()
