import puzzle_1_module

listLocationsA, listLocationsB = puzzle_1_module.get_location_lists("input.txt")

listLocationsA.sort()
listLocationsB.sort()

distance = 0

for i in range(len(listLocationsA)):
  distance += abs(listLocationsA[i] - listLocationsB[i])

print(distance)