from collections import deque

Grid = list[list[str]]
Coord = tuple[int, int]

def bfs(grid: Grid, start: Coord, end: Coord) -> list[Coord]:
    q = deque([(start, [start])])  # (coord, distance, path)
    visited = set()

    while q:
        (x, y), path = q.popleft()
        if (x, y) == end:
            return path

        if (x, y) in visited:
            continue
        visited.add((x, y))

        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_y, new_x = y + dy, x + dx
            if 0 <= new_y < len(grid) and 0 <= new_x < len(grid[0]):
                if grid[new_y][new_x] != "#":
                    q.append(((new_x, new_y), path + [(new_x, new_y)]))

    return []

def find_cheats(grid: Grid, path: dict[Coord, int]):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def in_bounds(x, y):
        return 0 <= y < len(grid) and 0 <= x < len(grid[0])

    cheats = set()
    for cell in path.keys():
        x, y = cell

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and grid[ny][nx] == "#":
                nx, ny = nx + dx, ny + dy
                if (
                    in_bounds(nx, ny)
                    and grid[ny][nx] == "."
                    and path[(nx, ny)] > path[cell]
                ):
                    cheats.add((cell, (nx, ny)))

    return cheats

def calculate_savings(path: dict[Coord, int], cheat: tuple[Coord, Coord]):
    return path[cheat[1]] - path[cheat[0]] - 2

def neighbors(
    coord: Coord, grid_set: set[Coord], cheat_length: int
) -> set[Coord]:
    possible_neighbors = set()
    x, y = coord
    for dx in range(-cheat_length, cheat_length + 1):
        dy = cheat_length - abs(dx)
        possible_neighbors.add((x + dx, y + dy))
        possible_neighbors.add((x + dx, y - dy))
    return possible_neighbors.intersection(grid_set)


def distances(coord1: Coord, coord2: Coord) -> int:
    return abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])
