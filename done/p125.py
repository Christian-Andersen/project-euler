from tqdm import tqdm


N = 10**8
print('Generating palindromes')
pals = [i for i in tqdm(range(N)) if str(i) == str(i)[::-1]]
print(f'Found {len(pals)} pals')


def is_sum_of_squares(x):
    for i in range(1, int((x**0.5)/2)):
        base = i
        summed = base**2
        while True:
            base += 1
            summed += base**2
            if summed > x:
                break
            if summed == x:
                return True
    return False


print('Iterating Over Pals')
total = 0
for i in tqdm(pals):
    if is_sum_of_squares(i):
        total += i
print('Done')
print(total)
