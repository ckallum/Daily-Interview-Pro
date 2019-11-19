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


def dfs(grid, i, j, word):
    if not word:
        return True
    if grid[i][j] != word[0] or len(grid) <= i < 0 or len(grid[0]) <= j< 0:
        return False
    temp = grid[i][j]
    grid[i][j] = " "
    if dfs(grid, i-1, j, word[1:]) or dfs(grid, i+1, j, word[1:]) or dfs(grid, i, j+1, word[1:]) or dfs(grid, i, j-1, word[1:]):
        return True
    grid[i][j] = temp
    return False


def search(grid, word):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == word[0] and dfs(grid, i, j, word):
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
    assert wordsearch(grid, "FOAM")
    assert wordsearch(grid2, 'FOAM')
    assert search(grid, "FOAM")


if __name__ == '__main__':
    main()
