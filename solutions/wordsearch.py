def wordsearch(matrix, word):
    rowRes = False
    colRes = False
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == word[0]:
                if row <= len(matrix) - len(word):
                    colRes = searchCol(matrix, word, row, col)
                if col <= len(matrix[0]) - len(word):
                    rowRes = searchRow(matrix, word, row, col)
            if rowRes or colRes:
                return True
    return False


def searchRow(matrix, word, row, col):
    current = ""
    for col in matrix[row]:
        current += col
        if current == word:
            return True
    return False


def searchCol(matrix, word, row, col):
    current = ""
    for row in range(row, len(matrix)):
        current += matrix[row][col]
        print(current)
        if current == word:
            return True
    return False


def main():
    grid = [
        ['F', 'A', 'C', 'I'],
        ['O', 'B', 'Q', 'P'],
        ['A', 'N', 'O', 'B'],
        ['M', 'A', 'S', 'S']]
    grid2 = [
        ['J', 'A', 'G', 'E', 'Y'],
        ['P', 'F', 'A', 'C', 'I'],
        ['D', 'O', 'B', 'Q', 'P'],
        ['K', 'A', 'N', 'O', 'B'],
        ['N', 'M', 'A', 'S', 'S'],
        ['I', 'S', 'B', 'D', 'P']]
    assert wordsearch(grid, "FOAM") == True
    assert wordsearch(grid2, 'FOAM') == True


if __name__ == '__main__':
    main()
