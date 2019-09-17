def reverse(x):
    if x >= 2 ** 31 or x < -(2 ** 31):
        return 0

    is_neg = False
    if abs(x) != x:
        is_neg = True
        x = abs(x)
    result = 0
    while x >= 1:
        result = result * 10 + x % 10
        x = x // 10
    return -result if is_neg else result


def main():
    assert reverse(123) == 321
    assert reverse(2**31) == 0
    assert reverse(-123) == -321


if __name__ == '__main__':
    main()
