class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def find_height(root):
    if not root:
        return 0
    return max(find_height(root.right), find_height(root.left))+1


def is_balanced(root):
    if not root:
        return True
    right = find_height(root.right)
    left = find_height(root.left)
    if abs(right-left) <= 1:
        return is_balanced(root.right) and is_balanced(root.left)
    return False


def main():
    n4 = Node(4)
    n3 = Node(3)
    n2 = Node(2, n4)
    n1 = Node(1, n2, n3)

    assert is_balanced(n1)
    # True

    #     1
    #    /
    #   2
    #  /
    # 4
    n1 = Node(1, n2)
    assert not is_balanced(n1)
    # False


if __name__ == '__main__':
    main()