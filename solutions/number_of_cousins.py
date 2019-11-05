from collections import deque


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


"""
1. find parent of node and its level
2. traverse tree and append all children at that level
    - if node is parent return None
"""


def find_level(root, val, parent, level):
    if not root:
        return None
    if root.value == val:
        return parent, level

    right = find_level(root.right, val, root, level + 1)
    left = find_level(root.right, val, root, level + 1)
    return right if right else left


def get_cousins(root, val, parent, height):
    result = []
    if not root:
        return []
    if root.value == parent.value:
        return []
    if height == 0:
        return [root.value]
    result.extend(get_cousins(root.right, val, parent, height - 1))
    result.extend(get_cousins(root.left, val, parent, height - 1))
    print(result)
    return result


def count_cousins(root, val):
    parent, height = find_level(root, val, None, 0)
    return get_cousins(root, val, parent, height)


def main():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right = Node(3)
    root.right.right = Node(5)
    assert (count_cousins(root, 5)) == [6, 4]


if __name__ == '__main__':
    main()
