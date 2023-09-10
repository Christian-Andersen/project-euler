import sys

NUMBERS = [str(i) for i in range(1, 10)]
sys.set_int_max_str_digits(0)
# Hi


def is_pan(s):
    return all([i in s for i in NUMBERS])


k = 2
fk = 1
fk1 = 1
while True:
    k += 1
    fk, fk1 = fk + fk1, fk
    s = str(fk)
    if is_pan(s[-9:]):
        if is_pan(s[:9]):
            print(k)
