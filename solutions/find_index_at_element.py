def find_index(numbers, low, high):
    if low >= high:
        return None
    mid = (low + high) // 2
    if numbers[mid] == mid:
        return mid
    if numbers[mid] < mid:
        return find_index(numbers, mid + 1, high)
    return find_index(numbers, low, mid)


def main():
    assert find_index([-5, 1, 3, 4, 5], 0, 5) == 1
    assert not find_index([1, 2, 3, 4, 5], 0, 5)


if __name__ == '__main__':
    main()
