from collections import defaultdict
from itertools import combinations
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "map.txt")

if __name__ == "__main__":
    # Reading the input into a grid
    grid = []


    for line in open(file_path).read().splitlines():
        grid.append(line)

    x_max = len(grid) - 1
    y_max = len(grid[0]) - 1

    def in_grid(a):
        return  0 <= a[0] <= x_max and 0 <= a[1] <= y_max

    def find_antinodes(ant1, ant2):
        diff_x = ant1[0] - ant2[0]
        diff_y = ant1[1] - ant2[1]
        return {(ant1[0] + diff_x, ant1[1] + diff_y),
                (ant2[0] - diff_x, ant2[1] - diff_y)}

    def find_harmonic_antinodes(ant1, ant2):
        antinodes = set()
        diff_x = ant1[0] - ant2[0]
        diff_y = ant1[1] - ant2[1]

        curr = ant1[0], ant1[1]
        while in_grid(curr):
            antinodes.add(curr)
            curr = curr[0] + diff_x, curr[1] + diff_y

        curr = ant2[0], ant2[1]
        while in_grid(curr):
            antinodes.add(curr)
            curr = curr[0] - diff_x, curr[1] - diff_y

        return antinodes

    antennas = defaultdict(list)
    for i, row in enumerate(grid):
        for j, c in enumerate(row):
            if c != ".":
                antennas[c].append((i,j))

    antinodes = set()
    harmonic_antinodes = set()
    for c, ant_list in antennas.items():
        print(c)
        for ant1, ant2 in combinations(ant_list, 2):
            antinodes = antinodes.union(find_antinodes(ant1, ant2))
            harmonic_antinodes = harmonic_antinodes.union(find_harmonic_antinodes(ant1, ant2))

    antinodes = {a for a in antinodes if in_grid(a)}
    #print(antinodes)
    print("Solution 1: ", len(antinodes))
    #print("Solution 2: ", len(harmonic_antinodes))