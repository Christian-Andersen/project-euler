# Prize Strings
OPTIONS = "LOA"


def is_prize_winner(attendances: str, late_count: int) -> bool:
    if attendances == "AAA":
        return False
    if late_count > 1:
        return False
    return True


def extend(d):
    new_d = {}
    for (attendances, late_count), value in d.items():
        for j in OPTIONS:
            new_attendances = j + attendances[:2]
            if j == "L":
                new_late_count = late_count + 1
            else:
                new_late_count = late_count
            key = (new_attendances, new_late_count)
            if is_prize_winner(new_attendances, new_late_count):
                if key in new_d:
                    new_d[key] += value
                else:
                    new_d[key] = value
    return new_d


def main():
    ways = {("L", 1): 1, ("O", 0): 1, ("A", 0): 1}
    for _ in range(2, 31):
        ways = extend(ways)
    return sum(ways.values())


if __name__ == "__main__":
    main()
