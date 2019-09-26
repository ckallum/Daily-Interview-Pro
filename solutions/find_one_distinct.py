def find_single_num(numbers):
    result = 0
    for i in range(32):
        sum_at_bit_i = 0
        x = 1 << i
        for number in numbers:
            if number & x:
                sum_at_bit_i += 1

        if sum_at_bit_i % 2:
            result = result | x
    return result


def main():
    assert find_single_num([8, 8, 2, 3, 4, 4, 2, 3, 1, 1, 5, 9, 9]) == 5


if __name__ == '__main__':
    main()
