def traversals(m, n):
    grid = [[0 for _ in range(n+1)] for _ in range(m+1)]
    grid[0][0] = 1
    for i in range(m+1):
        for j in range(n+1):
            if i != 0 or j != 0:
                if i == 0:
                    grid[i][j] = grid[i][j - 1]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j]
                else:
                    grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
    return grid[m][n]


def main():
    assert traversals(2, 2) == 6


if __name__ == '__main__':
    main()
