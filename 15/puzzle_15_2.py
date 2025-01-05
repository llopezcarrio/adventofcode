import os
import puzzle_15_module

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

warehouse_grid, movements = puzzle_15_module.parse_input(lines)
warehouse_grid_scaled = puzzle_15_module.scale_grid(warehouse_grid)
robot = puzzle_15_module.find_robot(warehouse_grid_scaled)

for movement in movements:
    robot = puzzle_15_module.move_robot2(warehouse_grid_scaled, robot, movement)

boxes = puzzle_15_module.find_boxes(warehouse_grid_scaled)
coordinates = sum(map(puzzle_15_module.calculate_gps_coordinate, boxes))
print(coordinates)
puzzle_15_module.print_grid(warehouse_grid_scaled)