def create_palindrome(s):
    for i in range(len(s)):
        if s[:i] + s[i + 1:] == (s[:i] + s[i + 1:])[::-1]:
            return True
    return False


def main():
    assert (create_palindrome("abcdcbea"))
    # True
    assert (create_palindrome("abccba"))
    # False
    assert not (create_palindrome("abccaa"))
    # False


if __name__ == '__main__':
    main()
