# Even Fibonacci Numbers
from itertools import count


def fib(x):
    if x == 0:
        return 1
    if x == 1:
        return 2
    return fib(x - 1) + fib(x - 2)


def main():
    answer = 0
    for i in count():
        fib_i = fib(i)
        if fib_i > 4_000_000:
            break
        if (fib_i % 2) == 0:
            answer += fib_i
    return answer


if __name__ == "__main__":
    print(main())
