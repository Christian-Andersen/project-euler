from itertools import permutations, product


def f(number1, number2, operation):
    match operation:
        case 0:
            return number1+number2
        case 1:
            return number1-number2
        case 2:
            return number1*number2
        case 3:
            return number1/number2


def check_chain(a, b, c, d):
    possible = set()
    digits = [a, b, c, d]
    length = len(digits)
    operations = list(range(length))
    for digit_order in permutations(digits, length):
        for operation_order in product(operations, repeat=(length-1)):
            x = digit_order[0]
            try:
                for i in range(length-1):
                    x = f(x, digit_order[i+1], operation_order[i])
            except ZeroDivisionError:
                continue
            if (x % 1) == 0:
                if x >= 1:
                    possible.add(int(x))
    for i in range(1, len(possible)):
        if i not in possible:
            return (i-1)
    return (i-1)


longest = 0
for d in range(10**3):
    print(d)
    for c in range(d):
        for b in range(c):
            for a in range(b):
                out = check_chain(a, b, c, d)
                if out > longest:
                    longest = out
                    print(a, b, c, d, out)
