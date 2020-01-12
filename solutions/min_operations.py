def min_operations(x, y):
    count = 0
    while y != x:

        if not y % 2:
            y /= 2
        else:
            y += 1
        count += 1
    return count


def main():
    assert min_operations(6, 20) == 3


if __name__ == '__main__':
    main()