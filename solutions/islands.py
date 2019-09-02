def is_valid(grid, r, c):
    rows, cols = len(grid), len(grid[0])
    if r < 0 or c < 0 or r >= rows or c >= cols:
        return False
    return True


def count_islands(grid):
    count = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1:
                count += 1
                linked_points = [point for point in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)] if
                                 is_valid(grid, point[0], point[1])]
                for point in linked_points:
                    if grid[point[0]][point[1]] == 1:
                        grid[point[0]][point[1]] = 2
                    elif grid[point[0]][point[1]] == 2:
                        count -= 1

                print(grid[0], '\n', grid[1], '\n', grid[2], '\n', grid[3], '\n')
    return count


def main():
    assert count_islands([[1, 1, 0, 0, 0],
                          [0, 1, 0, 0, 1],
                          [1, 0, 0, 1, 1],
                          [0, 0, 0, 0, 0]]) == 3


if __name__ == '__main__':
    main()
