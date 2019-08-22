def nonDecreasing(nums):
    changes = 0
    for index, x in enumerate(nums[:-1]):
        if x > nums[index + 1]:
            changes += 1

    if changes == 1:
        return True
    return False


def main():
    nums = [13, 4, 7]
    assert nonDecreasing(nums) == True
    assert nonDecreasing([13, 4, 1]) == False


if __name__ == '__main__':
    main()
