def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    return all(x % i != 0 for i in range(2, int(x**0.5) + 1))


def get_next_row(row_in: list) -> list:
    row_out = [1]
    row_out.extend([row_in[i] + row_in[i + 1] for i in range(len(row_in) - 1)])
    row_out.append(1)
    return row_out


def main() -> int:
    rows = [[1]]
    while len(rows) < 51:  # noqa: PLR2004
        rows.append(get_next_row(rows[-1]))

    numbers = set()
    for row in rows:
        for number in row:
            numbers.add(number)

    square_primes = [i**2 for i in range(10**3) if is_prime(i)]

    for number in numbers.copy():
        for i in square_primes:
            if i > number:
                break
            if (number % i) == 0:
                numbers.discard(number)
    return sum(numbers)


if __name__ == "__main__":
    main()
