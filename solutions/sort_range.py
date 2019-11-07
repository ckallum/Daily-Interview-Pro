from cmath import inf


def find_range_n_squared(numbers):
    max_value = -inf
    lower = inf
    upper = -1
    for index, num in enumerate(numbers):
        if num > max_value:
            max_value = num
        if num < max_value:
            upper = index
            for j, num2 in enumerate(numbers[:index]):
                if num2 > num and j < lower:
                    lower = j
                    break
    print(lower, upper)
    return lower, upper


def find_range(numbers):
    max_value = -inf
    min_value = inf
    upper = -1
    lower = -1
    for index, num in enumerate(numbers):
        if num > max_value:
            max_value = num
        if num < max_value:
            upper = index

    for index, num in reversed(list(enumerate(numbers))):
        if num < min_value:
            min_value = num
        if num > min_value:
            lower = index
    print(lower, upper)
    return lower, upper


def main():
    assert find_range([2, 4, 7, 5, 6, 8]) == (2, 4)
    assert find_range([2, 4, 7, 5, 6, 1]) == (0, 5)
    assert find_range_n_squared([2, 4, 7, 5, 6, 8]) == (2, 4)
    assert find_range_n_squared([2, 4, 7, 5, 6, 1]) == (0, 5)


if __name__ == '__main__':
    main()
