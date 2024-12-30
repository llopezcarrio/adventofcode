BUTTON_A_COST = 3
BUTTON_B_COST = 1
ADDVALUE = 0

def process_lines(lines, addValue):
    totalCost = 0

    global ADDVALUE
    ADDVALUE = addValue

    for i in range(0, len(lines), 4):
        ALine = lines[i]
        BLine = lines[i + 1]
        PLine = lines[i + 2]

        totalCost += process_line(ALine, BLine, PLine)

    return totalCost

def process_line(ALine, BLine, PLine):
    AVals = get_xy(ALine)
    BVals = get_xy(BLine)
    PVals = get_prize(PLine)

    a1, b1, c1 = AVals[0], BVals[0], PVals[0]
    a2, b2, c2 = AVals[1], BVals[1], PVals[1]

    # Calculate determinants using Cramer's Rule
    D = a1 * b2 - a2 * b1  # Main determinant
    Dx = c1 * b2 - c2 * b1  # Determinant for A
    Dy = a1 * c2 - a2 * c1  # Determinant for B

    if D == 0:
        return 0  # No unique solution

    # Solve for A and B
    A = Dx / D
    B = Dy / D

    # Check for integer solutions
    if not (A.is_integer() and B.is_integer()):
        return 0

    # Calculate total cost
    A, B = int(A), int(B)
    return A * BUTTON_A_COST + B * BUTTON_B_COST


def get_xy(line):
    parts = line.split(":")[1].strip().split(",")
    x = int(parts[0].split("+")[1].strip())
    y = int(parts[1].split("+")[1].strip())
    return x, y


def get_prize(line):
    parts = line.split(":")[1].strip().split(",")
    x = ADDVALUE + int(parts[0].split("=")[1].strip())
    y = ADDVALUE + int(parts[1].split("=")[1].strip())
    return x, y
