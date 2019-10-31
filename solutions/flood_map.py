from collections import deque


def find_neighbours(row, col):
    return [(row - 1, col), (row + 1, col), (row - 1, col - 1), (row - 1, col + 1), (row, col - 1), (row, col + 1),
            (row + 1, col - 1), (row + 1, col + 1)]


def find_high_points(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] > 0:
                neighbours = [(r, c) for r, c in find_neighbours(row, col) if
                              0 <= r < len(grid) and 0 <= c < len(grid[0])]
                if all([grid[r][c] < grid[row][col] for r, c in neighbours]):
                    grid[row][col] = 101

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 101:
                grid[row][col] = 1
                neighbours = [(r, c) for r, c in find_neighbours(row, col) if
                              0 <= r < len(grid) and 0 <= c < len(grid[0])]
                for r, c in neighbours:
                    grid[r][c] = 0
            else:
                grid[row][col] = 0

    return grid



def find_plateau(grid):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            neighbours = [(r, c) for r, c in find_neighbours(row, col) if
                          0 <= r < len(grid) and 0 <= c < len(grid[0])]
            if not all([grid[r][c] <= grid[row][col] for r, c in neighbours]):
                grid[row][col] = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] != 0:
                grid[row][col] = 1
    return grid


def main():
    assert find_high_points([[1, 2, 1, 3, 4],
                             [1, 5, 2, 2, 2],
                             [4, 5, 1, 9, 7],
                             [3, 5, 3, 7, 6],
                             [4, 3, 1, 7, 3]]) == [[0, 0, 0, 0, 1],
                                                   [0, 0, 0, 0, 0],
                                                   [0, 0, 0, 1, 0],
                                                   [0, 0, 0, 0, 0],
                                                   [0, 0, 0, 0, 0]]

    assert find_plateau([[1, 2, 3, 4],
                         [5, 5, 5, 2],
                         [1, 1, 1, 1],
                         [0, 0, 0, 9]]) == [[0, 0, 0, 0],
                                            [1, 1, 1, 0],
                                            [0, 0, 0, 0],
                                            [0, 0, 0, 1]]


if __name__ == '__main__':
    main()
