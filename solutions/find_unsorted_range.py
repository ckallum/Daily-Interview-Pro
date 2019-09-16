from cmath import inf


def find_range(nums):
    start_index = 0
    end_index = 0
    current_max = -inf
    needs_sorted = False
    for index, number in enumerate(nums):
        if not needs_sorted and number >= nums[start_index]:
            start_index = index
        if number >= current_max:
            current_max = number
        else:
            end_index = index
            needs_sorted = True

    return start_index, end_index


def main():
    assert find_range([1, 7, 5, 9, 7, 8, 10]) == (1, 5)


if __name__ == '__main__':
    main()
