from pathlib import Path
from itertools import cycle
import math

def solutions():
    data = Path("input.txt").read_text()
    dirs, maps = data.split('\n\n')
    maps = {s.split(' = ')[0]: (s.split(' = ')[1].split(', ')[0][1:], s.split(' = ')[1].split(', ')[1][:-1])
            for s in maps.strip().split('\n')}
    sol1 = 0; pos = 'AAA'
    nodes = [n for n in maps.keys() if n.endswith('A')]; steps = [0] * len(nodes)
    for d in cycle(dirs):
        pos = maps[pos][0] if d == 'L' else maps[pos][1]
        sol1 += 1
        if pos == 'ZZZ':
            break
    for i, n in enumerate(nodes):
        pos = n
        for d in cycle(dirs):
            pos = maps[pos][0] if d == "L" else maps[pos][1]
            steps[i] += 1
            if pos.endswith("Z"):
                break
        
    return sol1, math.lcm(*steps)

if __name__ == "__main__":
    solutions()
    
