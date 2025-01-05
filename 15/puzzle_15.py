
import os
import puzzle_15_module


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

warehouse_grid, movements = puzzle_15_module.parse_input(lines)
robot = puzzle_15_module.find_robot(warehouse_grid)

for movement in movements:
    robot = puzzle_15_module.move_robot(warehouse_grid, robot, movement)

boxes = puzzle_15_module.find_boxes(warehouse_grid)
coordinates = sum(map(puzzle_15_module.calculate_gps_coordinate, boxes))

print(coordinates)