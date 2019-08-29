def sort_colours(colours):
    left = 0
    right = len(colours) - 1
    while left < right:
        if colours[left] != 0 and colours[right] == 0:
            temp = colours[right]
            colours[right] = colours[left]
            colours[left] = temp
        else:
            if colours[right] != 0:
                right -= 1
            if colours[left] == 0:
                left += 1
    right = len(colours) - 1
    while left < right:
        print(colours)
        print(colours[left], colours[right])
        if colours[left] != 1 and colours[right] == 1:
            temp = colours[right]
            colours[right] = colours[left]
            colours[left] = temp
        else:
            if colours[right] != 1:
                right -= 1
            if colours[left] == 1:
                left += 1
    return colours


def main():
    assert sort_colours([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]
    assert sort_colours([0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]) == [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]


if __name__ == '__main__':
    main()
