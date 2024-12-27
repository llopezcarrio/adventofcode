import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "disk.txt")


disk = []

f = open(file_path, "r")
for line in f:
    disk = line.rstrip('\n')
f.close()

blocks = []

i = 0
position = 0
indexUseSpaceBlocks = 0
useSpaceBlocksPositions = []

freeSpaceCount = 0

while i < len(disk):

   if i % 2 == 0:
        value = indexUseSpaceBlocks
        for j in range(int(disk[i])):
            blocks.append(value)
            useSpaceBlocksPositions.append(position)
            position += 1
        indexUseSpaceBlocks +=1
   else:
        value = "."
        for j in range(int(disk[i])):
            blocks.append(value)
            freeSpaceCount += 1
            position += 1

   i += 1


checksum = 0
for i in range(len(blocks)):
    if blocks[i] == ".":
        if freeSpaceCount > 0 and useSpaceBlocksPositions[len(useSpaceBlocksPositions)-1] > i:
            tmp = blocks[i]
            blocks[i] = blocks[useSpaceBlocksPositions[len(useSpaceBlocksPositions)-1]]
            blocks[useSpaceBlocksPositions[len(useSpaceBlocksPositions)-1]] = tmp
            useSpaceBlocksPositions.pop()
            freeSpaceCount -= 1
            checksum += (blocks[i] * i)
        else:
            break
    else:
        checksum += (blocks[i] * i)

print(checksum)