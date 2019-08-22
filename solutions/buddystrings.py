def buddystring(a, b):
    if len(a) != len(b):
        return False

    for index1, value in enumerate(a[:-1]):
        for index2, value2 in enumerate(a[index1 + 1:], start=index1 + 1):
            swapped = swap(a, index1, index2)
            if swapped == b:
                return True
    return False


def swap(string, index1, index2):
    string = list(string)
    temp = string[index1]
    string[index1] = string[index2]
    string[index2] = temp
    return "".join(string)


def buddystring2(a, b):
    if len(a) != len(b):
        return False
    i = 0
    prev = -1
    current = -1
    count = 0
    while i < len(a):
        if a[i] != b[i]:
            count += 1
            if count > 2:
                return False
            prev = current
            current = i
        i += 1

    return count == 2 and a[prev] == b[current] and b[prev] == a[current]


def main():
    assert buddystring('aaaaaaabc', 'aaaaaaacb') == True
    assert buddystring('aaaaaabbc', 'aaaaaaacb') == False
    assert buddystring('', 'aaaaaaacb') == False
    assert buddystring('ab', 'ab') == False
    assert buddystring('aaaaaabbc', 'aaaaababc') == True
    assert buddystring('aabaaaabc', 'aaaaaabbc') == True

    assert buddystring2('aaaaaaabc', 'aaaaaaacb') == True
    assert buddystring2('aaaaaabbc', 'aaaaaaacb') == False
    assert buddystring2('', 'aaaaaaacb') == False
    assert buddystring2('ab', 'ab') == False
    assert buddystring2('aaaaaabbc', 'aaaaababc') == True
    assert buddystring2('aabaaaabc', 'aaaaaabbc') == True


if __name__ == '__main__':
    main()
