import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "map.txt")

map = []
guardPositionX = 0
guardPositionY = 0
moving = "^"
i=0
lineLength = 0

f = open(file_path, "r")
for line in f:
    j = 0
    charList = []
    for char in line.rstrip('\n'):
        charList.append(char)
        if char == "^":
            lineLength =len(line.rstrip('\n'))
            guardPositionX = i
            guardPositionY = j
        j += 1
    map.append(charList)
    i+=1

f.close()

guardLeaves = False
map[guardPositionX][guardPositionY] = "X"
while guardLeaves == False:

    if moving == "^":
        if guardPositionX - 1 > 0:
           if map[guardPositionX - 1][guardPositionY] != "#":
                guardPositionX = guardPositionX - 1
                map[guardPositionX][guardPositionY] = "X"
           else:
                moving = ">"
        else:
            moving = ">"

    if moving == ">":
        if guardPositionY + 1 < lineLength:
           if map[guardPositionX][guardPositionY +1 ] != "#":
                guardPositionY = guardPositionY + 1
                map[guardPositionX][guardPositionY] = "X"
           else:
                moving = "v"
        else:
            moving = "v"

    if moving == "v":
        if guardPositionX + 1 < len(map):
           if map[guardPositionX + 1][guardPositionY] != "#":
                guardPositionX = guardPositionX + 1
                map[guardPositionX][guardPositionY] = "X"
           else:
                moving = "<"
        else:
            moving = "<"

    if moving == "<":
        if guardPositionY - 1 > 0:
           if map[guardPositionX][guardPositionY - 1] != "#":
                guardPositionY = guardPositionY - 1
                map[guardPositionX][guardPositionY] = "X"
           else:
                moving = "^"
        else:
            moving = "^"

    if guardPositionX == len(map) - 1 or guardPositionX == 0 or guardPositionY == lineLength-1 or guardPositionY == 0:
        guardLeaves = True

countX = 0
for i in range(len(map)):
    for j in range(lineLength):
        if map[i][j] == "X":
            countX += 1

print(countX)