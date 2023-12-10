from pathlib import Path

def is_walkable(arr2d: list[str], src: tuple[int, int], delta: tuple[int, int]):
    dest = (src[0] + delta[0], src[1] + delta[1])
    # Only necessary in the example, actual input doesn't touch the border of the grid
    # if dest[0] < 0 or dest[0] >= len(arr2d) or dest[1] < 0 or dest[1] >= len(arr2d[dest[0]]):
    #     return False
    pos, new_pos = arr2d[src[0]][src[1]], arr2d[dest[0]][dest[1]]
    match delta:
        case (-1, 0):
            return pos in 'S|LJ' and new_pos in 'S|F7'
        case (1, 0):
            return pos in 'S|F7' and new_pos in 'S|LJ'
        case (0, -1):
            return pos in 'S-J7' and new_pos in 'S-FL'
        case (0, 1):
            return pos in 'S-FL' and new_pos in 'S-J7'
        case _:
            raise ValueError(f"Unknown direction: {delta}")

def walk(arr2d: list[str]):
    start = (-1, -1)
    for idx, line in enumerate(arr2d):
        if (si := line.find('S')) != -1:
            start = (idx, si)
            break
    prev = pos = start
    visited, sol1 = {start}, 1
    for d in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        if is_walkable(arr2d, pos, d):
            pos = (pos[0] + d[0], pos[1] + d[1])
            visited.add(pos)
            break
    while pos != start:
        for d in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
            if is_walkable(arr2d, pos, d) and (new_pos := (pos[0] + d[0], pos[1] + d[1])) != prev:
                prev = pos
                pos = new_pos
                visited.add(pos)
                sol1 += 1
                break
    # The furthest point is the halfway point since there is only one main loop
    return sol1 // 2, visited

def solutions():
    # Logic for part2 comes from https://www.youtube.com/watch?v=YiX9clrJBXA
    data = Path("input.txt").read_text().splitlines()
    sol2 = 0
    sol1, visited = walk(data)
    for i in range(len(data)):
        parity = 0  # https://en.wikipedia.org/wiki/Nonzero-rule
        for j in range(len(data[i])):
            if not (i, j) in visited:
                if parity % 2 == 1:
                    sol2 += 1
                continue # if the point is not in the path, don't update parity
            if data[i][j] in '|LJ': # Or '|F7', any of those on an *horizontal* line changes parity
                parity += 1
            
    return sol1, sol2

if __name__ == "__main__":
    solutions()

