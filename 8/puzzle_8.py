import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "map.txt")

map = []
lineLenght = 0

f = open(file_path, "r")
for line in f:
    map.append(line.rstrip('\n'))
    lineLenght = len(line.rstrip('\n'))
f.close()

frequenciesType=[]
frequenciesPositions=[]
frequenciesPositionsIndex = 0

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] != '.':
           foundType = False
           for k in range(len(frequenciesType)):
               if frequenciesType[k] == map[i][j]:
                   frequenciesPositions.append([k,i,j])
                   foundType = True
                   break
           if not foundType:
              frequenciesType.append(map[i][j])
              frequenciesPositions.append([len(frequenciesType)-1, i, j])


# Sort by the first position (index 0)
frequenciesPositions = sorted(frequenciesPositions, key=lambda x: x[0])

countAntiNodes = []
for i in range(len(frequenciesType)):
    print(frequenciesType[i])
    for j in range(len(frequenciesPositions)-1):
        if frequenciesPositions[j][0] == i:
            for k in range(j+1, len(frequenciesPositions)):
                if frequenciesPositions[k][0] == i:
                    col = frequenciesPositions[j][2] - frequenciesPositions[k][2]
                    row = frequenciesPositions[j][1] - frequenciesPositions[k][1]
                    if frequenciesPositions[j][2] + col >= 0 and frequenciesPositions[j][2] + col < lineLenght and frequenciesPositions[j][1] + row >=0  and frequenciesPositions[j][1] + row < len(map):
                        countAntiNodes.append([frequenciesPositions[j][1] + row,frequenciesPositions[j][2] + col])
                        print(frequenciesPositions[j][1] + row, frequenciesPositions[j][2] + col)
                    if frequenciesPositions[k][2] - col >= 0 and frequenciesPositions[k][2] - col < lineLenght and frequenciesPositions[k][1] - row >=0  and frequenciesPositions[k][1] - row < len(map):
                        countAntiNodes.append([frequenciesPositions[k][1] - row,frequenciesPositions[k][2] - col])
                        print(frequenciesPositions[k][1] - row, frequenciesPositions[k][2] - col)

cleanDuplicates = []
for i in range(len(countAntiNodes)):
    duplicateNode = False
    for j in range(len(cleanDuplicates)):
        if countAntiNodes[i][0] == cleanDuplicates[j][0] and countAntiNodes[i][1] == cleanDuplicates[j][1]:
            duplicateNode = True
            break
    if not duplicateNode:
        cleanDuplicates.append(countAntiNodes[i])

print(len(cleanDuplicates))