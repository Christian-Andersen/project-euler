def get_proper_divisors(x: int) -> list[int]:
    out = [1]
    for i in range(2, int(x//2)+1):
        if (x % i) == 0:
            out.append(i)
    return out


def make_chain(start_of_chain: int) -> list[int]:
    chain = [start_of_chain]
    for _ in range(10**6):
        new_number = sum(get_proper_divisors(chain[-1]))
        if new_number > 1_000_000:
            chain = None
            break
        if new_number == chain[0]:
            break
        if new_number in chain:
            chain = None
            break
        chain.append(new_number)
    else:
        raise
    return chain


for n in range(1_000_000):
    out = make_chain(n)
    if out is not None:
        print(n, len(out), out)
