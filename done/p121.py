# Disc Game Prize Fund
from fractions import Fraction

probs = [Fraction(1, 2), Fraction(1, 2)]
blue = [1, 0]
red = [0, 1]
for turn in range(2, 16):
    new_probs = []
    new_blue = []
    new_red = []
    chance_of_blue = Fraction(1, (turn + 1))
    for i in range(len(probs)):
        new_probs.append(probs[i] * chance_of_blue)
        new_blue.append(blue[i] + 1)
        new_red.append(red[i])
        new_probs.append(probs[i] * (1 - chance_of_blue))
        new_blue.append(blue[i])
        new_red.append(red[i] + 1)
    probs = new_probs
    blue = new_blue
    red = new_red
    assert sum(probs) == 1
    assert [(b + r) == turn for b, r in zip(blue, red)]
    assert len(blue) == len(red) == len(probs) == (2 ** (turn))
    winning_prob = Fraction(0)
    for b, r, p in zip(blue, red, probs):
        if b > r:
            winning_prob += p
    prize = Fraction(winning_prob.denominator, winning_prob.numerator).__floor__()
    print(turn, winning_prob, prize)
