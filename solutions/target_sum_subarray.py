def find_subarray(numbers, k):
    if k in numbers:
        return [k]
    numbers_dict = {number: [] for number in range(k + 1)}
    for index, number in enumerate(numbers):
        if number <= k and not numbers_dict[number]:
            numbers_dict[number].append((index, number))

    for i in range(k + 1):
        for index, number in enumerate(numbers):
            if number <= i and numbers_dict[i - number]:
                if (index, number) not in numbers_dict[i - number]:
                    numbers_dict[i] = numbers_dict[i - number] + [(index, number)]

    print(numbers_dict)

    return [x[1] for x in numbers_dict[k]]


def main():
    assert find_subarray([1, 3, 2, 5, 7, 2], 14) == [2, 5, 7]


if __name__ == '__main__':
    main()
