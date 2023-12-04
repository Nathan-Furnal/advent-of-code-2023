from pathlib import Path
from collections import defaultdict

def solutions():
    clean = lambda x: map(str.split, x.split(':')[1].split('|'))
    data = map(lambda x: list(clean(x)), Path("input.txt").read_text().splitlines())
    sol1 = 0
    copies = defaultdict(lambda: 1, {1: 1})
    for idx, line in enumerate(data):
        copies[idx + 1] = max(copies[idx + 1], 1)  # Puts one into the dict if no copies
        inter = set(line[0]).intersection(set(line[1]))
        if (li := len(inter)) > 0:
            sol1 += 2**(li - 1)
            for i in range(idx + 2, idx + 2 + li): # counting from 1 (not 0) and next card (+1)
                copies[i] += copies[idx + 1]  # Adds number of copies for given card

    return sol1, sum(copies.values())
        

if __name__ == "__main__":
    solutions()
