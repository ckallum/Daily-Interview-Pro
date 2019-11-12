def has_character_map(str1, str2):
    character_map = dict()
    for i in range(len(str1)):
        if str1[i] not in character_map:
            if str2[2] not in character_map.values():
                character_map[str1[i]] = str2[i]
            else:
                return False
        else:
            if character_map[str1[i]] != str2[i]:
                return False
    return True


def main():
    assert (has_character_map('abc', 'def'))
    # True
    assert not (has_character_map('aac', 'def'))


if __name__ == '__main__':
    main()
