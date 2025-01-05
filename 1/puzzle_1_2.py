import puzzle_1_module

listLocationsA, listLocationsB = puzzle_1_module.get_location_lists("input.txt")

similarityScore = 0

for i in range(len(listLocationsA)):
  countLocation = listLocationsB.count(listLocationsA[i])
  similarityScore += listLocationsA[i] * countLocation

print(similarityScore)