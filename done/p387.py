def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if (x % i) == 0:
            return False
    return True


digits = [str(digit) for digit in range(0, 10)]
harshad_numbers = list(str(i) for i in range(1, 10))
all_harshad_numbers = []
for x in harshad_numbers:
    d, r = divmod(int(x), sum(int(digit) for digit in x))
    if r == 0:
        if is_prime(d):
            all_harshad_numbers.append(x)
for number_of_digits in range(2, 14):
    new_harshad_numbers = []
    for i in harshad_numbers:
        for j in digits:
            x = i + j
            if 0 == (int(x) % sum(int(digit) for digit in x)):
                new_harshad_numbers.append(x)
    harshad_numbers = new_harshad_numbers
    for x in harshad_numbers:
        d, r = divmod(int(x), sum(int(digit) for digit in x))
        if r == 0:
            if is_prime(d):
                all_harshad_numbers.append(x)
summed = 0
for i in all_harshad_numbers:
    for j in digits:
        x = int(i + j)
        if x < 10**14:
            if is_prime(x):
                summed += x
print(summed)
