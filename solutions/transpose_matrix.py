def transpose(mat):
    if len(mat) == 0:
        return []

    new_mat = [[0] * len(mat) for _ in range(len(mat[0]))]

    for x, row in enumerate(mat):
        for y, cell in enumerate(row):
            new_mat[y][x] = cell

    return new_mat


def main():
    assert transpose([[1, 2, 3],
                      [4, 5, 6]]) == [[1, 4],
                                      [2, 5],
                                      [3, 6]]


if __name__ == '__main__':
    main()
