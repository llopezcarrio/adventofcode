import collections
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "map.txt")


map = []

f = open(file_path, "r")
for line in f:
    map.append(line.rstrip('\n'))
f.close()

def find_paths_recursive(grid, current_path=[(0,2)], solutions=[]):
    n = len(grid)
    dirs = [(-1,0), (1,0), (0,1), (0,-1)]

    last_cell = current_path[-1]

    for x,y in dirs:
        new_i = last_cell[0] + x
        new_j = last_cell[1] + y

        # Check if new cell is in grid
        if new_i<0 or new_i>=n or new_j<0 or new_j>=n:
            continue

        # Check if new cell has bigger value than last
        if int(grid[new_i][new_j]) - int(grid[last_cell[0]][last_cell[1]]) != 1:
            continue

        # Check if new cell is already in path
        if (new_i, new_j) in current_path:
            continue

        # Add cell to current path
        current_path_copy = current_path.copy()
        current_path_copy.append((new_i, new_j))

        if int(grid[new_i][new_j]) == 9 and len(current_path_copy) == 10:
            solutions.append((new_i, new_j))

        # Create new current_path array for every direction
        find_paths_recursive(grid, current_path_copy, solutions)

    return solutions

#def compute_cell_values(grid1, solutions):
#    path_values = []
#
#    for solution in solutions:
#        solution_values = []
#        for cell in solution:
#            solution_values.append(grid1[cell[0]][cell[1]])
#        path_values.append(solution_values)
#    return path_values

countSolutions = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == '0':
           solutions = find_paths_recursive(map, [(i,j)], [])
           countSolutions += len(solutions)

#path_values = compute_cell_values(map, solutions)

print('Solutions:')
print(solutions)
#print('Values:')
#print(path_values)
print('Count Solutions:')
print(countSolutions)