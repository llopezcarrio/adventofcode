import os
import copy

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
            startGuardPositionX = i
            StartGuardPositionY = j
        j += 1
    map.append(charList)
    i+=1

f.close()

countBlockers = 0

for i in range(len(map)):

    for j in range(lineLength):
        print(i,j)
        mapAux = copy.deepcopy(map)
        if mapAux[i][j] == ".":

            mapAux[i][j] = "#"
            guardPositionX= startGuardPositionX
            guardPositionY= StartGuardPositionY
            moving = "^"

            guardLeaves = False
            while guardLeaves == False:

                if moving == "^":
                    if guardPositionX - 1 >= 0:
                        if mapAux[guardPositionX - 1][guardPositionY] != "#" and mapAux[guardPositionX - 1][guardPositionY] != "O":
                            guardPositionX = guardPositionX - 1
                        else:
                            moving = ">"
                            if mapAux[guardPositionX-1][guardPositionY] == "O":
                                countBlockers += 1
                                break
                            else:
                                mapAux[guardPositionX-1][guardPositionY] = "O"
                    else:
                        moving = ">"

                if moving == ">":
                    if guardPositionY + 1 < lineLength:
                        if mapAux[guardPositionX][guardPositionY +1 ] != "#" and mapAux[guardPositionX][guardPositionY+1] != "O":
                            guardPositionY = guardPositionY + 1
                        else:
                            moving = "v"
                    else:
                        moving = "v"

                if moving == "v":
                    if guardPositionX + 1 < len(map):
                        if mapAux[guardPositionX + 1][guardPositionY] != "#" and mapAux[guardPositionX + 1][guardPositionY] != "O":
                            guardPositionX = guardPositionX + 1
                        else:
                            moving = "<"
                    else:
                        moving = "<"

                if moving == "<":
                    if guardPositionY - 1 >= 0:
                        if mapAux[guardPositionX][guardPositionY - 1] != "#" and mapAux[guardPositionX][guardPositionY-1] != "O":
                            guardPositionY = guardPositionY - 1
                        else:
                            moving = "^"
                    else:
                        moving = "^"

                if guardPositionX == len(map) - 1 or guardPositionX == 0 or guardPositionY == lineLength-1 or guardPositionY == 0:
                    guardLeaves = True

print(countBlockers)