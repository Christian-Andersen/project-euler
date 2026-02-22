def main():
    square = 0
    square_change = -1
    l_squared = 29
    change_1 = 3
    change_2 = 16
    while True:
        change_1 += 2
        l_squared += change_1
        while True:
            if square > l_squared:
                out = False
                break
            if square == l_squared:
                out = True
                break
            square_change += 2
            square += square_change
        if out:
            print(round(l_squared**0.5))
        change_2 += 8
        l_squared += change_2
        while True:
            if square > l_squared:
                out = False
                break
            if square == l_squared:
                out = True
                break
            square_change += 2
            square += square_change
        if out:
            return round(l_squared**0.5)


if __name__ == "__main__":
    main()
