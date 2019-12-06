from collections import Counter, defaultdict


def nminusklogn(s, t):
    k = len(t)
    result = []
    t = sorted(t)
    for i in range(0, len(s) - k + 1):
        if sorted(s[i:i + k]) == t:
            result.append(i)
    return result


def find_anagrams(s, t):
    char_map = dict(Counter(t))
    current_map = defaultdict(int)
    length = 0
    result = []
    for index in range(len(s)):
        print(dict(current_map), char_map)
        length += 1
        current_map[s[index]] += 1
        while length > len(t):
            current_map[s[index - length+1]] -= 1
            if current_map[s[index - length + 1]] == 0:
                del current_map[s[index - length+1]]
            length -= 1
        if dict(current_map) == char_map:
            result.append(index - length + 1)
    return result


def main():
    assert (nminusklogn('acdbacdacb', 'abc')) == [3, 7]
    assert (find_anagrams('acdbacdacb', 'abc')) == [3, 7]


if __name__ == '__main__':
    main()
