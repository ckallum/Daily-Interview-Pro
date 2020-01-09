def transpose(matrix):
    rows = len(matrix[0])
    columns = len(matrix)
    new_mat = [[0] * columns] * rows
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j])
            new_mat[j][i] = matrix[i][j]
            print(new_mat)
    print(new_mat)
    return new_mat


def main():
    assert transpose([[1, 2, 3],
                      [4, 5, 6]]) == [[1, 4],
                                      [2, 5],
                                      [3, 6]]


if __name__ == '__main__':
    main()
