class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def print_BFS(root):
    if not root:
        return

    queue = list()
    queue.append(root)
    res = []
    while len(queue) > 0:
        res.append(queue[0].value)
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return res


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    assert print_BFS(root) == [1, 2, 3, 4, 5]


if __name__ == '__main__':
    main()
