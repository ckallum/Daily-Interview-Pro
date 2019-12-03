def sort_squares(nums):
    negatives = []
    result = []
    for num in nums:
        if num < 0:
            negatives.append(num)
            continue
        while negatives and num >= -negatives[-1]:
            result.append(negatives.pop()**2)
        result.append(num**2)
    print(result)
    return result


def main():
    assert sort_squares([-5, -3, -1, 0, 1, 4, 5]) == [0, 1, 1, 9, 16, 25, 25]


if __name__ == '__main__':
    main()
