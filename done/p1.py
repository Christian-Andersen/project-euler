# Multiples of 3 or 5
def main():
    return sum(i for i in range(1000) if ((i % 3) == 0) or ((i % 5) == 0))


if __name__ == "__main__":
    print(main())
