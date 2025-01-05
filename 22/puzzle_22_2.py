from typing import Counter
import os
import puzzle_22_module


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

with open(file_path, "r", encoding="utf-8") as f:
    secret_numbers = map(int, f.read().split())

banana_sequences = Counter()
for secret_number in secret_numbers:
    prices, changes = puzzle_22_module.get_prices_and_changes(secret_number)
    sequences = puzzle_22_module.get_banana_sequences(prices, changes)
    banana_sequences.update(sequences)

max_sequence = max(banana_sequences.values())
print(max_sequence)