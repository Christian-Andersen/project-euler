square_base = 1
square = square_base**2
summed = 0
for a in range(2, 333_333_333 + 1):
    for offset in (1, 0, -1):
        b = a + offset
        half_b, mod = divmod(b, 2)
        if (mod % 2) == 1:
            continue
        sqrt_h = a**2 - (half_b) ** 2
        if sqrt_h > square:
            square_base += 1
            square = square_base**2
        if sqrt_h != square:
            continue
        h = square
        summed += a + a + b
print(summed)
