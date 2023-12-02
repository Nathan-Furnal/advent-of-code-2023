from pathlib import Path
import re

def solutions():
    d = {"red": 12, "green": 13, "blue": 14}
    f = lambda x: re.findall(r"(\d+)\s(blue|green|red)", x)
    data = Path("input.txt").read_text().splitlines()
    sol1, sol2 = 0, 0
    for l in data:
        dd = {"red": 0, "green": 0, "blue": 0}
        for v, k in f(l):
            dd[k] = max(int(v), dd.get(k, 0))
            
        if all(dd[k] <= d[k] for k in d):
            sol1 += int(l.split(':')[0][5:])
            
        sol2 += dd["green"] * dd["blue"] * dd["red"]
            
    return sol1, sol2

if __name__ == "__main__":
    solutions()
