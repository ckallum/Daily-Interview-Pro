from functools import reduce
from random import choice


def solver(board):
    if isComplete(board):
        return board
    empty = [(x, y) for x in range(3) for y in range(3) if board[y][x] == 0]
    col, row = choice(empty)
    for val in range(1, 10):
        board[row][col] = val
        if isValid(board):
            res = solver(board)
            if isComplete(res):
                return res
        board[row][col] = 0
    return board


def validrow(board):
    for row in board:
        values = list()
        for value in row:
            if value in values and value != 0:
                return False
            values.append(value)
    return True


def validcol(board):
    for i in range(len(board[0])):
        values = list()
        for row in board:
            if row[i] in values and row[i] != 0:
                return False
            values.append(row[i])
    return True


def validgrid(board):
    for i in range(3):
        for j in range(3):
            values = list()
            if board[i][j] in values and board[i][j] != 0:
                return False
            values.append(board[i][j])

    return True


def isValid(board):
    return validrow(board) and validcol(board) and validgrid(board)


def isComplete(board):
    return all(x != 0 for x in list(reduce(lambda x, y: x + y, board)))


def main():
    board = [[0 for _ in range(3)] for _ in range(3)]
    print(solver(board))


if __name__ == '__main__':
    main()
