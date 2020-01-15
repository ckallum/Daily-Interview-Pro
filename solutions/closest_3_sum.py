from cmath import inf


def three_sum(nums, target):
    closest = inf
    nums.sort()
    result = []
    for i in range(len(nums) - 2):
        j = i + 1
        k = len(nums) - 1
        while j < k:
            current = nums[i] + nums[j] + nums[k]
            if abs(target - current) < closest:
                closest = abs(target - current)
                result = [nums[i], nums[j], nums[k]]
            if current > target:
                k -= 1
            else:
                j += 1
    print(result)
    return result


def main():
    assert three_sum([2, 1, -5, 4], -1) == [-5, 1, 4]


if __name__ == '__main__':
    main()
