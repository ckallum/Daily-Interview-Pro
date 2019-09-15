from collections import deque


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):

        # pre-order printing of the tree.
        result = ''
        result += str(self.val)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result


def serialise_node(node):
    if not node:
        return "#"
    return str(node.val) + serialise_node(node.left) + serialise_node(node.right)


def deserialize_node(serial):
    node_queue = list(serial)
    return deserialize(node_queue)


def deserialize(node_queue):
    if not node_queue:
        return None, None
    node_queue = deque(node_queue)
    next_val = node_queue.popleft()
    if next_val == '#':
        return None, list(node_queue)
    next_node = Node(next_val)
    result = deserialize(list(node_queue))
    next_node.left = result[0]
    node_queue = result[1]
    result = deserialize(node_queue)
    next_node.right = result[0]
    node_queue = result[1]
    return next_node, list(node_queue)


def main():
    tree = Node(1)
    tree.left = Node(3)
    tree.left.left = Node(2)
    tree.left.right = Node(5)
    tree.right = Node(4)
    tree.right.right = Node(7)
    assert serialise_node(tree) == "132##5##4#7##"
    assert str(deserialize_node(serialise_node(tree))[0]) == "132547"


if __name__ == '__main__':
    main()
