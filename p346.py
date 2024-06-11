# Strong Repunits


def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def main():
    return


if __name__ == "__main__":
    main()
