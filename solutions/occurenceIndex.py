def getRange(arr, target):
    indexes = (-1, -1)
    for index, x in enumerate(arr):
        if x > target:
            break
        if x == target:
            if indexes[0] == -1:
                indexes = (index, -1)
            else:
                indexes = (indexes[0], index)
    return indexes


def main():
    list1 = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
    list2 = [100, 150, 150, 153]
    list3 = [1, 2, 3, 4, 5, 6, 10]
    assert getRange(list1, 9) == (6, 8)
    assert getRange(list2, 150) == (1, 2)
    assert getRange(list3, 9) == (-1, -1)


