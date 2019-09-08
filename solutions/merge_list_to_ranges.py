def find_ranges(nums):
    start = nums[0]
    end = start
    arrow = "->"
    ranges = []
    for index, num in enumerate(nums[1:], start=1):
        if num != end + 1:
            if num == end:
                pass
            else:
                ranges.append(str(start) + arrow + str(end))
                start = num
                end = start
        else:
            end += 1
    ranges.append(str(start) + arrow + str(end))
    return ranges


def main():
    assert find_ranges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]) == ['0->2', '5->5', '7->11', '15->15']


if __name__ == '__main__':
    main()
