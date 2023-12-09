from pathlib import Path
from itertools import pairwise

def ndiff(arr):
    sol1, sol2, i = arr[-1], 0, 0
    diff = arr[-1] - arr[-2]
    while diff != 0:
        if i % 2 == 0:
            first = arr[0]
        arr = [r - l for l, r in pairwise(arr)]
        diff = arr[-1]
        if i % 2 == 0:
            sol2 += (first - arr[0])
        sol1 += diff; i += 1
        
    return sol1, sol2
    
def solutions():
    data =  [list(map(int, x)) for x in map(str.split, Path("input.txt").read_text().splitlines())]
    sol1, sol2 = 0, 0
    for arr in data:
        s1, s2 = ndiff(arr)
        sol1 += s1; sol2 += s2
        
    return sol1, sol2
    
if __name__ == "__main__":
    solutions()
    
