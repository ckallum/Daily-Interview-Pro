class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(root, k, floor=None, ceiling=None):
    if root is None:
        return None
    if root.value >= k:
        ceiling = root.value
    if root.value <= k:
        floor = root.value

    if root.left:
        leftCeiling = findCeilingFloor(root.left, k, floor, ceiling)[1]
        if ceiling is not None:
            ceiling = min(leftCeiling, ceiling)
        else:
            ceiling = leftCeiling
        leftFloor = findCeilingFloor(root.left, k, floor, ceiling)[0]
        if floor is not None:
            floor = max(floor, leftFloor)
        else:
            floor = leftFloor
    if root.right:
        rightCeiling = findCeilingFloor(root.right, k, floor, ceiling)[1]
        if ceiling is not None:
            ceiling = min(rightCeiling, ceiling)
        else:
            ceiling = rightCeiling
        rightFloor = findCeilingFloor(root.right, k, floor, ceiling)[0]
        if floor is not None:
            floor = max(floor, rightFloor)
        else:
            floor = rightFloor

    return floor, ceiling


def main():
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.right.right = Node(30)
    root.right.left = Node(12)
    assert findCeilingFloor(root, 14) == (12, 15)
    r = findCeilingFloor(root, 14)
    print(r)

if __name__ == '__main__':
    main()
