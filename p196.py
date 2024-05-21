# Prime Triplets

def is_prime():
    return #TODO

def get_triangular_number(n: int) -> int:
    return n*(n+1)//2

def get_row(n: int) -> list[int]:
    return list(range(get_triangular_number(n-1)+1, get_triangular_number(n)+1))

def get_prime_triplets(n: int) -> list[int]:
    rows = []
    for i in range(5):
        row = get_row(n + i - 2)



def main():
    print(get_row(2))

if __name__=="__main__":
    main()
