def main() -> int:
    total_discs = 10**12
    blue_discs = int(total_discs * (0.5**0.5))
    lhs = 2 * (blue_discs**2 - blue_discs)
    rhs = total_discs**2 - total_discs
    while True:
        # p1 = blue_discs/total_discs
        # p2 = (blue_discs-1)/(total_discs-1)
        # print(p1*p2)
        if lhs == rhs:
            print(blue_discs, total_discs)
            break
        if lhs < rhs:
            lhs += 4 * blue_discs
            blue_discs += 1
        else:
            rhs += 2 * total_discs
            total_discs += 1
            blue_discs -= 1
            lhs -= 4 * blue_discs
    return blue_discs


if __name__ == "__main__":
    main()
