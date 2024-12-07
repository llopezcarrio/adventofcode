import os

def get_location_lists(fileName):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, fileName)

    f = open(fileName, "r")
    listLocationsA = []
    listLocationsB = []

    for line in f:
        locations = line.split('   ')
        listLocationsA.append(int(locations[0]))
        listLocationsB.append(int(locations[1]))

    f.close()

    return listLocationsA, listLocationsB
