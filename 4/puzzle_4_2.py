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

        if word == "M" or word == "S":
           if c+2 < lineLen and i+2 < colLen:
                if letterSoup[i+1][c+1] == "A":
                   word += letterSoup[i+1][c+1]
                   word += letterSoup[i+2][c+2]

                   if puzzle_4_module.validateWord2(word) == 1:
                      word = letterSoup[i][c+2]
                      word += letterSoup[i+1][c+1]
                      word += letterSoup[i+2][c]
                      count += puzzle_4_module.validateWord2(word)

print(count)