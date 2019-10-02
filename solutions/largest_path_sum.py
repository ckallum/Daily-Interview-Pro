class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_largest_sum(root):
    if not root:
        return 0

    if not (root.left or root.right):
        return root.value

    right_sum = find_largest_sum(root.right)
    left_sum = find_largest_sum(root.left)

    return max(root.value+right_sum, root.value+left_sum, right_sum, left_sum)


def main():
    root = Node(10)
    left = Node(20)
    right = Node(-25)
    left.left = Node(2)
    left.right = Node(1)
    right.right = Node(3)
    right.left = Node(4)
    root.left = left
    root.right = right
    assert find_largest_sum(root) == 32


if __name__ == '__main__':
    main()