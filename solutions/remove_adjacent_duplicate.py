def remove(nums):
    while True:
        i = 0
        found = False
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                found = True
                nums = nums[:i] + nums[i + 2:]
            i += 1
        if not found:
            break
    print(nums)
    return nums


def main():
    assert remove("cabba") == "c"


if __name__ == '__main__':
    main()
