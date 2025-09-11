# Largest Palindrome Product
def is_palindrome(x):
    str_x = str(x)
    return str_x == str_x[::-1]


def main():
    largest_palindrome = 0
    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            x = i * j
            if x < largest_palindrome:
                break
            if not is_palindrome(x):
                continue
            largest_palindrome = x
    return largest_palindrome


if __name__ == "__main__":
    print(main())
