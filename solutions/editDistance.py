def distance(s1, s2):
    matrix = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = 1 + min(matrix[i][j - 1], matrix[i - 1][j], matrix[i - 1][j - 1])
    print(matrix)
    return matrix[len(s1)][len(s2)]


def main():
    assert distance("biting", "sitting") == 2
    assert distance("aabcdef", "abcdef") == 1
    assert distance("sittting", "sitting") == 1


if __name__ == '__main__':
    main()


