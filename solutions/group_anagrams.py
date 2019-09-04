from functools import reduce


def group(strings):
    anagram_dict = {}
    for string in strings:
        anagram = str(sorted(string))
        if anagram not in anagram_dict:
            anagram_dict[anagram] = [string]
        else:
            anagram_dict[anagram].append(string)
    return list(anagram_dict.values())


def main():
    assert group(['abc', 'bcd', 'cba', 'cbd', 'efg']) == [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]


if __name__ == '__main__':
    main()