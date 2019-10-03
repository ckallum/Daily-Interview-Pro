from copy import copy


def find_permutations(numbers, low, high):
    if low == high:
        return [numbers]
    result = []
    for i in range(low, high+1):
        temp = copy(numbers)
        temp[low], temp[i] = temp[i], temp[low]
        result.extend(find_permutations(temp, low + 1, high))

    return result


def main():
    assert find_permutations([1, 2, 3], 0, 2) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]


if __name__ == '__main__':
    main()
