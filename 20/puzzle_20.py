from collections import deque
import os
import puzzle_20_module

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

with open(file_path, "r", encoding="utf-8") as f:
    grid = [list(line.strip()) for line in f]

get_point = lambda value: [
    (x, y)
    for y in range(len(grid))
    for x in range(len(grid[0]))
    if grid[y][x] == value
][0]

start = get_point("S")
end = get_point("E")

grid[start[1]][start[0]] = "."
grid[end[1]][end[0]] = "."

normal_path = puzzle_20_module.bfs(grid, start, end)

path = {cell: i for i, cell in enumerate(normal_path)}

cheats = puzzle_20_module.find_cheats(grid, path)

threshold = 100

savings = sum(1 for cheat in cheats if puzzle_20_module.calculate_savings(path, cheat) >= threshold)

print(savings)