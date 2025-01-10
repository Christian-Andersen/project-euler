def main():
    MM = 2000
    print("Generating Squares")
    squares = set(i**2 for i in range(MM**2 + (2 * MM) ** 2 + 1))
    print("Done")

    def paths(M):
        count = 0
        for a in range(1, M + 1):
            for b in range(1, a + 1):
                for c in range(1, b + 1):
                    if (a**2 + (b + c) ** 2) in squares:
                        count += 1
        return count


if __name__ == "__main__":
    main()
