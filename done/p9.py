# Special Pythagorean Triplet
def is_pythagorean_triplet(a: int, b: int, c: int) -> bool:
    return (a**2 + b**2) == c**2


def main() -> int | None:
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = 1000 - (a + b)
            if c <= 0:
                break
            if is_pythagorean_triplet(a, b, c):
                return a * b * c
    return None


if __name__ == "__main__":
    print(main())
