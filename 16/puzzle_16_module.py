from enum import Enum, auto
from typing import NamedTuple
from collections.abc import Callable
import heapq


class Direction(Enum):
    UP = auto()
    RIGHT = auto()
    DOWN = auto()
    LEFT = auto()

    def __hash__(self) -> int:
        return hash(self.value)

    def __lt__(self, other) -> bool:
        return self.value < other.value


Grid = list[list[str]]
State = NamedTuple("State", [("x", int), ("y", int), ("direction", Direction)])

class Dijkstra:
    def __init__(
        self,
        neighbors_fn: Callable[[State], list[State]],
        cost_fn: Callable[[State, State], float],
        min_cost: float,
        max_cost: float,
    ):
        self.cost_function = cost_fn
        self.neighbors_function = neighbors_fn
        self.previous = {}
        self.costs = {}
        self.min_cost = min_cost
        self.max_cost = max_cost

    def find_path(self, start: State):
        queue = []
        queue.append([0, start])
        self.previous = {}
        self.costs = {}
        self.costs[start] = self.min_cost
        self.previous[start] = []

        while queue:
            _, current = heapq.heappop(queue)

            for neighbor in self.neighbors_function(current):
                new_cost = self.costs[current] + self.cost_function(current, neighbor)

                if neighbor not in self.costs or new_cost < self.costs[neighbor]:
                    self.costs[neighbor] = new_cost
                    heapq.heappush(queue, [new_cost, neighbor])
                    self.previous[neighbor] = [current]

                elif new_cost == self.costs[neighbor]:
                    self.previous[neighbor].append(current)

    def get_cost(self, end: State) -> float:
        if end not in self.costs:
            return self.max_cost

        return self.costs[end]

    def get_paths(self, end: State) -> list[State]:
        path = []
        stack = [end]

        while stack:
            current = stack.pop()
            path.append(current)
            for previous in self.previous[current]:
                stack.append(State(*previous))

        return path

def neighbors_fn(
    cell: State,
    grid: Grid,
    width: int,
    height: int,
) -> list[State]:
    neighbors = []
    for direction in Direction:
        if direction == cell.direction:
            continue
        neighbors.append(State(cell.x, cell.y, direction))
    match cell.direction:
        case Direction.UP:
            if cell.y > 0 and grid[cell.y - 1][cell.x] != "#":
                neighbors.append(State(cell.x, cell.y - 1, cell[2]))
        case Direction.RIGHT:
            if cell.x < width - 1 and grid[cell.y][cell.x + 1] != "#":
                neighbors.append(State(cell.x + 1, cell.y, cell[2]))
        case Direction.DOWN:
            if cell.y < height - 1 and grid[cell.y + 1][cell.x] != "#":
                neighbors.append(State(cell.x, cell.y + 1, cell[2]))
        case Direction.LEFT:
            if cell.x > 0 and grid[cell.y][cell.x - 1] != "#":
                neighbors.append(State(cell.x - 1, cell.y, cell[2]))
    return neighbors

def cost_fn(cell1: State, cell2: State) -> int:
    if cell1.x == cell2.x and cell1.y == cell2.y:
        if cell1.direction == cell2.direction:
            return 0
        if cell1.direction in (Direction.UP, Direction.DOWN):
            if cell2.direction in (Direction.UP, Direction.DOWN):
                return 2000
            return 1000
        if cell2.direction in (Direction.UP, Direction.DOWN):
            return 1000
        return 2000
    return 1