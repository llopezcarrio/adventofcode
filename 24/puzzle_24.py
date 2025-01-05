import os
import puzzle_24_module

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

with open(file_path, "r", encoding="utf-8") as f:
    inputs, gates = f.read().split("\n\n")

inputs = inputs.splitlines()
inputs = {input.split(": ")[0]: int(input.split(": ")[1]) for input in inputs}
gates = gates.splitlines()

while gates:
    gate = gates.pop(0)
    if not puzzle_24_module.run_gate(gate, inputs):
        gates.append(gate)

z_bits = ((k, v) for k, v in inputs.items() if k.startswith("z"))
z_bits = sorted(z_bits, key=lambda x: x[0], reverse=True)

binary_number = int("".join(str(x[1]) for x in z_bits), 2)
print(binary_number)