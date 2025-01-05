def get_r_max(a):
    r_s = []
    r_max = 0
    for n in range(2 * a):
        lhs = (a - 1) ** n + (a + 1) ** n
        r = lhs % (a**2)
        r_s.append(r)
        r_max = max(r_max, r)
    return r_max


summed = 0
for a in range(3, 1000 + 1):
    summed += get_r_max(a)
print(summed)
