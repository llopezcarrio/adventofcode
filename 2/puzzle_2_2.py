import puzzle_2_module
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input2.txt")

f = open(file_path, "r")
safeReports = 0
for line in f:
    print(line)
    levels = line.split(' ')

    position = 0
    totalLevels = len(levels)
    safeReport = 1

    validatingLevels = True

    while validatingLevels:

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

        if safeReport == 1:
            break

        if position > totalLevels - 1:
            validatingLevels = False
        else:
            safeReport = 1
            levels = line.split(' ')
            del levels[position]
            position += 1

    safeReports += safeReport

print(safeReports)


f.close()