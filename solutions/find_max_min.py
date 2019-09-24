def find_min_max(nums, low, high):
    if low == high:
        return nums[low], nums[high]
    if high == low + 1:
        return (nums[low], nums[high]) if nums[low] < nums[high] else (nums[high], nums[low])

    mid = (low + high) // 2
    left = find_min_max(nums, low, mid)
    right = find_min_max(nums, mid + 1, high)

    res = []
    res.append(left[0]) if left[0] < right[0] else res.append(right[0])
    res.append(left[1]) if left[1] > right[1] else res.append(right[1])
    return res


def main():
    nums = [3, 5, 1, 2, 4, 8]
    assert find_min_max(nums, 0, len(nums) - 1) == [1, 8]


if __name__ == '__main__':
    main()
