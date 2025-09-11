def expand_increasing(d: dict[int, int]) -> dict[int, int]:
    out = {k: 0 for k in range(1, 10)}
    for key, value in d.items():
        for i in range(1, key + 1):
            out[i] += value
    return out


def expand_decreasing(d: dict[int, int]) -> dict[int, int]:
    out = {k: 1 for k in range(1, 10)}
    for key, value in d.items():
        for i in range(key, 10):
            out[i] += value
    return out


def main():
    x = {k: 1 for k in range(1, 10)}
    y = {k: 1 for k in range(1, 10)}
    answer = 9
    for _ in range(2, 101):
        x = expand_increasing(x)
        y = expand_decreasing(y)
        answer += sum(x.values()) + sum(y.values()) - 9
    return answer


if __name__ == "__main__":
    main()
