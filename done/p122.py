# Efficient Exponentiation


def extend(ways):
    new_ways = set()
    for way in ways:
        for i in range(len(way)):
            for j in range(i + 1):
                new_power = way[i] + way[j]
                if new_power in way:
                    continue
                new_ways.add(tuple(sorted(way + (new_power,))))
    return new_ways


def main():
    answers = 1_000_000 * [float("inf")]
    ways = [(1,)]
    for way in ways:
        answers[1] = 0
    for m in range(1, 30):
        ways = extend(ways)
        for way in ways:
            answers[max(way)] = min(answers[max(way)], m)
        if sum(answers[1:201]) != float("inf"):
            break
    return sum(answers[1:201])


if __name__ == "__main__":
    main()
