# Hexadecimal Numbers
from itertools import product

WAYS = list(product(range(2), repeat=3))

DIGITS = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
]


class COUNTER:
    def __init__(self, n:int) -> None:
        self.n = n
    
    def extend(self):
        

def check_f(n: int) -> int:
    count = 0
    for i in product(DIGITS, repeat=n):
        if i[0] == "0":
            continue
        if "0" not in i:
            continue
        if "1" not in i:
            continue
        if "A" not in i:
            continue
        count += 1
    return count




for i in range(3, 16):
    print(i, "-", check_f(i))
