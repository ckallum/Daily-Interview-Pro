def findCount(n, possibleSteps):

    stepsDict = dict()
    stepsDict[0] = 1
    if n < min(possibleSteps):
        return 0
    for x in range(1, n+1):
        stepsDict[x] = 0
        for step in possibleSteps:
            if x - step in stepsDict:
                stepsDict[x] += stepsDict[x-step]
    return stepsDict[n]


def main():
    assert findCount(4, [1, 2]) == 5
    assert findCount(5, [1, 2, 3]) == 13


if __name__ == '__main__':
    main()
