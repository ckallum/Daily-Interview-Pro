from cmath import inf


def find_min(n):
    square_set = set()
    for i in range(1, int(n ** (0.5)) + 1):
        square_set.add(i ** 2)
    square_dict = [inf] * (n + 1)
    square_dict[0] = 0
    for square in square_set:
        for i in range(square, n+1):
            square_dict[i] = min(square_dict[i], 1 + square_dict[i - square])
    return square_dict[n]


def main():
    assert find_min(13) == 2
    assert find_min(1) == 1


if __name__ == '__main__':
    main()
