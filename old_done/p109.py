def main():
    scores = {}
    scores["0"] = 0
    for i in range(1, 21):
        scores[str(i)] = i
        scores["D" + str(i)] = 2 * i
        scores["T" + str(i)] = 3 * i
    scores["25"] = 25
    scores["D25"] = 2 * 25

    ways = set()
    for i in scores:
        for j in scores:
            for k in scores:
                if k.startswith("D"):
                    ways.add((tuple(sorted((i, j))), k))
    counter = 0
    for way in ways:
        score = scores[way[0][0]] + scores[way[0][1]] + scores[way[1]]
        if score < 100:
            counter += 1
    return counter


if __name__ == "__main__":
    main()
