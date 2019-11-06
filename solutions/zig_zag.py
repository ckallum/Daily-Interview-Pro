from collections import deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def zig_zag(node):
    # If current level is left_to_right, next level is right to left so we append in opposite order of direction we
    # are going
    next_level_queue = deque()
    current_level_queue = deque([node])
    left_to_right = True
    result = list()
    while current_level_queue:
        current = current_level_queue.pop()
        result.append(current.value)
        if left_to_right:
            if current.left:
                next_level_queue.append(current.left)
            if current.right:
                next_level_queue.append(current.right)

        else:
            if current.right:
                next_level_queue.append(current.right)
            if current.left:
                next_level_queue.append(current.left)
        if not current_level_queue:
            next_level_queue, current_level_queue = current_level_queue, next_level_queue
            left_to_right = not left_to_right
    print(result)
    return result


def main():
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n2 = Node(2, n4, n5)
    n3 = Node(3, n6, n7)
    n1 = Node(1, n2, n3)

    assert zig_zag(n1) == [1, 3, 2, 4, 5, 6, 7]


if __name__ == '__main__':
    main()
