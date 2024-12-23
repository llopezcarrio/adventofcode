import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "rules.txt")

rules = []

f = open(file_path, "r")
for line in f:
    rule = line.rstrip('\n').split("|")
    rules.append(rule)
f.close()

file_path = os.path.join(script_dir, "updates.txt")

updates = []

f = open(file_path, "r")
for line in f:
    update = line.rstrip('\n').split(",")
    updates.append(update)
f.close()

addMiddle = 0

for i in range(0, len(updates)):
    validUpdate = True
    exitLoop = False
    while exitLoop == False:
        for z in range(0, len(updates[i])-1):
            page1 = updates[i][z]
            page2 = updates[i][z+1]

            validRule = False
            for y in range(0, len(rules)):
                if page1 == rules[y][0] and page2 == rules[y][1]:
                    validRule = True
                    exitLoop = True
                    break
            if not validRule:
                validUpdate = False
                updates[i][z] = page2
                updates[i][z+1] = page1
                exitLoop = False
                break

            if z == len(updates[i])-1:
                exitLoop = True


    if not validUpdate:
       aux= int((z+2)/2)
       addMiddle += int(updates[i][aux])

print(addMiddle)