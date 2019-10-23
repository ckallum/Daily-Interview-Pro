from collections import deque


class Node(object):
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None


def print_bfs(root):
    result = []
    node_list = deque()
    current = 0
    node_list.append((root, current))
    while node_list:
        temp = node_list.popleft()
        if temp[1] != current:
            result.append("break")
            current = temp[1]
        result.append(temp[0].value)
        if temp[0].left:
            node_list.append((temp[0].left, current + 1))
        if temp[0].right:
            node_list.append((temp[0].right, current + 1))
    return result


def main():
    tree = Node('a')
    tree.left = Node('b')
    tree.right = Node('c')
    tree.left.left = Node('d')
    tree.left.right = Node('e')
    tree.right.left = Node('f')
    tree.right.right = Node('g')
    assert print_bfs(tree) == ['a', 'break', 'b', 'c', 'break', 'd', 'e', 'f', 'g']


if __name__ == '__main__':
    main()
