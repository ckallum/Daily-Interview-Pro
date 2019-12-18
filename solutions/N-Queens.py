def is_valid(board, row):
    if row in board:
        return False

    column = len(board)
    for occupied_column, occupied_row in enumerate(board):
        if abs(occupied_row - row) == abs(occupied_column - column):
            return False

    return True


def n_queens(n, board=[]):
    if n == len(board):
        return board

    for row in range(n):
        if is_valid(board, row):
            res = n_queens(n, board + [row])
            if res:
                return res

    return None


def main():
    res = n_queens(5)
    result = []
    for row, col in enumerate(res):
        result.append((row,col))
    assert result == [(0, 0), (1, 2), (2, 4), (3, 1), (4, 3)]


# Q . . . .
# . . . Q .
# . Q . . .
# . . . . Q
# . . Q . .

if __name__ == '__main__':
    main()
