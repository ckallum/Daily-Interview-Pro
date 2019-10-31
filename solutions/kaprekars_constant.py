from copy import copy


def kaprekar_iterations(n):
    count = 0
    while n != 6174:
        n = sorted(str(n))
        n2 = list(reversed(copy(n)))
        if len(n2) < 4:
            n2 = n2 + ['0' for _ in range(4 - len(n2))]
        int_n = int("".join(n))
        int_n2 = int("".join(n2))
        n = int_n2-int_n
        count += 1
    return count


def main():
    assert kaprekar_iterations(123) == 3


if __name__ == '__main__':
    main()
