from math import inf
from collections import deque
"""
WINDOW PROBLEM
If the current subarray sum is negative and the next value is positive, then the current subarray is obsolete because
the next value will always be bigger than the current subarray. If the next value is negative then we have to 
start a new subarray as the next value will only make the subarray smaller which means we cannot improve on our 
current max /total of the current subarray(remember the subarray has to be contiguous). If later we find a bigger 
value to negate the negative sum of the current subarray then that value as a standalone subarray will have a higher
total than the current subarray therefore the current subarray is obsolete.

If the current subarray sum is positive then the as long as the next value doesn't bring the sum below 0 then 
there is still a possibility of a new value being added to make the sum larger than the current max in that 
current subarray. If the current subarray is positive then a new positive value by itself will always be smaller 
than the current subarray + the new positive value. 
"""

def findsum(numbers):

    maxsum = -inf
    currentsum = 0
    currentsub = deque()
    for num in numbers:
        currentsub.append(num)
        if currentsum != abs(currentsum):
            currentsum = num
            currentsub = deque([num])
        else:
            currentsum += num
            if currentsum > maxsum:
                maxsum = currentsum
    return maxsum


def main():
    assert findsum([35, -50, 42, 14, -5, 86]) == 137


if __name__ == '__main__':
    main()
