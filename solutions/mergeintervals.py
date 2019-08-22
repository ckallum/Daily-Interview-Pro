"""
    You are given an array of intervals - that is, an array of tuples (start, end).
    The array may not be sorted, and could contain overlapping intervals.
    Return another array where the overlapping intervals are merged.

For example:
[(1, 3), (5, 8), (4, 10), (20, 25)]

This input should return [(1, 3), (4, 10), (20, 25)] since (5, 8) and (4, 10)
can be merged into (4, 10).

Here's a starting point:

def merge(intervals):
  # Fill this in.

print merge([(1, 3), (5, 8), (4, 10), (20, 25)])
# [(1, 3), (4, 10), (20, 25)]

"""
from math import inf


def merge_intervals(intervals):
    result = list()
    result.append(intervals[0])
    for start, end in intervals[1:]:
        index = 0
        resIndex = 1
        popped = False
        while index < len(result) and result:
            min, max = result[index]
            if start < min and end > max:
                result.pop(index)
                index -= 1
            elif start > min and end < max:
                popped = True
            elif end < max:
                resIndex -= 1
            else:
                resIndex += 1
            index += 1
        if not popped:
            result.insert(resIndex, (start, end))
        print(result)
    return result


def main():
    assert merge_intervals([(1, 3), (5, 8), (6, 9), (4, 10), (20, 25)]) == [(1, 3), (4, 10), (20, 25)]
    assert merge_intervals([(1, 3), (5, 8), (4, 10), (6, 9), (20, 25)]) == [(1, 3), (4, 10), (20, 25)]


if __name__ == '__main__':
    main()
