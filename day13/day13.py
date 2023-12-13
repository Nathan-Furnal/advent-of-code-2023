"""
Thanks to https://old.reddit.com/r/adventofcode/comments/18h940b/2023_day_13_solutions/kd7m014/
for the line combining trick
"""

from pathlib import Path

def ndiff(s1: str, s2: str) -> int:
    return sum(i != j for i, j in zip(s1, s2))

def tr(pat: list[str]) -> list[str]:
    return [''.join(pat[i][j] for i in range(len(pat))) for j in range(len(pat[0]))]

def mirroring(pat: list[str], cutoff: int) -> int:
    for line in range(1, len(pat)):
        lines_to_check = min(line, len(pat) - line)
        s1 = "".join(pat[:line][::-1][:lines_to_check])  # Combine all lines in reverse
        s2 = "".join(pat[line:][:lines_to_check])        # Combine all lines
        if ndiff(s1, s2) == cutoff: # If all lines combines have `cutoff` differences then good
            return line
    return 0

def solutions():
    data = [s.split() for s in Path("input.txt").read_text().split("\n\n")]
    score = lambda g, diff: 100 * mirroring(g, diff) + mirroring(tr(g), diff)

    sol1 = sum([score(g, 0) for g in data])
    sol2 = sum([score(g, 1) for g in data])
    return sol1, sol2

if __name__ == "__main__":
    solutions()    
