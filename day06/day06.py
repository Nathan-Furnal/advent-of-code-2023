from pathlib import Path
import math

def solutions():
    data = Path("input.txt").read_text().splitlines()
    times = list(map(int, map(str.strip, data[0].split(':')[1].split())))
    dists = list(map(int, map(str.strip, data[1].split(':')[1].split())))
    time, dist = int(''.join(map(str, times))), int(''.join(map(str, dists)))
    solve = lambda t, d: math.ceil((-t + math.sqrt(t**2 - 4*d))/ -2 + 1e-6) # add eps to avoid pure eq
    sol1, sol2 = 1, 0
    for t, d in zip(times, dists):
        sol1 *= t - solve(t, d) * 2 + 1
    sol2 = time - solve(time, dist) * 2 + 1
    return sol1, sol2

if __name__ == "__main__":
    solutions()


# Total time is n seconds, k is time to charge
# dist = k*(n - k)
# -k² + nk - dist = 0
# delta = n**2 - 4dist
# roots = (-n +- sqrt(n**2 - 4dist)) / -2
