def main():
    a = []
    for base in range(2, 1000):
        for power in range(2, 100):
            summed = sum([int(i) for i in str(base**power)])
            if base == summed:
                a.append(base**power)
    a.sort()
    print(a[2 - 1], a[10 - 1], a[30 - 1])
    return a


if __name__ == "__main__":
    main()
