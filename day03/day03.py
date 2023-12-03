from pathlib import Path
from collections import deque

def isin(data: list[str], ix: int, iy: int):
    return ix >= 0 and ix < len(data) and iy >= 0 and iy < len(data[ix])

def consume(data: list[str], ix: int, iy: int, seen: set[tuple[int, int]]) -> int:
    dq = deque(); x, y = ix, iy
    while isin(data, x, y) and (c := data[x][y]).isdigit():
        dq.appendleft(c); seen.add((x, y))
        y -= 1
    y = iy + 1 # Do not count the starting digit two times
    while isin(data, x, y) and (c := data[x][y]).isdigit():
        dq.append(c); seen.add((x, y))
        y += 1
    return int(''.join(dq)) if dq else 0

def findnum(data: list[str], ix: int, iy: int, seen: set[tuple[int, int]], part2=False) -> int:
    nums = []
    for dx, dy in [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]:
        x, y = ix + dx, iy + dy
        if isin(data, x, y) and data[x][y].isdigit() and (x, y) not in seen:
            nums.append(consume(data, x, y, seen))
    if part2:
        if data[ix][iy] == "*" and len(nums) == 2:
            return nums[0] * nums[1]
        return 0
    return sum(nums)

def solutions():
    data = Path("input.txt").read_text().splitlines()
    visited1, visited2 = set(), set()
    sol1, sol2 = 0, 0
    for i, line in enumerate(data):
        for j, char in enumerate(line):
            if not (char.isdigit() or char == '.'):
                sol1 += findnum(data, i, j, visited1)
                sol2 += findnum(data, i, j, visited2, part2=True)
    return sol1, sol2

if __name__ == "__main__":
    solutions()
