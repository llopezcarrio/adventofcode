import os
def parse_schematic(lines: list[str]) -> tuple[int, ...]:
    heights = [-1 for _ in range(5)]
    for line in lines:
        for j, char in enumerate(line):
            if char == "#":
                heights[j] += 1
    return tuple(heights)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

locks = set()
keys = set()

for i in range(0, len(lines), 8):
    # If top line is all filled, it's a lock
    if lines[i] == "#####":
        locks.add(parse_schematic(lines[i : i + 8]))
    else:
        keys.add(parse_schematic(lines[i : i + 8]))

fits = 0
for lock in locks:
    for key in keys:
        if all(
            lock_height + key_height <= 5
            for lock_height, key_height in zip(lock, key)
        ):
            fits += 1

print(fits)