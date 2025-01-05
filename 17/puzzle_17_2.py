import os
import puzzle_17_module

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines()
    registers = {}
    registers["A"] = int(lines[0].split(":")[1].strip())
    registers["B"] = int(lines[1].split(":")[1].strip())
    registers["C"] = int(lines[2].split(":")[1].strip())

    program = list(map(int, lines[4].split(":")[1].strip().split(",")))

quine_value = puzzle_17_module.find_quine(program, registers)
print(f"ANSWER2: { quine_value = }")