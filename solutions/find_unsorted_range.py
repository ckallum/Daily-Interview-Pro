from cmath import inf


def find_range(nums):
    start_index = -1
    end_index = -1
    current_max = -inf
    needs_sorted = False
    for index, number in enumerate(nums):
        if number >= current_max:
            current_max = number
        else:
            end_index = index
            if not needs_sorted:
                start_index = 0
                while number > nums[start_index]:
                    start_index += 1
                needs_sorted = True

    print(start_index, end_index)
    return start_index, end_index


def main():
    assert find_range([1, 7, 5, 9, 7, 8, 10]) == (1, 5)
    assert find_range([1, 2, 3, 4, 5, 6, 1]) == (0, 6)
    assert find_range([1, 2, 3, 4, 5]) == (-1, -1)


if __name__ == '__main__':
    main()
