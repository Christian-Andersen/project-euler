import json
from itertools import permutations

SQUARES = set(i**2 for i in range(10**5))

with open("0098_words.txt", "r") as f:
    s = str(f.readlines()).replace("'", "")
    words = json.loads(s)
words_set = set(words)

pals = {}
for word in words:
    sorted_word = "".join(sorted(word))
    if sorted_word not in pals:
        pals[sorted_word] = []
    pals[sorted_word].append(word)
pals = {k: v for k, v in pals.items() if len(v) != 1}
for key, value in pals.items():
    letters = set(key)
    for i in permutations(range(10), len(letters)):
        look_up = {k: v for k, v in zip(letters, i)}
        is_square = len(value) * [False]
        scores = []
        for idx, word in enumerate(value):
            number = ""
            for letter in word:
                number += str(look_up[letter])
            if number.startswith("0"):
                continue
            number = int(number)
            if number in SQUARES:
                is_square[idx] = True
                scores.append(number)
        if all(is_square):
            print(value, scores)
