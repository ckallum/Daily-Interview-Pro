def shiftNotInPlace(numbers):
    numberofzeros = len([x for x in numbers if x == 0])
    result = [x for x in numbers if x != 0]
    result += [0 for _ in range(numberofzeros)]
    return result


def shiftInPlace(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1

    while count < len(arr):
        arr[count] = 0
        count += 1

    return arr


def main():
    assert shiftNotInPlace([0, 0, 1, 0, 3, 12, 0]) == [1, 3, 12, 0, 0, 0, 0]
    assert shiftInPlace([0, 0, 1, 0, 3, 12, 0]) == [1, 3, 12, 0, 0, 0, 0]


if __name__ == '__main__':
    main()
