from pathlib import Path
import itertools as it

def minloc(seeds: list[int], maps: list[list[tuple[int, int, int]]]):
    sol = seeds[0]
    for seed in seeds:
        for _map in maps:
            for dest, source, length in _map:
                if source <= seed < source + length:
                    seed += -source + dest
                    break
        sol = sol if sol < seed else seed
    return sol

def intervals(locs: list[range],  _map: list[tuple[int, int, int]]):
    next_locs = []
    for r in locs:
        stop = False
        for dest, source, length in _map:
            if source <= r.start < r.stop <= source + length:
                stop = True
                next_locs.append(range(r.start - source + dest, r.stop - source + dest))
                break
            if source < r.start < source + length <= r.stop:
                next_locs.append(range(r.start - source + dest, dest + length))
                next_locs.append(range(source + length, r.stop))
                break
            if r.start < source and source + length <= r.stop:
                next_locs.append(range(dest, dest + length))
                next_locs.append(range(source + length, r.stop))
                break
        if not stop:
            next_locs.append(r)
    return next_locs

def rangeloc(ranges, maps):
    allranges = []
    for _map in maps:
        ranges = intervals(ranges, _map)
        allranges.append(ranges)
    return min(map(lambda x: x.start, it.chain.from_iterable(allranges)))

def solutions():
    data = Path("input.txt").read_text().split('\n\n')
    seeds = [int(s) for s in data[0].split(': ')[1].split(' ')]
    ranges = [range(i, i+j) for i, j in it.batched(seeds, 2)]
    maps = []
    sol1, sol2 = seeds[0], seeds[0]
    for m in data[1:]:  # For each mapping, put it in a list and the triplets in tuples
        tmp = []
        for vals in m.split(':')[1].strip().split('\n'):
            tmp.append(tuple(map(int, vals.split())))
        maps.append(sorted(tmp, key=lambda x: x[1])) # Sort on source start
    sol1 = minloc(seeds, maps)
    sol2 = rangeloc(ranges, maps)
    return sol1, sol2
                

if __name__ == "__main__":
    solutions()
