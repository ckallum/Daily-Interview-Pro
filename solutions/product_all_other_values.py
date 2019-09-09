from collections import deque


def get_values(numbers):
    temp = 1
    result_array = [1 for _ in numbers]
    # Each index has the accumulative product shifted one place to the right
    for index, number in enumerate(numbers):
        result_array[index] = temp
        temp *= number
    temp = 1
    # From right to left, the number at that index is missing progressively more values to be multiplied. Starting
    # from the last value in numbers.
    for index in range(len(numbers) - 1, -1, -1):
        result_array[index] *= temp
        temp *= numbers[index]

    return result_array


def get_values2(numbers):
    left_to_right = []
    right_to_left = deque()
    accumulative_product = 1
    for number in numbers:
        accumulative_product *= number
        left_to_right.append(accumulative_product)
    accumulative_product = 1
    for number in numbers[::-1]:
        accumulative_product *= number
        right_to_left.appendleft(accumulative_product)

    for index in range(len(numbers)):
        if 0 < index < len(numbers) - 1:
            numbers[index] = left_to_right[index - 1] * right_to_left[index + 1]
        elif index == 0:
            numbers[index] = right_to_left[1]
        else:
            numbers[index] = left_to_right[len(left_to_right) - 2]
    return numbers


def main():
    assert get_values([2, 3, 4, 1, 3, 4, 6, 7]) == [6048, 4032, 3024, 12096, 4032, 3024, 2016, 1728]
    assert get_values2([2, 3, 4, 1, 3, 4, 6, 7]) == [6048, 4032, 3024, 12096, 4032, 3024, 2016, 1728]


if __name__ == '__main__':
    main()
