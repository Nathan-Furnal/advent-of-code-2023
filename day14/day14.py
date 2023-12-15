from pathlib import Path
from collections import defaultdict

def roll(rocks: list[list[str]], pos: tuple[int, int], direction: str):
    x, y = pos
    dx = -1 if direction == "N" else 1 if direction == "S" else 0
    dy = -1 if direction == "W" else 1 if direction == "E" else 0
    while (0 <= x+dx < len(rocks)) and (0 <= y+dy < len(rocks[0])) and (rocks[x + dx][y + dy] == "."):
           x += dx; y += dy;
    rocks[pos[0]][pos[1]] = "."
    rocks[x][y] = 'O'

def roll_all(rocks: list[list[str]], direction: str):
    match direction:
        case 'N':
            for i in range(1, len(rocks)):
                for j in range(len(rocks[0])):
                    if rocks[i][j] == 'O': roll(rocks, (i,j), direction)
        case 'S':
            for i in range(len(rocks)-1, -1, -1):
                for j in range(len(rocks[0])):
                    if rocks[i][j] == 'O': roll(rocks, (i,j), direction)
        case 'W':
            for j in range(1, len(rocks[0])):
                for i in range(len(rocks)):
                    if rocks[i][j] == 'O': roll(rocks, (i,j), direction)
        case 'E':
            for j in range(len(rocks[0])-1, -1, -1):
                for i in range(len(rocks)):
                    if rocks[i][j] == 'O': roll(rocks, (i,j), direction)
        case _: raise ValueError(f"Unknown direction: {direction}")

def spin(rocks: list[list[str]]):
    for d in 'NWSE':
        roll_all(rocks, d)

def load(rocks: list[list[str]]):
    return sum(len(rocks) - i for j in range(len(rocks[0])) for i in range(len(rocks)) if rocks[i][j] =="O")

def solutions():
    data = [list(l) for l in Path("input.txt").read_text().split()]
    N_CYCLES = 1000000000
    roll_all(data, 'N')
    sol1, sol2 = load(data), 0
    cache = defaultdict(list)
    cache[str(data)].append(0)
    past_cycles, i = [], 0
    while True:
        s = str(data)
        past_cycles.append(s)        
        cache[s].append(i)        
        spin(data)
        i += 1; s = str(data)
        if len(cache[s]) > 1:
            break
    clen = cache[s][1] - cache[s][0]
    sol2 = load(eval(past_cycles[(N_CYCLES - cache[s][0])%clen + cache[s][0]]))
    return sol1, sol2

if __name__ == "__main__":
    solutions()
