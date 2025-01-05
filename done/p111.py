from itertools import combinations, product


def is_prime(x: int):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if (x % i) == 0:
            return False
    return True


def list_to_number(number_list: list):
    return int("".join([str(i) for i in number_list]))


def S(n, d):
    allowed_number = list(range(10))
    allowed_number.remove(d)
    if is_prime(int(n * str(d))):
        raise
    for number_repeated in range(n - 1, 0, -1):
        prime_sum = 0
        for i in combinations(range(n), number_repeated):
            for j in product(allowed_number, repeat=(n - number_repeated)):
                j = list(j)
                for k in i:
                    j.insert(k, d)
                if j[0] == 0:
                    continue
                number = list_to_number(j)
                if is_prime(number):
                    prime_sum += number
        if prime_sum != 0:
            return prime_sum


total = 0
for i in range(10):
    total += S(10, i)
print(total)
