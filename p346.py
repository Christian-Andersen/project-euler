# Strong Repunits


def number_to_base(n: int, b: int) -> list[int]:
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def is_strong_repunit(n: int) -> bool:
    if n == 1:
        return True
    count = 0
    for b in range(2, n):
        l = number_to_base(n, b)
        if (l[0] == 1) and (len(set(l)) == 1):
            count += 1
            if count == 2:
                return True
    return False


def main():
    for i in range(1, 50):
        if is_strong_repunit(i):
            print(i)


if __name__ == "__main__":
    main()
