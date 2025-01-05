import os
import puzzle_18_module

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")


with open(file_path, "r", encoding="utf-8") as f:
    falling_bytes: list[puzzle_18_module.Coordinate] = [
        (int(x), int(y)) for line in f for x, y in [line.strip().split(",")]
    ]

width, height = 71, 71

grid = [["." for _ in range(width)] for _ in range(height)]

index = 2913
for x, y in falling_bytes[:index]:
    grid[y][x] = "#"

# print_grid(grid)

start: puzzle_18_module.Coordinate = (0, 0)
end: puzzle_18_module.Coordinate = (width - 1, height - 1)

i = index
while i < len(falling_bytes):
    falling_byte = falling_bytes[i]
    grid[falling_byte[1]][falling_byte[0]] = "#"

    dijkstra = puzzle_18_module.Dijkstra(
        lambda cell: puzzle_18_module.adjacent_neighbors_fn(cell, grid, width, height),
        puzzle_18_module.neutral_cost_fn,
        0.0,
        float("inf"),
    )

    min_cost = float("inf")
    dijkstra.find_path(start)
    min_cost = dijkstra.get_cost(end)
    if min_cost == float("inf"):
        break

    i += 1

print(falling_bytes[i])