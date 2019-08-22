def spiral(grid):
    x, y = 0, 0
    result = list()
    right = True
    down = False
    left = False
    up = False
    while True:
        result.append(grid[y][x])
        grid[y][x] = False
        if right:
            if x + 1 < len(grid[0]) and grid[y][x + 1] is not False:
                x += 1
            elif y + 1 < len(grid[0]) and grid[y + 1][x] is not False:
                right = False
                down = True
                y += 1
            else:
                break
        elif down:
            if y + 1 < len(grid) and grid[y + 1][x] is not False:
                y += 1
            elif x - 1 >= 0 and grid[y][x - 1] is not False:
                down = False
                left = True
                x -= 1
            else:
                break
        elif left:
            if x - 1 >= 0 and grid[y][x - 1] is not False:
                x -= 1
            elif y - 1 >= 0 and grid[y-1][x] is not False:
                left = False
                up = True
                y -= 1
            else:
                break
        elif up:
            if y - 1 >= 0 and grid[y-1][x] is not False:
                y -= 1
            elif x + 1 < len(grid[0]) and grid[y][x+1] is not False:
                up = False
                right = True
                x += 1
            else:
                break

    return result


def main():
    grid = [[1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20]]
    assert spiral(grid) == [1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12]


if __name__ == '__main__':
    main()
