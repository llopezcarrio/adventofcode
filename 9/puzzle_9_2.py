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
            useSpaceBlocksPositions.append([position, int(disk[i])])
            position += 1
        indexUseSpaceBlocks +=1
   else:
        value = "."
        for j in range(int(disk[i])):
            blocks.append(value)
            freeSpaceCount += 1
            position += 1

   i += 1


while len(useSpaceBlocksPositions) > 0:
    requiredSpace = useSpaceBlocksPositions[len(useSpaceBlocksPositions)-1][1]
    enoughSpace = False
    print(len(useSpaceBlocksPositions))
    for i in range(len(blocks)):
        if blocks[i] == "." and useSpaceBlocksPositions[len(useSpaceBlocksPositions)-1][0] > i:
            freeSpace = 1
            isFreeSpace = True
            while isFreeSpace:
                if blocks[i + freeSpace] == ".":
                    freeSpace += 1
                else:
                     isFreeSpace = False

            if freeSpace >= requiredSpace:
                for j in range(requiredSpace):
                    blocks[i + j] = blocks[useSpaceBlocksPositions[len(useSpaceBlocksPositions)-1][0]]
                    blocks[useSpaceBlocksPositions[len(useSpaceBlocksPositions)-1][0]] = "."
                    useSpaceBlocksPositions.pop()
                enoughSpace = True
                break

    if not enoughSpace:
        for j in range(requiredSpace):
                    useSpaceBlocksPositions.pop()

checksum = 0
for i in range(len(blocks)):
   if blocks[i] != ".":
        checksum += (blocks[i] * i)

print(checksum)