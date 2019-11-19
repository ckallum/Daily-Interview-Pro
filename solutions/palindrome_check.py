from collections import Counter


def check_palindrome(string):
    char_dict = Counter(string)
    palindrome = ""
    odd_char = ""
    print(char_dict)
    for char, count in char_dict.items():
        if not (count % 2):
            palindrome += char * (count // 2)
        elif not odd_char:
            odd_char = char
            palindrome += char * (count // 2)
        else:
            return None
    return palindrome+odd_char+palindrome[::-1]


def main():
    assert check_palindrome("abcabc") == "abccba"
    assert check_palindrome("abdcabc") == "abcdcba"
    assert check_palindrome("momon") == "monom"


if __name__ == '__main__':
    main()