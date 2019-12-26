def larger_number(nums):
    results = [-1]*len(nums)
    numbers_left = [0]
    for i, n in enumerate(nums):
        while numbers_left and n > nums[numbers_left[-1]]:
            index = numbers_left.pop()
            results[index] = i
        numbers_left.append(i)
    return results


def main():
    assert larger_number([3, 2, 5, 6, 9, 8]) == [2, 2, 3, 4, -1, -1]


if __name__ == '__main__':
    main()