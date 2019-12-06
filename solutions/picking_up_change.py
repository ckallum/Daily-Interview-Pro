def max_change(mat):
    m = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
    m[0][0] = mat[0][0]
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if row != 0:
                m[row][col] = max(m[row][col], m[row-1][col]+mat[row][col])
            if col != 0:
                m[row][col] = max(m[row][col], m[row][col-1]+mat[row][col])
    return m[-1][-1]


def main():
    mat = [
        [0, 3, 0, 2],
        [1, 2, 3, 3],
        [6, 0, 3, 2]
    ]

    assert max_change(mat) == 13


if __name__ == '__main__':
    main()
