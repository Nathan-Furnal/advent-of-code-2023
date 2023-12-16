from pathlib import Path
from collections import defaultdict
from itertools import chain
import sys; sys.setrecursionlimit(5000)

def goto(data: list[str], pos: tuple[int, int], direction: tuple[int, int]):
    x, y = pos
    match direction:
        case (0, 1): # east
            if data[x][y] == '|': return [(-1, 0), (1, 0)]
            elif data[x][y] == '\\': return [(1, 0)]
            elif data[x][y] == '/':  return [(-1, 0)]
            else: return [direction]
        case (0, -1): # west
            if data[x][y] == '|': return [(-1, 0), (1, 0)]
            elif data[x][y] == '\\': return [(-1, 0)]
            elif data[x][y] == '/':  return [(1, 0)]
            else: return [direction]
        case (-1, 0): # north
            if data[x][y] == '-':
                return [(0, 1), (0, -1)]
            elif data[x][y] == '\\': return [(0, -1)]
            elif data[x][y] == '/': return [(0, 1)]
            else: return [direction]
        case (1, 0): # south
            if data[x][y] == '-': return [(0, 1), (0, -1)]
            elif data[x][y] == '\\': return [(0, 1)]
            elif data[x][y] == '/': return [(0, -1)]
            else: return [direction]
        case _:
            raise ValueError(f"Unknown direction: {direction}")
        

def walk(data: list[str], pos: tuple[int, int], direction: tuple[int, int], seen: dict):
    x, y = pos; dx, dy = direction
    if (x + dx) < 0 or (y + dy) < 0 or (x + dx) >= len(data) or (y + dy) >= len(data[0]):
        return
    if (True, direction) in seen[(x, y)] and (True, direction) in seen[(x+dx, y+dy)]:
        return    
    x += dx; y += dy; seen[(x, y)].add((True, direction))
    for d in goto(data, (x,y), direction):
        walk(data, (x,y), d, seen)

# def optim(data: list[str], seen: dict[tuple[int, int], set]):
#     total = 0
#     for 

def print_tiles(tiles, seen):
    for i in range(len(tiles)):
        for j in range(len(tiles[0])):
            if (i, j) in seen: print("#", end="")
            else: print('.', end="")
        print()

def solutions():
    data = Path("input.txt").read_text().splitlines()
    seen = defaultdict(set)
    initdir = goto(data, (0, 0), (0, 1))
    for d in initdir:
        walk(data, (0, 0), d, seen)
    sol1, sol2 = len(seen), 0
    maxlen = len(seen)
    for i in range(len(data[0])): #         Going N to S from top
        for d in goto(data, (0, i), (1, 0)):
            seen = defaultdict(set)
            walk(data, (0, i), d, seen)
            maxlen = max(maxlen, len(seen))
    for i in range(len(data[0])): #         Going S to N from bottom
        for d in goto(data, (len(data)-1, i), (-1, 0)):
            seen = defaultdict(set)
            walk(data, (len(data)-1, i), d, seen)
            maxlen = max(maxlen, len(seen))
    for i in range(len(data)): #         Going E to W from right
        for d in goto(data, (i, len(data[0])- 1), (0, -1)):
            seen = defaultdict(set)
            walk(data, (i, len(data[0])- 1), d, seen)
            maxlen = max(maxlen, len(seen))
    for i in range(len(data)): #         Going W to E from left
        for d in goto(data, (i, 0), (0, 1)):
            seen = defaultdict(set)
            walk(data, (i, 0), d, seen)
            maxlen = max(maxlen, len(seen))            
    
    return sol1, maxlen

if __name__ == "__main__":
    solutions()
