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
                    grid[row][col] = 1
                    for r, c in neighbours:
                        grid[r][c] = 0

    print(grid)
    return grid


def flood_cells(grid, high_points, row, col):
    level = grid[row][col]
    queue = [(row, col)]
    while queue:
        row, col = queue.pop()
        high_points[row][col] = level
        for i, j in [(r, c) for r, c in find_neighbours(row, col) if
                     0 <= r < len(grid) and 0 <= c < len(grid[0])]:
            if high_points[i][j] == 0 or (high_points[i][j] == 1 and grid[i][j] <= level):
                queue.append((i, j))

    print(high_points)
    return high_points


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
    assert find_high_points([[1, 4, 3, 4],
                             [3, 2, 3, 1],
                             [5, 3, 5, 1],
                             [4, 2, 3, 3]]) == [[0, 1, 0, 1],
                                                [0, 0, 0, 0],
                                                [1, 0, 1, 0],
                                                [0, 0, 0, 0]]

    assert flood_cells([[1, 4, 3, 4],
                        [3, 2, 3, 1],
                        [5, 3, 5, 1],
                        [4, 2, 3, 3]], [[0, 1, 0, 1],
                                        [0, 0, 0, 0],
                                        [1, 0, 1, 0],
                                        [0, 0, 0, 0]], 0, 1) == [[4, 4, 4, 4],
                                                                 [4, 4, 4, 4],
                                                                 [1, 4, 1, 4],
                                                                 [4, 4, 4, 4]]
    assert find_plateau([[1, 2, 3, 4],
                         [5, 5, 5, 2],
                         [1, 1, 1, 1],
                         [0, 0, 0, 9]]) == [[0, 0, 0, 0],
                                            [1, 1, 1, 0],
                                            [0, 0, 0, 0],
                                            [0, 0, 0, 1]]


if __name__ == '__main__':
    main()
