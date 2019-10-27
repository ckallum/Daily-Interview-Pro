def find_max(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            left, above = 0, 0
            if 0 <= row - 1:
                above = matrix[row - 1][col]
            if 0 <= col - 1:
                left = matrix[row][col - 1]
            matrix[row][col] += max(above, left)
    print(matrix[2][3])
    return matrix[len(matrix)-1][len(matrix[0])-1]


def main():
    assert find_max([[0, 3, 1, 1],
                     [2, 0, 0, 4],
                     [1, 5, 3, 1]]) == 12


if __name__ == '__main__':
    main()
