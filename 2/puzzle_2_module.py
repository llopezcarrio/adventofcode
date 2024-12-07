def validateSafeReport(levelA, levelB):

    badIncreaseDecrease = False
    pattern = ""

    differ = levelA - levelB

    if not(abs(differ) in range(1, 4)):
       badIncreaseDecrease = True

    elif (differ > 0 and not badIncreaseDecrease):
       pattern = "decrease"

    elif (differ < 0 and not badIncreaseDecrease):
        pattern = "increase"

    return badIncreaseDecrease, pattern
