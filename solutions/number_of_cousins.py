from collections import deque


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def count_cousins(root, val):
    queue = deque([(root, 0)])
    level_nodes = []
    level = 0
    while queue:
        current = queue.popleft()
        if current[0].value == val:
            return level_nodes + [x[0].value for x in queue if x[1] == level]
        if current[1] != level:
            level_nodes = [current[0].value]
            level = current[1]
        else:
            level_nodes.append(current[0].value)
        if current[0].left:
            queue.append((current[0].left, level + 1))
        if current[0].right:
            queue.append((current[0].right, level + 1))

    return level_nodes


def main():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right = Node(3)
    root.right.right = Node(5)
    assert (count_cousins(root, 5)) == [4, 6]


if __name__ == '__main__':
    main()
