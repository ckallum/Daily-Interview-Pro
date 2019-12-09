def rotate(mat):
    for i in range((len(mat)+1)//2):
        for j in range(i, len(mat) - i-1):
            mat[i][j], mat[-i-1][-j-1], mat[j][-i-1], mat[-j-1][i] = mat[-j-1][i], mat[j][-i-1], mat[i][j], mat[-i-1][-j-1]
    print(mat)
    return mat


# Fill this in.

def main():
    mat = [[5, 9, 5, 4], [1, 2, 3, 3], [4, 5, 6, 2], [7, 8, 9, 1]]

    # Looks like
    # 5 9 5 4
    # 1 2 3 3
    # 4 5 6 2
    # 7 8 9 1

    # Looks like
    # 7 4 1 5
    # 8 5 2 9
    # 9 6 3 5
    # 1 2 3 4
    assert (rotate(mat)) == [[7, 4, 1, 5], [8, 5, 2, 9], [9, 6, 3, 5], [1, 2, 3, 4]]


if __name__ == '__main__':
    main()
