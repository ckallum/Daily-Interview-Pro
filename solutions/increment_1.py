def increment_one(numbers):
    for index, number in reversed(list(enumerate(numbers))):
        if number != 9:
            numbers[index] += 1
            break
        elif index == 0 and number == 9:
            numbers[0] = 1
            numbers.append(0)
            break
        else:
            numbers[index] = 0

    return numbers


def main():
    assert increment_one([2, 9, 9]) == [3, 0, 0]
    assert increment_one([9, 9, 9]) == [1, 0, 0, 0]


if __name__ == '__main__':
    main()
