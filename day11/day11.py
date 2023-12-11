from pathlib import Path
import itertools as it

def solutions():
    data = Path("input.txt").read_text().splitlines()
    stars, cols, rows = [], [], []
    for i, r in enumerate(data):
        star = False
        for j, c in enumerate(r):
            if c == '#':
                star = True
                stars.append((i, j))
        if not star:
            rows.append(i)
    for j in range(len(data[0])):
        for i in range(len(data)):
            if data[i][j] == "#":
                break
        else: cols.append(j)

    sol1, sol2 = 0, 0
    for left, right in it.combinations(stars, 2):
        bl, sl = (left[0], right[0]) if left[0] > right[0] else (right[0], left[0])
        br, sr = (left[1], right[1]) if left[1] > right[1] else (right[1], left[1])
        diff = abs(right[0] - left[0]) + abs(right[1] - left[1])
        sol1 += diff; sol2 += diff
        for r in rows:
            if sl < r < bl:
                sol1 += 1; sol2 += 999_999  # special rows added n-1 times
        for c in cols:
            if sr < c < br:
                sol1 += 1; sol2 += 999_999  # special cols added n-1 times

    return sol1, sol2

if __name__ == "__main__":
    solutions()
            
            
