total_discs = 10**12
blue_discs = int(total_discs * (0.5**0.5))
LHS = 2 * (blue_discs**2 - blue_discs)
RHS = total_discs**2 - total_discs

while True:
    # p1 = blue_discs/total_discs
    # p2 = (blue_discs-1)/(total_discs-1)
    # print(p1*p2)
    if LHS == RHS:
        print(blue_discs, total_discs)
        break
    elif LHS < RHS:
        LHS += 4 * blue_discs
        blue_discs += 1
    else:
        RHS += 2 * total_discs
        total_discs += 1
        blue_discs -= 1
        LHS -= 4 * blue_discs
