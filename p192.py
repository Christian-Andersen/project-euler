# Best Approximations
from fractions import Fraction
from decimal import Decimal, getcontext
from tqdm import trange

getcontext().prec = 1000

DENOMINATOR_LIMIT = 10**12

answer = 0
for n in trange(2, 100000 + 1):
    answer += (
        Fraction(str(Decimal(n).sqrt()))
        .limit_denominator(DENOMINATOR_LIMIT)
        .denominator
    )
print(answer)
Fraction(5)
