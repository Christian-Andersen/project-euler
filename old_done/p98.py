import json
from itertools import permutations
from pathlib import Path

SQUARES = {i**2 for i in range(10**5)}


def main() -> list[str] | None:
    with Path("0098_words.txt").open() as f:
        s = str(f.readlines()).replace("'", "")
        words = json.loads(s)

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
            look_up = dict(zip(letters, i, strict=False))
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
                return value
    return None


if __name__ == "__main__":
    main()
