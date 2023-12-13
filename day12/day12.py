from pathlib import Path
from functools import cache

@cache
def consume(springs: str, groups: tuple[int,...]):
    if not groups:
        return 1 - ('#' in springs)
    if not springs:
        return 0
    c, g = springs[0], groups[0]
    match c:
        case ".":
            consume(springs[1:], groups)
        case '#':
            if springs[:g].replace('?', '#') != g * '#':
                return 0
            if len(springs) == g:
                return 1 if len(groups) == 1 else 0
            if springs[g] in '?.':
                return consume(springs[g+1:], groups[1:])
            return 0
        case '?':
            return consume('.' + springs[1:], groups) + consume('#' + springs[1:], groups)
    return consume(springs[1:], groups)

def solutions():
    data = list(map(lambda x: (x[0], tuple(int(i) for i in x[1].split(","))),
               map(str.split, Path("input.txt").read_text().splitlines())))
    sol1, sol2 = 0, 0
    for springs, groups in data:
        sol1 += consume(springs, groups)
        sol2 += consume('?'.join(springs for _ in range(5)), groups * 5)
    return sol1, sol2

if __name__ == "__main__":
    solutions()
    
