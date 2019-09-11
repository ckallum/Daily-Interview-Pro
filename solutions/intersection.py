def intersection(nums1, nums2):
    intersection_arr = []
    for num in nums1:
        if num in nums2 and num not in intersection_arr:
            intersection_arr.append(num)
    return intersection_arr


def main():
    assert intersection([1, 2, 2, 1], [2, 2]) == [2]
    assert intersection([9, 4, 2, 4, 4, 2, 1, 1, 2], [4, 4, 2, 0]) == [4, 2]


if __name__ == '__main__':
    main()
