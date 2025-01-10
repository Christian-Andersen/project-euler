def find_ways(N, L):
    ways = [[]]
    for idx in range(N):
        print(idx, len([way for way in ways if len(way) == idx]))
        new_ways = []
        for way in ways:
            if idx < len(way):
                new_ways.append(way)
            else:
                new_ways.append(way + [False])
                new_ways.append(way + L * [True])
        ways = new_ways
    ways = [way for way in ways if len(way) == N]
    return ways


def main():
    return len(find_ways(50, 2)) - 1


if __name__ == "__main__":
    main()
