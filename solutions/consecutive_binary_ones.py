def find_consecutive(number):
    count = 0
    max_count = 0
    prev = 0
    while number >= 1:
        mod = number % 2
        if prev == 1:
            count += mod
        else:
            count = mod
        prev = mod

        if count > max_count:
            max_count = count
        number //= 2
    return max_count


def main():
    assert find_consecutive(242) == 4


if __name__ == '__main__':
    main()
