# A Modified Collatz Sequence

A_NEXT = (
    lambda x: (x // 3),
    lambda x: ((4 * x + 2) // 3),
    lambda x: ((2 * x - 1) // 3),
)

LOOKUP = {"D": 0, "U": 1, "d": 2}

DESIRED_PATH = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
DESIRED_PATH = [LOOKUP[i] for i in DESIRED_PATH]
LENGTH = len(DESIRED_PATH)


def check(a):
    for i in range(LENGTH):
        r = a % 3
        if r != DESIRED_PATH[i]:
            return False
        a = A_NEXT[r](a)
    return True


def main():
    a = 10**15
    while True:
        a += 1
        print(a, end="\r")
        if check(a):
            print(a)
            print(a)
            return


if __name__ == "__main__":
    main()
