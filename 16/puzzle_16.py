
import os
import puzzle_16_module

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

with open(file_path, "r", encoding="utf-8") as f:
    grid = [list(line.strip()) for line in f]

height, width = len(grid), len(grid[0])

start: puzzle_16_module.State | None = None
ends: list[puzzle_16_module.State] | None = None

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == "S":
            start = puzzle_16_module.State(x, y, puzzle_16_module.Direction.RIGHT)
        if cell == "E":
            ends = [
                puzzle_16_module.State(x, y, puzzle_16_module.Direction.UP),
                puzzle_16_module.State(x, y, puzzle_16_module.Direction.RIGHT),
                puzzle_16_module.State(x, y, puzzle_16_module.Direction.DOWN),
                puzzle_16_module.State(x, y, puzzle_16_module.Direction.LEFT),
            ]

assert start is not None
assert ends is not None

dijkstra = puzzle_16_module.Dijkstra(
    lambda cell: puzzle_16_module.neighbors_fn(cell, grid, width, height),
    puzzle_16_module.cost_fn,
    0.0,
    float("inf"),
)

min_cost = float("inf")
dijkstra.find_path(start)
for end in ends:
    min_cost = min(min_cost, dijkstra.get_cost(end))

print(int(min_cost))