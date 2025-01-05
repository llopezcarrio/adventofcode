import puzzle_3_module
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

f = open(file_path, "r")

text = f.read()
#text = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"

totalResults = puzzle_3_module.calculateResults(text)

print(totalResults)

f.close()