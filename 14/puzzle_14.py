import os
import puzzle_14_module

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "input.txt")

w = 101
h = 103
s =100

quadrants = [0,0,0,0]

f = open(file_path, "r")
for line in f:
    p=line.strip().split(" ")[0]
    pw=int(p.split("=")[1].split(",")[0])
    pt=int(p.split("=")[1].split(",")[1])
    v=line.strip().split(" ")[1]
    vr=int(v.split("=")[1].split(",")[0])
    vd=int(v.split("=")[1].split(",")[1])

    x,y = puzzle_14_module.move_robot(pw,pt,vr,vd,w,h,s)
    quadrant = puzzle_14_module.get_quadrant(x,y,w,h)
    if quadrant != 0:
        quadrants[quadrant-1] +=1

total=1
for i in range(len(quadrants)):
    if quadrants[i] != 0:
        total *= quadrants[i]

print(total)