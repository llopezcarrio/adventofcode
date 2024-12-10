import puzzle_3_module
import os
import re

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input1.txt")

f = open(file_path, "r")


regex = r"don\'t\(\)|do\(\)"

text = f.read()
#text = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

matches = re.finditer(regex, text)

totalResults = 0
nextMatches = True

match = next(matches, -1)
start = 0
previousMatch = match.group()

while nextMatches:

    if match == -1:
        if previousMatch == "do()":
            totalResults += puzzle_3_module.calculateResults(text[start:])
            print(text[start:])
        nextMatches = False
    else:
        if start == 0:
           totalResults += puzzle_3_module.calculateResults(text[0:int(match.start())])
           print(text[0:int(match.start())])
        else:
            if previousMatch == "do()":
               totalResults += puzzle_3_module.calculateResults(text[start:int(match.start())])
               print(text[start:int(match.start())])


        previousMatch= match.group()
        start = int(match.end())
        match = next(matches, -1)
        print(totalResults)

print(totalResults)

f.close()