def validate(board):
    if len(board) != 9:
        return False
    for r in board:
        if len(r) != 9:
            return False
        seen = [False] * 10
        for col in r:
            if col != ' ':
                if seen[col]:
                    return False
                else:
                    seen[col] = True

    for col in range(len(board[0])):
        seen = [False] * 10
        for r in range(len(board)):
            if board[r][col] != " ":
                if seen[board[r][col]]:
                    return False
                else:
                    seen[board[r][col]] = True
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            seen = [False] * 10
            for r in range(3):
                for c in range(3):
                    if board[row + r][col + c] != ' ':
                        if seen[board[row + r][col + c]]:
                            return False
                        else:
                            seen[board[row + r][col + c]] = True
    return True


def main():
    assert validate(board=[
        [5, ' ', 4, 6, 7, 8, 9, 1, 2],
        [6, ' ', 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 6, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9],
    ]) == True


if __name__ == '__main__':
    main()
