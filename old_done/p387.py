def is_prime(x: int) -> bool:
    if x <= 1:
        return False
    return all(x % i != 0 for i in range(2, int(x**0.5) + 1))


digits = [str(digit) for digit in range(10)]
harshad_numbers = [str(i) for i in range(1, 10)]
all_harshad_numbers = []
for x in harshad_numbers:
    d, r = divmod(int(x), sum(int(digit) for digit in x))
    if r == 0 and is_prime(d):
        all_harshad_numbers.append(x)
for _number_of_digits in range(2, 14):
    new_harshad_numbers = []
    for i in harshad_numbers:
        for j in digits:
            x = i + j
            if (int(x) % sum(int(digit) for digit in x)) == 0:
                new_harshad_numbers.append(x)
    harshad_numbers = new_harshad_numbers
    for x in harshad_numbers:
        d, r = divmod(int(x), sum(int(digit) for digit in x))
        if r == 0 and is_prime(d):
            all_harshad_numbers.append(x)
summed = 0
for i in all_harshad_numbers:
    for j in digits:
        x = int(i + j)
        if x < 10**14 and is_prime(x):
            summed += x
print(summed)
