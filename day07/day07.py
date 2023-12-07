from pathlib import Path
from collections import Counter
from itertools import groupby

def solutions():
    orders = {'T': 'A', 'J': 'B', 'Q': 'C', 'K': 'D', 'A': 'E'} # lexicographic reorder
    order = lambda x, p2: '1' if (x == 'J' and p2) else orders.get(x, x)
    data = [*map(str.split, Path("input.txt").read_text().splitlines())]
    part1, part2 = [], []
    for line in data:
        mc = Counter(line[0]).most_common()
        s1, s2 = line[0], line[0]
        part1.append(((mc[0][1], mc[1][1] if len(mc) > 1 else 0), s1, int(line[1])))
        for char, _ in mc:
            if char != 'J':
                s2 = s2.replace('J', char)
                mc = Counter(s2).most_common()
                break
        part2.append(((mc[0][1], mc[1][1] if len(mc) > 1 else 0), s2, line[0], int(line[1])))

    sol1, sol2, i1, i2 = 0, 0, 1, 1
    keyfunc = lambda x: x[0]
    group1 = groupby(sorted(part1, key=keyfunc), key=keyfunc)
    group2 = groupby(sorted(part2, key=keyfunc), key=keyfunc)
    
    for (_, g1), (_, g2) in zip(group1, group2):
        for el in sorted(g1, key=lambda x: [order(c, False) for c in x[1]]):
            sol1 += i1 * el[2]; i1 += 1
        for el in sorted(g2, key=lambda x: [order(c, True) for c in x[2]]):
            sol2 += i2 * el[3]; i2 += 1
            
    return sol1, sol2

if __name__ == "__main__":
    solutions()
