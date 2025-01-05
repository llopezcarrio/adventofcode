import puzzle_4_module
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

f = open(file_path, "r")

letterSoup = []
lineLen = 0
colLen = 0

for line in f:
    letterSoup.append(line)
    lineLen = len(line)
f.close()

count = 0
colLen = len(letterSoup)

for i in range(0, len(letterSoup)):

    for c in range(0, len(letterSoup[i])):
        word=letterSoup[i][c]

        if word == "X" or word == "S":
           #Find Horrizontally
           if c+3 < lineLen:
                word += letterSoup[i][c+1]
                word += letterSoup[i][c+2]
                word += letterSoup[i][c+3]
                count += puzzle_4_module.validateWord(word)

           #Find Vertically
           if i+3 < colLen:
                word=letterSoup[i][c]
                word += letterSoup[i+1][c]
                word += letterSoup[i+2][c]
                word += letterSoup[i+3][c]
                count += puzzle_4_module.validateWord(word)

           #Find Dagonal R
           if i+3 < colLen and c+3 < lineLen:
                word=letterSoup[i][c]
                word += letterSoup[i+1][c+1]
                word += letterSoup[i+2][c+2]
                word += letterSoup[i+3][c+3]
                count += puzzle_4_module.validateWord(word)

           #Find Dagonal L
           if i+3 < colLen and c-3 >= 0:
                word=letterSoup[i][c]
                word += letterSoup[i+1][c-1]
                word += letterSoup[i+2][c-2]
                word += letterSoup[i+3][c-3]
                count += puzzle_4_module.validateWord(word)


print(count)