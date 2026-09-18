def find_ways(n: int, length: int) -> list[list[bool]]:
    ways = [[]]
    for idx in range(n):
        print(idx, len([way for way in ways if len(way) == idx]))
        new_ways = []
        for way in ways:
            if idx < len(way):
                new_ways.append(way)
            else:
                new_ways.append([*way, False])
                new_ways.append([*way, *length * [True]])
        ways = new_ways
    return [way for way in ways if len(way) == n]


def main() -> int:
    return len(find_ways(50, 2)) - 1


if __name__ == "__main__":
    main()
