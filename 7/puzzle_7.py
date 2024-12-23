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
    testValue= equations[i].split(": ")
    numbers=testValue[1].split(" ")

    operadors = []
    total_combinations = 2 ** (len(numbers)-1)  # There are 2^n combinations

    # Iterate over all numbers from 0 to 2^n - 1
    for i in range(total_combinations):
        # Convert the number to a binary string, ensuring it has exactly n bits
        binary_str = format(i, f'0{len(numbers)-1}b')

        # Map binary string to 'A' and 'B'
        array = ['A' if bit == '0' else 'B' for bit in binary_str]

        operadors.append(array)

        # Print the generated combination (array)

    for i in range(len(operadors)):
        total = int(numbers[0])
        for j in range(len(numbers)-1):
            if operadors[i][j] == 'A':
               total = int(numbers[j+1])  + total
            if operadors[i][j] == 'B':
               total = int(numbers[j+1])  * total
        if total == int(testValue[0]):
            totalTestValues += int(testValue[0])
            break


print(totalTestValues)