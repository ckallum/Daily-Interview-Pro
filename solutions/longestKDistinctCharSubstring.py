from collections import deque


def find(sequence, uniquenums):
    currentsequence = deque()
    currentmax = 0
    valueDict = dict()
    for x in sequence:
        valueDict[x] = 0
    for x in sequence:
        currentsequence.append(x)
        valueDict[x] += 1
        while notValid(valueDict, uniquenums):
            val = currentsequence.popleft()
            valueDict[val] -= 1
        if len(currentsequence) > currentmax:
            currentmax = len(currentsequence)
    return currentmax


def notValid(diction, uniquenums):
    count = 0
    for x in diction:
        if diction[x] > 0:
            count += 1
            if count > uniquenums:
                return True
    return False


def main():
    assert find([1, 3, 5, 3, 1, 3, 1, 5], 2) == 4


if __name__ == '__main__':
    main()
