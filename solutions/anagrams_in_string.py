from collections import Counter, defaultdict
import time


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
        length += 1
        current_map[s[index]] += 1
        while length > len(t):
            current_map[s[index - length + 1]] -= 1
            if current_map[s[index - length + 1]] == 0:
                del current_map[s[index - length + 1]]
            length -= 1
        if current_map.items() == char_map.items():
            result.append(index - length + 1)
    return result


def find_anagrams2(s, t):
    result = []

    ch_map = defaultdict(int)
    for ch in t:
        ch_map[ch] += 1

    for idx in range(len(s)):
        ch = s[idx]

        if idx >= len(t):
            old_ch = s[idx - len(t)]
            ch_map[old_ch] += 1
            if ch_map[old_ch] == 0:
                del ch_map[old_ch]

        ch_map[ch] -= 1
        if ch_map[ch] == 0:
            del ch_map[ch]

        if idx + 1 >= len(t) and len(ch_map) == 0:
            result.append(idx - len(t) + 1)

    return result


def main():
    start_time = time.time()
    assert (nminusklogn('acdbacdacb', 'abc')) == [3, 7]
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    assert (find_anagrams('acdbacdacb', 'abc')) == [3, 7]
    print("--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    assert (find_anagrams2('acdbacdacb', 'abc')) == [3, 7]
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
