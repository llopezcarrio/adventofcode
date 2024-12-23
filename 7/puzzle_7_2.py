import os


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "equations.txt")

equations = []

f = open(file_path, "r")
for line in f:

    #rule = line.rstrip('\n').split("|")

    equations.append(line.rstrip('\n'))

f.close()

totalTestValues=0

for i in range(len(equations)):
    print(i)
    testValue= equations[i].split(": ")
    numbers=testValue[1].split(" ")

    operadors = []
    total_combinations = 3 ** (len(numbers)-1)

    for i in range(total_combinations):

        tertiary = ""
        if i == 0:
            tertiary == "0"
        else:
            while i > 0:
                remainder = i % 3
                tertiary = str(remainder) + tertiary
                i //= 3

        binary_str = tertiary.zfill(len(numbers)-1)

        # Map binary string to 'A' and 'B'
        array = ['A' if bit == '0' else 'B' if bit == '1' else 'C' for bit in binary_str]

        operadors.append(array)

        # Print the generated combination (array)

    for i in range(len(operadors)):
        total = int(numbers[0])
        for j in range(len(numbers)-1):
            if operadors[i][j] == 'A':
               total = int(numbers[j+1])  + total
            if operadors[i][j] == 'B':
               total = int(numbers[j+1])  * total
            if operadors[i][j] == 'C':
               total = int(str(total) + numbers[j+1])
        if total == int(testValue[0]):
            totalTestValues += int(testValue[0])
            break


print(totalTestValues)