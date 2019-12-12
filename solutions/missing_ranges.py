def missing_ranges(nums, low, high):
    results = []
    for index, num in enumerate(nums):
        if index + 1 < len(nums):
            if nums[index] != nums[index + 1] - 1:
                if nums[index + 1] - 1 < high:
                    results.append((num + 1, nums[index + 1] - 1))
                else:
                    results.append((num + 1, high - 1))

    return results


def main():
    assert (missing_ranges([1, 3, 5, 10], 1, 10)) == [(2, 2), (4, 4), (6, 9)]
    assert (missing_ranges([1, 3, 5, 10], 1, 7)) == [(2, 2), (4, 4), (6, 6)]


if __name__ == '__main__':
    main()
