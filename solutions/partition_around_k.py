def partition(nums, k):
    index = 0
    less_than_index = 0
    larger_than_index = len(nums) - 1
    while index <= larger_than_index:
        current = nums[index]
        if current < k:
            nums[less_than_index], nums[index] = nums[index], nums[less_than_index]
            less_than_index += 1
            index += 1
        if current > k:
            nums[larger_than_index], nums[index] = nums[index], nums[larger_than_index]
            larger_than_index -= 1
        if current == k:
            index += 1
    print(nums)
    return nums


def main():
    assert partition([2, 2, 2, 4, 2, 2, 5, 2, 5], 3) == [2, 2, 2, 2, 2, 2, 5, 5, 4]
    assert partition([2, 2, 2, 4, 2, 2, 5, 2, 3], 3) == [2, 2, 2, 2, 2, 2, 3, 5,4]


if __name__ == '__main__':
    main()
