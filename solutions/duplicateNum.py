def bruteFind(l):
    s = set()
    res = None
    for x in l:
        if x not in s:
            s.add(x)
            res = x
    return res


def inPlaceFind(l):
    res = None
    l.sort()
    for index, x in enumerate(l[:-1:2]):
        if l[index + 1] != x:
            res = x
    return res


def main():
    nums = [4, 3, 2, 4, 1, 3, 2]
    assert bruteFind(nums) == 1
    assert inPlaceFind(nums) == 1


if __name__ == '__main__':
    main()
