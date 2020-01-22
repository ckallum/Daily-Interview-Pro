def reshape_matrix(mat, x, y):
    number_of_elements = len(mat) * len(mat[0])
    if x * y != number_of_elements:
        return None
    result = [[None for _ in range(x)] for _ in range(y)]
    current_row = 0
    current_col = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if current_col == x:
                current_col = 0
                current_row += 1
            result[current_row][current_col] = mat[i][j]
            print(result)
            current_col += 1

    print(result)
    return result


def main():
    assert reshape_matrix([[1, 2], [3, 4]], 1, 4) == [[1], [2], [3], [4]]

    assert not reshape_matrix([[1, 2], [3, 4]], 2, 3)


if __name__ == '__main__':
    main()
