from cmath import inf


def find(s, c):
    current_closest = inf
    result = [inf] * len(s)
    for index, char in enumerate(s):
        if char == c:
            current_closest = index
            result[index] = 0
        elif current_closest != inf:
            result[index] = index - current_closest
    current_closest = inf
    for index, char in reversed(list(enumerate(s))):
        if char == c:
            current_closest = index
            result[index] = 0
        elif current_closest != inf:
            result[index] = min(result[index], current_closest-index)
    print(result)
    return result


def main():
    assert find('helloworld', 'l') == [2, 1, 0, 0, 1, 2, 2, 1, 0, 1]


if __name__ == '__main__':
    main()
