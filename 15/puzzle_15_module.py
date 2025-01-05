from enum import Enum
from typing import List, Tuple

Grid = List[List[str]]
Coordinate = tuple[int, int]

class Directions(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

    def __repr__(self) -> str:
        match self:
            case Directions.UP:
                return "^"
            case Directions.DOWN:
                return "v"
            case Directions.LEFT:
                return "<"
            case Directions.RIGHT:
                return ">"

class EdgeError(Exception):
    pass

def parse_movement(movement: str) -> Directions:
    match movement:
        case "^":
            return Directions.UP
        case "v":
            return Directions.DOWN
        case "<":
            return Directions.LEFT
        case ">":
            return Directions.RIGHT
        case _:
            raise ValueError(f"Invalid movement: {movement}")


def parse_input(lines: List[str]) -> tuple[Grid, List[Directions]]:
    i = 0
    warehouse_grid = []
    while lines[i] != "\n":
        warehouse_grid.append(list(lines[i].strip()))
        i += 1

    movements = [
        parse_movement(movement)
        for j in range(i + 1, len(lines))
        for movement in lines[j].strip()
    ]
    return warehouse_grid, movements

def find_robot(grid: Grid) -> Coordinate:
    for y, row in enumerate(grid):
        for x, spot in enumerate(row):
            if spot == "@":
                return (x, y)
    raise ValueError("Robot not found")

def boxes_to_move(
    grid: Grid, box: Coordinate, direction: Directions
) -> list[Coordinate]:
    x, y = box
    dx, dy = direction.value
    new_x, new_y = x + dx, y + dy
    # No need to check for further boxes if there is a wall or empty space
    # Return the current box
    if grid[new_y][new_x] == "#":
        raise EdgeError("Edge of the grid")
    if grid[new_y][new_x] == ".":
        return [box]
    if grid[new_y][new_x] == "O":
        return boxes_to_move(grid, (new_x, new_y), direction) + [box]
    # Shouldn't reach here
    return []

def move_robot(grid: Grid, robot: Coordinate, direction: Directions) -> Coordinate:
    x, y = robot
    dx, dy = direction.value
    new_x, new_y = x + dx, y + dy
    # Can't move if there is a wall, return Early
    if grid[new_y][new_x] == "#":
        return robot
    # Can move freely, update the grid
    if grid[new_y][new_x] == ".":
        grid[y][x] = "."
        grid[new_y][new_x] = "@"
        return (new_x, new_y)
    # Box is in new spot, check if box can be moved
    if grid[new_y][new_x] == "O":
        try:
            boxes = boxes_to_move(grid, (new_x, new_y), direction)
        # Furthest box can't be moved, return Early
        except EdgeError:
            return robot
        for box in boxes:
            box_x, box_y = box
            new_box_x, new_box_y = box_x + dx, box_y + dy
            grid[box_y][box_x] = "."
            grid[new_box_y][new_box_x] = "O"
        grid[y][x] = "."
        grid[new_y][new_x] = "@"
        return (new_x, new_y)
    # Shouldn't reach here
    raise ValueError("Spot is invalid")

def find_boxes(grid: Grid) -> list[Coordinate]:
    return [
        (x, y)
        for y, row in enumerate(grid)
        for x, cell in enumerate(row)
        if cell in {"O", "["}
    ]

def calculate_gps_coordinate(box: Coordinate) -> int:
    return box[1] * 100 + box[0]

def scale_grid(grid: Grid) -> Grid:
    new_grid = []
    for row in grid:
        new_row = []
        for spot in row:
            match spot:
                case "O":
                    new_row.extend(["[", "]"])
                case "@":
                    new_row.extend(["@", "."])
                case "#":
                    new_row.extend(["#", "#"])
                case ".":
                    new_row.extend([".", "."])
        new_grid.append(new_row)
    return new_grid

def move_robot2(grid: Grid, robot: Coordinate, direction: Directions) -> Coordinate:
    x, y = robot
    dx, dy = direction.value
    new_x, new_y = x + dx, y + dy
    # Can't move if there is a wall, return Early
    if grid[new_y][new_x] == "#":
        return robot
    # Can move freely, update the grid
    if grid[new_y][new_x] == ".":
        grid[y][x] = "."
        grid[new_y][new_x] = "@"
        return (new_x, new_y)
    # Box is in new spot, check if box can be moved
    if grid[new_y][new_x] == "[" or grid[new_y][new_x] == "]":
        if grid[new_y][new_x] == "[":
            box = ((new_x, new_y), (new_x + 1, new_y))
        else:
            box = ((new_x - 1, new_y), (new_x, new_y))
        try:
            boxes = boxes_to_move2(grid, box, direction)
        except EdgeError:
            return robot
        match direction:
            case Directions.UP:
                boxes = sorted(boxes, key=lambda x: x[0][1])
            case Directions.DOWN:
                boxes = sorted(boxes, key=lambda x: x[0][1], reverse=True)
            case Directions.LEFT:
                boxes = sorted(boxes, key=lambda x: x[0][0])
            case Directions.RIGHT:
                boxes = sorted(boxes, key=lambda x: x[0][0], reverse=True)
        for box in boxes:
            box_l, box_r = box
            new_box_l, new_box_r = (
                (box_l[0] + dx, box_l[1] + dy),
                (box_r[0] + dx, box_r[1] + dy),
            )
            grid[box_l[1]][box_l[0]] = "."
            grid[box_r[1]][box_r[0]] = "."
            grid[new_box_l[1]][new_box_l[0]] = "["
            grid[new_box_r[1]][new_box_r[0]] = "]"
        grid[y][x] = "."
        grid[new_y][new_x] = "@"
        return (new_x, new_y)
    # Shouldn't reach here
    raise ValueError("Spot is invalid")

def boxes_to_move2(
    grid: Grid, box: Tuple[Coordinate, Coordinate], direction: Directions
) -> list[tuple[Coordinate, Coordinate]]:
    dx, dy = direction.value
    if direction in (Directions.LEFT, Directions.RIGHT):
        # same code as part 1
        x, y = box[0] if direction == Directions.LEFT else box[1]
        bracket = "]" if direction == Directions.LEFT else "["
        new_x, new_y = x + dx, y + dy
        adjacent_box = (
            ((new_x - 1, new_y), (new_x, new_y))
            if direction == Directions.LEFT
            else ((new_x, new_y), (new_x + 1, new_y))
        )
        if grid[new_y][new_x] == "#":
            raise EdgeError("Edge of the grid")
        if grid[new_y][new_x] == ".":
            return [box]
        if grid[new_y][new_x] == bracket:
            return boxes_to_move2(grid, adjacent_box, direction) + [box]
    if direction in (Directions.UP, Directions.DOWN):
        new_left, new_right = (
            (box[0][0] + dx, box[0][1] + dy),
            (box[1][0] + dx, box[1][1] + dy),
        )

        if (
            grid[new_left[1]][new_left[0]] == "#"
            or grid[new_right[1]][new_right[0]] == "#"
        ):
            raise EdgeError("Wall")

        if (
            grid[new_left[1]][new_left[0]] == "."
            and grid[new_right[1]][new_right[0]] == "."
        ):
            return [box]

        # No need to check right bracket really
        if (
            grid[new_left[1]][new_left[0]] == "["
            and grid[new_right[1]][new_right[0]] == "]"
        ):
            return boxes_to_move2(
                grid,
                ((new_left[0], new_left[1]), (new_right[0], new_right[1])),
                direction,
            ) + [box]

        left_box, right_box = [], []
        if grid[new_left[1]][new_left[0]] == "]":
            left_box = boxes_to_move2(
                grid,
                ((new_left[0] - 1, new_left[1]), (new_left[0], new_left[1])),
                direction,
            )
        if grid[new_right[1]][new_right[0]] == "[":
            right_box = boxes_to_move2(
                grid,
                ((new_right[0], new_right[1]), (new_right[0] + 1, new_right[1])),
                direction,
            )
        return left_box + right_box + [box]
    return []

def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()