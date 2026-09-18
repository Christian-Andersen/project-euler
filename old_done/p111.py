from itertools import combinations, product


def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    return all(x % i != 0 for i in range(2, int(x**0.5) + 1))


def list_to_number(number_list: list) -> int:
    return int("".join([str(i) for i in number_list]))


def S(n: int, d: int) -> int | None:  # noqa: N802
    allowed_number = list(range(10))
    allowed_number.remove(d)
    if is_prime(int(n * str(d))):
        raise  # noqa: PLE0704
    for number_repeated in range(n - 1, 0, -1):
        prime_sum = 0
        for i in combinations(range(n), number_repeated):
            for j in product(allowed_number, repeat=(n - number_repeated)):
                j_list = list(j)
                for k in i:
                    j_list.insert(k, d)
                if j_list[0] == 0:
                    continue
                number = list_to_number(j_list)
                if is_prime(number):
                    prime_sum += number
        if prime_sum != 0:
            return prime_sum
    return None


def main() -> int:
    total = 0
    for i in range(10):
        total += S(10, i)  # ty: ignore[unsupported-operator]
    return total


if __name__ == "__main__":
    main()
