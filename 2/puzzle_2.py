import puzzle_2_module
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

f = open(file_path, "r")
safeReports = 0
for line in f:
    levels = line.split(' ')
    safeReport = 1
    level = 0
    countBadIncreaseDecrease = 0
    countIncrease = 0
    countDecrease = 0

    while (level < len(levels)-1):
        badIncreaseDecrease, pattern = puzzle_2_module.validateSafeReport(int(levels[level]), int(levels[level+1]))
        if badIncreaseDecrease:
            safeReport = 0
            break
        if pattern == "increase":
            countIncrease += 1
        if pattern == "decrease":
            countDecrease += 1
        if (countIncrease > 1 and countDecrease > 0) or (countIncrease > 0 and countDecrease > 1):
            safeReport = 0
            break
        level += 1

    safeReports += safeReport

print(safeReports)

f.close()