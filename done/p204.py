from numba import njit

@njit
def main():
    N = 1000000001

    # Create and initialize the sieve and hammings lists
    sieve = [False] * N
    sieve[0] = True
    sieve[1] = True
    hammings = [False] * N
    hammings[0] = True

    for i in range(2, N):
        if sieve[i]:
            continue
        if i > 100:
            for j in range(i, N, i):
                hammings[j] = True
        for j in range(i + i, N, i):
            sieve[j] = True

    # Calculate the answer
    answer = N - sum(hammings)

    print(answer)

if __name__=="__main__":
    main()