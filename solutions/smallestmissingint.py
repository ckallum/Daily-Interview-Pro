def first_missing_number(nums):
    result = 1
    numdict = dict()
    for value in nums:
        if value > 1:
            numdict[value] = True
        if value == result:
            result += 1
    while result in numdict:
        result += 1
    return result


def main():
    assert first_missing_number([3, 4, -1, 1]) == 2
    assert first_missing_number([1, 2, 0]) == 3
    assert first_missing_number([1, 2, 5]) == 3
    assert first_missing_number([1]) == 2
    assert first_missing_number([-1, -2]) == 1


if __name__ == '__main__':
    main()
