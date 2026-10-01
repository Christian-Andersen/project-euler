# Even Fibonacci Numbers
def main() -> int:
    answer = 0
    a, b = 1, 2
    while a <= 4_000_000:  # noqa: PLR2004
        if (a % 2) == 0:
            answer += a
        a, b = b, a + b
    return answer


if __name__ == "__main__":
    print(main())
