def longest_sequence(numbers):
    numbers_set = set(numbers)
    max_sequence = 0
    for number in numbers_set:
        if number - 1 not in numbers_set:
            current = number
            length = 0
            while current in numbers_set:
                current += 1
                length += 1
            max_sequence = max(max_sequence, length)

    return max_sequence


def main():
    assert longest_sequence([100, 10, 200, 2, 3, 4, 1]) == 4


if __name__ == '__main__':
    main()
