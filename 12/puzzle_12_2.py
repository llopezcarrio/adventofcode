import collections
import os
import copy

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "map.txt")


map = []

f = open(file_path, "r")
i = 0
for line in f:
    row = []
    for j in range(len(line.rstrip('\n'))):
        row.append(line.rstrip('\n')[j])
    i += 1
    map.append(row)
f.close()

grid = copy.deepcopy(map)

def get_perimeter(row,col):
    perimeter = 0
    if col+1 < len(grid[row]):
       if grid[row][col] != grid[row][col+1]:
           perimeter += 1
    else:
        perimeter += 1

    if col-1 >= 0:
       if grid[row][col] != grid[row][col-1]:
           perimeter += 1
    else:
        perimeter += 1

    if row+1 < len(grid):
       if grid[row][col] != grid[row+1][col]:
            perimeter += 1
    else:
        perimeter += 1

    if row-1 >= 0:
       if grid[row][col] != grid[row-1][col]:
          perimeter += 1
    else:
       perimeter += 1

    return perimeter


def is_inbounds(grid, row, col, search):
        return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == search

def bfs(row, col, grid,region, search):
    area = 1
    sides =0

    region =[]
    q = collections.deque()
    q.append((row, col))
    if get_top_left_corner(row, col):
        sides += 2
    if get_top_right_corner(row, col):
        sides += 2
    if get_top_inside_left_corner(row, col):
        sides += 2
    if get_top_inside_right_corner(row, col):
        sides += 2
    grid[row][col] = "0"



    region.append((row, col))

    while q:
        # visit the node
        row, col = q.popleft()

        for new_row, new_col in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]:
            if is_inbounds(grid, new_row, new_col, search):
               if get_top_left_corner(new_row, new_col):
                    sides += 2
               if get_top_right_corner(new_row, new_col):
                    sides += 2
               if get_top_inside_left_corner(new_row, new_col):
                    sides += 2
               if get_top_inside_right_corner(new_row, new_col):
                    sides += 2
               grid[new_row][new_col] = "0"
               area += 1

               q.append((new_row, new_col))


    return area, sides

count = 0
num_rows = len(map)
num_cols = len(map[0])

def get_top_left_corner(row, col):
    #top left corner

    if col-1 >= 0:
       if grid[row][col-1] == grid[row][col]:
          return False

    if row-1 >= 0:
       if grid[row-1][col] == grid[row][col]:
          return False

    return True

def get_top_right_corner(row, col):
    #top right corner

    if col+1 < len(map[0]):
       if grid[row][col+1] == grid[row][col]:
          return False

    if row-1 >= 0:
       if grid[row-1][col] == grid[row][col]:
          return False

    return True

def get_top_inside_right_corner(row, col):
    #top inside right corner

    if col-1 >=0:
       if grid[row][col-1] != grid[row][col]:
          return False
    else:
        return False

    if row+1 < len(map):
       if grid[row+1][col] != grid[row][col]:
          return False
    else:
        return False

    if row+1 < len(map) and col-1 >=0:
       if grid[row+1][col-1] == grid[row][col]:
          return False
    else:
        return False

    return True

def get_top_inside_left_corner(row, col):
    #top inside left corner

    if col+1 < len(map[0]):
       if grid[row][col+1] != grid[row][col]:
          return False
    else:
        return False

    if row+1 < len(map):
       if grid[row+1][col] != grid[row][col]:
          return False
    else:
        return False

    if row+1 < len(map) and col+1 < len(map[0]):
       if grid[row+1][col+1] == grid[row][col]:
          return False
    else:
        return False

    return True


fencePrices = 0
for row in range(0, num_rows):
    for col in range(0, num_cols):
        if map[row][col] != "0":
           count += 1
           area, sides = bfs(int(row), int(col), map, row+col, map[row][col])
           fencePrices += (area * sides)


print(fencePrices)