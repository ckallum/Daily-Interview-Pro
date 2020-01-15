def pascals(n):
    triangle = [[1] * i for i in range(1, n + 1)]
    for i in range(n):
        for j in range(1, i):
            triangle[i][j] = triangle[i-1][j]+triangle[i-1][j-1]
    return triangle[-1]


def main():
    assert pascals(6) == [1,5,10,10,5,1]


if __name__ == '__main__':
    main()
