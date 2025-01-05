import os
from re import findall
from math import prod
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


positions = puzzle_14_module.move_robots(robots, s, w, h)

quadrants = [0, 0, 0, 0]

for pw, ph in positions:
    if pw < w//2 and ph < h//2:
        quadrants[0] += 1
    elif pw >= w//2 and ph < h//2:
        quadrants[1] += 1
    elif pw < w//2 and ph >= h//2:
        quadrants[2] += 1
    elif pw >= w//2 and ph >= h//2:
        quadrants[3] += 1

print(prod(quadrants))