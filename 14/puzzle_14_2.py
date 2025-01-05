from re import findall
from operator import itemgetter
import os
import puzzle_14_module

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

w = 101
h = 103
s = 100
robots = []
quadrants = [0,0,0,0]

f = open(file_path, "r")

for line in f:
    robot=line.strip()

    pw, ph, vw, vh = map(int, findall(r"-?\d+", robot))
    robots.append((pw,ph,vw,vh))


tree_time = 0
maxTime = range(w * h)
positions = [puzzle_14_module.move_robots(robots, s, w, h) for s in maxTime]

for i in range(1, min(w, h)):
    a, b, c, d = 0 + i, w - 1 - i, 0 + i, h - 1 - i

    area = (b - a + 1) * (d - c + 1)

    densities = [
        sum(a <= pw <= b and c <= ph <= d for pw, ph in position) / area for position in positions
    ]

    time, max_density = max(zip(maxTime, densities), key=itemgetter(1))

    if time == tree_time:
        break

    tree_time = time

print(tree_time)