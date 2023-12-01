from pathlib import Path
import re
import operator as op

def solutions():
    f = lambda x: int(''.join(op.itemgetter(0, -1)(re.findall(r'\d', x))))
    nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    pat = '|'.join(nums.keys())
    sub = lambda x: ''.join(nums.get(i[0], i[1]) for i in re.findall(rf'(?=({pat}))|(\d)', x))
    data = Path("input.txt").read_text().splitlines()
    sol1 = sum(f(l) for l in data)
    sol2 = sum(f(sub(l)) for l in data)
    return sol1, sol2

if __name__ == "__main__":
    solutions()
