# Smallest Multiple
from math import lcm


def main() -> int:
    return lcm(*range(1, 20 + 1))


if __name__ == "__main__":
    print(main())
