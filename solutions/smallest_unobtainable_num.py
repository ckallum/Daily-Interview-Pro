def find_smallest(numbers):
    """
        We are starting with num as it's the first possible positive number to be returned,
        since the numbers are sorted in ascending order, we can find the smallest unobtainable number
        by simply adding all the numbers we have iterated over together until the total is smaller
        than the current number we are comparing to.
        - By continuously adding the current number to the result, we are essentially getting the
        largest possible obtainable number with the numbers we have already seen. Starting with 1 at the
        beginning automatically gives the biggest obtainable number +1 which is the smallest unobtainable
        number.

    """
    res = 1
    for num in numbers:
        if res < num:
            return res
        else:
            res += num
    return res


def main():
    assert find_smallest([1, 2, 3, 8, 9, 10]) == 7


if __name__ == '__main__':
    main()