def find_single_num(numbers):
    result = 0
    for i in range(32):
        sum_at_bit_i = 0
        x = 1 << i
        for number in numbers:
            if number & x:
                sum_at_bit_i += 1

        """
            If there is an extra one at the end of ANDing all the numbers at that bit
            then we know that the distinct number also has a one at that bit, and therefore
            allows us to continue building the 32 bit number.
        """
        if sum_at_bit_i % 2:
            result = result | x
    return result


def main():
    assert find_single_num([8, 8, 2, 3, 4, 4, 2, 3, 1, 1, 5, 9, 9]) == 5


if __name__ == '__main__':
    main()
