import os
import puzzle_19_module

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

with open(file_path, "r", encoding="utf-8") as f:
    part1, part2 = f.read().split("\n\n")
    towels = set(part1.split(", "))

    designs = part2.splitlines()

possible_designs = sum(puzzle_19_module.is_possible(towels, design) for design in designs)

print(f"ANSWER1: { possible_designs = }")