class TicTacToe(object):
    def __init__(self, n):
        self.board = [[0 for _ in range(n)] for _ in range(n)]

    def move(self, row, col, player):
        self.board[row][col] = player
        winning_set = {(self.board[0][0], self.board[0][1], self.board[0][2]),
                       (self.board[1][0], self.board[1][1], self.board[1][2]),
                       (self.board[2][0], self.board[2][1], self.board[2][2]),
                       (self.board[0][0], self.board[1][0], self.board[2][0]),
                       (self.board[0][1], self.board[1][1], self.board[2][1]),
                       (self.board[0][2], self.board[1][2], self.board[2][2]),
                       (self.board[0][0], self.board[1][1], self.board[2][2]),
                       (self.board[0][2], self.board[1][1], self.board[2][0])}
        if (player, player, player) in winning_set:
            return 1
        return 0


def main():
    board = TicTacToe(3)
    assert board.move(0, 0, 1) == 0
    assert board.move(0, 2, 2) == 0
    assert board.move(2, 2, 1) == 0
    assert board.move(1, 1, 2) == 0
    assert board.move(2, 0, 1) == 0
    assert board.move(1, 0, 2) == 0
    assert board.move(2, 1, 1) == 1


if __name__ == '__main__':
    main()
