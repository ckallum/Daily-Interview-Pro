def is_knight_on_board(x, y, k, cache={}):
    if (x, y, k) in cache:
        return cache[(x, y, k)]
    if not (0 <= x <= 7 and 0 <= y <= 7):
        return 0
    if not k:
        return 1

    moves = valid_moves(x, y)
    probabilities = [is_knight_on_board(i, j, k - 1) for i, j in moves]
    cache[(x, y, k)] = sum(probabilities) / len(moves)
    return cache[(x, y, k)]


def valid_moves(x, y):
    return [
        (x + 1, y + 2),
        (x - 1, y + 2),
        (x + 1, y - 2),
        (x - 1, y - 2),
        (x + 2, y + 1),
        (x - 2, y + 1),
        (x + 2, y - 1),
        (x - 2, y - 1)]


def main():
    assert is_knight_on_board(0, 0, 1) == 0.25


if __name__ == '__main__':
    main()
