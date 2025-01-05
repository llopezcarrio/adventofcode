import os
import puzzle_24_module

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

with open(file_path, "r", encoding="utf-8") as f:
    gates = f.read().split("\n\n")[1]

gates = gates.splitlines()

swaps = puzzle_24_module.get_swaps(gates)
swaps = ",".join(sorted(swaps))
print(f"ANSWER2: { swaps = }")