def rotate_nd(nums, k):
    for i in range(k + 1):
        start = nums[0]
        for j in range(len(nums) - 1):
            nums[j] = nums[j + 1]
        nums[len(nums) - 1] = start
    return nums


def rotate_not_inplace(nums, k):
    return nums[-k:] + nums[:len(nums) - k]


def rotate_n(nums, k):
    def rotate(start, end):
        for i in range((end - start) // 2):
            nums[start + i], nums[end - 1 - i] = nums[end - 1 - i], nums[start + i]

    rotate(len(nums) - k, len(nums))
    rotate(0, len(nums) - k)
    rotate(0, len(nums))
    return nums


def main():
    ans = [5, 6, 7, 1, 2, 3, 4]
    assert rotate_nd([1, 2, 3, 4, 5, 6, 7], 3) == ans
    assert rotate_not_inplace([1, 2, 3, 4, 5, 6, 7], 3) == ans
    assert rotate_n([1, 2, 3, 4, 5, 6, 7], 3) == ans


if __name__ == '__main__':
    main()
