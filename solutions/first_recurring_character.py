def first_recurring_char(s):
    chars = set()
    for char in s:
        if char in chars:
            return char
        chars.add(char)
    return None


def main():
    assert first_recurring_char("qwertty") == 't'
    assert not first_recurring_char("qwerty")


if __name__ == '__main__':
    main()