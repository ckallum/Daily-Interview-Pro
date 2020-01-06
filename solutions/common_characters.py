def common_characters(words):
    char_map = set(words[0])
    for word in words:
        new_map = set()
        for c in word:
            if c in char_map:
                new_map.add(c)
        char_map = new_map
    return char_map


def main():
    assert common_characters(['google', 'facebook', 'youtube']) == {'e', 'o'}


if __name__ == '__main__':
    main()