from collections import deque


def lookandsay(n):
    if n == 1:
        return [1]
    current = [1]
    for _ in range(2, n + 1):
        temp = list()
        count = 1
        currentval = current[0]
        for value in current[1:]:
            if value == currentval:
                count += 1
            else:
                temp.append(count)
                temp.append(currentval)
                count = 1
                currentval = value
        temp.append(count)
        temp.append(currentval)
        current = temp
    return current


def main():
    assert lookandsay(2) == [1, 1]
    assert lookandsay(3) == [2, 1]
    assert lookandsay(4) == [1, 2, 1, 1]
    assert lookandsay(5) == [1, 1, 1, 2, 2, 1]


if __name__ == '__main__':
    main()
