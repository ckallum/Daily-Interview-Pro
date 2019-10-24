from copy import copy


def reverse_num(temp):
    reverse = 0
    while temp > 0:
        reverse *= 10
        reverse += temp % 10
        temp //= 10
    return reverse


def is_palindrome(number):
    if abs(number) != number:
        number = abs(number)
    temp = copy(number)
    return reverse_num(temp) == number


def main():
    assert is_palindrome(1001001)
    assert is_palindrome(-100010001)
    assert not is_palindrome(1451)


if __name__ == '__main__':
    main()
