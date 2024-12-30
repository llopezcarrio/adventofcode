import os
import puzzle_13_module

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

BUTTON_A_COST = 3
BUTTON_B_COST = 1

lines = []
f = open(file_path, "r")
for line in f:
    lines.append(line.strip())
total_cost = puzzle_13_module.process_lines(lines, 10000000000000)
print(f"Total Cost: {total_cost}")