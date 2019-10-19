from string import ascii_uppercase


def convert(number):
    alphabet_dict = {number: ascii_uppercase[number - 1] for number in range(0, 26)}
    result = ''
    while number >= 1:
        res = (number % 26)
        result = alphabet_dict[res] + result
        if res == 0:
            number -= 1
        number //= 26
    return result


def main():
    # assert convert(26) == 'Z'
    # assert convert(51) == 'AY'
    assert convert(52) == 'AZ'
    assert convert(676) == 'YZ'
    assert convert(702) == 'ZZ'
    assert convert(704) == 'AAB'


if __name__ == '__main__':
    main()
