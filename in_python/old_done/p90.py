from itertools import combinations


def main():
    squares = {"01", "04", "09", "16", "25", "36", "49", "64", "81"}

    digits = [str(i) for i in range(10)]

    cubes = []
    for comb in combinations(digits, 6):
        comb = set(comb)
        if "6" in comb:
            comb.add("9")
        elif "9" in comb:
            comb.add("6")
        cubes.append(comb)

    count = 0
    for i in range(len(cubes)):
        for j in range(i):
            cube_1 = cubes[i]
            cube_2 = cubes[j]
            displayed = set()
            for digit_1 in cube_1:
                for digit_2 in cube_2:
                    displayed.add(digit_1 + digit_2)
                    displayed.add(digit_2 + digit_1)
            if len(squares - displayed) == 0:
                count += 1
    print(count)
    return count


if __name__ == "__main__":
    main()
