def reverse_string(strings):
    for index, string in enumerate(strings):
        strings[index] = string[::-1]
    return strings


def main():
    assert reverse_string(["The", "black", "cat", "sat"]) == ["ehT", "kcalb", "tac", "tas"]


if __name__ == '__main__':
    main()
