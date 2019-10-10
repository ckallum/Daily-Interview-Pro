from cmath import inf


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def minimum_level_sum(root):
    if not root:
        return inf
    if not (root.left and root.right):
        return inf

    left_min = minimum_level_sum(root.left)
    right_min = minimum_level_sum(root.right)
    if root.left and root.right:
        return min(root.value+root.left.value+root.right.value, left_min, right_min)

    return inf


def main():
    #     10
    #    /  \
    #   2    8
    #  / \    \
    # 4   1    2
    node = Node(10)
    node.left = Node(2)
    node.right = Node(8)
    node.left.left = Node(4)
    node.left.right = Node(1)
    node.right.right = Node(2)
    print(minimum_level_sum(node))
    assert minimum_level_sum(node)== 7


if __name__ == '__main__':
    main()
