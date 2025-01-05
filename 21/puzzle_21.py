import os
import puzzle_21_module

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

sum_of_shortest_sequences = 0
for line in lines:
    number = int(line[:-1])
    shortest_sequence_length = puzzle_21_module.shortest_sequence(0, line, 2)
    sum_of_shortest_sequences += shortest_sequence_length * number
print(sum_of_shortest_sequences)