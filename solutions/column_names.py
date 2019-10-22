from string import ascii_uppercase


def column_name(column):
    result = ""
    numbers = {number: ascii_uppercase[number-1] for number in range(0, 26)}
    while column >= 1:
        res = column % 26
        result = numbers[res] + result
        if res == 0:
            column -= 1
        column //= 26
    return result


def main():
    assert column_name(26) == 'Z'
    assert column_name(27) == 'AA'
    assert column_name(28) == 'AB'


if __name__ == '__main__':
    main()
