
import os
import puzzle_22_module

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

with open(file_path, "r", encoding="utf-8") as f:
    secret_numbers = map(int, f.read().split())

sum_secret_numbers = 0
for secret_number in secret_numbers:
    for _ in range(2000):
        secret_number = puzzle_22_module.find_secret_number(secret_number)
    sum_secret_numbers += secret_number

print(sum_secret_numbers)