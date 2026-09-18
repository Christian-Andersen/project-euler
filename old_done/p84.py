from random import randint, shuffle

from tqdm import trange


def main() -> float | None:  # noqa: C901, PLR0912
    cc = ["GO", "JAIL"] + 14 * [None]
    ch = [
        "GO",
        "JAIL",
        "C1",
        "E3",
        "H2",
        "R1",
        "nextR",
        "nextR",
        "nextU",
        "back3",
    ] + 6 * [None]
    shuffle(cc)
    shuffle(ch)
    squares = [
        "GO",
        "A1",
        "CC1",
        "A2",
        "T1",
        "R1",
        "B1",
        "CH1",
        "B2",
        "B3",
        "JAIL",
        "C1",
        "U1",
        "C2",
        "C3",
        "R2",
        "D1",
        "CC2",
        "D2",
        "D3",
        "FP",
        "E1",
        "CH2",
        "E2",
        "E3",
        "R3",
        "F1",
        "F2",
        "U2",
        "F3",
        "G2J",
        "G1",
        "G2",
        "CC3",
        "G3",
        "R4",
        "CH3",
        "H1",
        "T2",
        "H2",
    ]
    counter = len(squares) * [0]
    player_loc = 0
    for _move in trange(10**7):
        player_loc += randint(1, 4) + randint(1, 4)  # noqa: S311
        player_loc %= len(squares)
        if squares[player_loc] == "G2J":
            player_loc = squares.index("JAIL")
        elif squares[player_loc].startswith("CC"):
            card = cc.pop(0)
            cc.append(card)
            if card is not None:
                player_loc = squares.index(card)
        elif squares[player_loc].startswith("CH"):
            card = ch.pop(0)
            ch.append(card)
            if card is not None:
                if card == "back3":
                    player_loc += -3
                elif card == "nextU":
                    possible_loc = player_loc
                    while True:
                        possible_loc += 1
                        possible_loc %= len(squares)
                        if squares[possible_loc].startswith("U"):
                            player_loc = possible_loc
                            break
                elif card == "nextR":
                    possible_loc = player_loc
                    while True:
                        possible_loc += 1
                        possible_loc %= len(squares)
                        if squares[possible_loc].startswith("R"):
                            player_loc = possible_loc
                            break
                else:
                    player_loc = squares.index(card)
        counter[player_loc] += 1

    third_largest = sorted(counter)[-3]
    for a, b in zip(squares, counter, strict=False):
        if b >= third_largest:
            print(a, squares.index(a), "\t", 100 * b / sum(counter))
            return 100 * b / sum(counter)
    return None


if __name__ == "__main__":
    main()
