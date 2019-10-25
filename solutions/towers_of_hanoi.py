def towers_of_hanoi(n, source, helper=[], target=[]):
    if n > 0:
        towers_of_hanoi(n - 1, source, target, helper)
        if source:
            target.append(source.pop())
        towers_of_hanoi(n - 1, helper, source, target)
    # print([source, target, helper])
    return source, helper, target


def main():
    assert towers_of_hanoi(4, [4, 3, 2, 1]) == ([], [], [4, 3, 2, 1])


if __name__ == '__main__':
    main()
