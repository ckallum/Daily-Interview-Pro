# Iterating over array to match values to condition->consider sorting first in these type of problems/reducing element
# Common middle algorithm

def findPythagoreanTriplets(nums):
    for index, val in enumerate(nums):
        nums[index] = val * val
    nums = list(sorted(set(nums)))
    for index, val in reversed(list(enumerate(nums))):
        left = 0
        right = index - 1
        while right > left:
            res = nums[right] + nums[left]
            if res == val:
                return True
            elif res < val:
                left += 1
            else:
                right -= 1

    return False


def main():
    inp = [3, 5, 12, 5, 13]
    inp2 = [3, 5, 5, 13]
    assert findPythagoreanTriplets(inp) == True
    assert findPythagoreanTriplets(inp2) == False


if __name__ == '__main__':
    main()
