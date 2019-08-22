def witness(heights):
    currentMax = 0
    results = dict
    count = 0
    for len, val in enumerate(heights):
        if val > currentMax:
            currentMax = val
            count += 1
    return count


def main():
    assert witness([1, 4, 3, 6, 3]) == 3


if __name__ == '__main__':
    main()
