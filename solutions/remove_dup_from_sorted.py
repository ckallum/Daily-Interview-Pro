def remove_dups(nums):
    i = 0

    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    for _ in range(len(nums) - i - 1):
        nums.pop()
    return nums


def main():
    assert remove_dups([1, 1, 1, 1, 1, 1]) == [1]
    assert remove_dups([1, 1, 2, 3, 4, 4, 4, 4, 4, 5, 5, 6, 7, 9]) == [1, 2, 3, 4, 5, 6, 7, 9]


if __name__ == '__main__':
    main()
