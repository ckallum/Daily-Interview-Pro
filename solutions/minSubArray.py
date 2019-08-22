from collections import deque
from math import inf


def solution(array, k):
    minlen = inf
    currentsub = deque()
    runningTotal = 0
    for value in array:
        currentsub.append(value)
        runningTotal += value
        if runningTotal >= k:
            while runningTotal >= k:
                if len(currentsub) < minlen:
                    minlen = len(currentsub)
                runningTotal -= currentsub.popleft()
    return minlen


def main():
    nums = [2, 3, 1, 2, 4, 3]
    assert solution(nums, 7) == 2


if __name__ == '__main__':
    main()
