def is_rotation(s1, s2):
    for i in range(len(s2)):
        s1 = s1[-1] + s1[:-1]
        if s1 == s2:
            return True
    return False


def main():
    assert not is_rotation("acb", "abc")
    assert is_rotation("abcde", "cdeab")


if __name__ == '__main__':
    main()
