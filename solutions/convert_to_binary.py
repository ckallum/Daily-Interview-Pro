def base_2(n):
    result = 0
    while n > 0:
        remainder = n % 2
        result = result * 10 + remainder
        n = (n - remainder) / 2
    new_result = 0
    while result > 0:
        new_result = new_result * 10 + (result % 10)
        result //= 10
    print(new_result)
    return int(new_result)


def main():
    assert (base_2(123)) == 1111011


if __name__ == '__main__':
    main()
