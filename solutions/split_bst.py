class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        if self.left and self.right:
            return f"({self.value}, {self.left}, {self.right})"
        if self.left:
            return f"({self.value}, {self.left})"
        if self.right:
            return f"({self.value}, None, {self.right})"
        return f"({self.value})"


def split_bst(bst, s):
    if not bst:
        return None, None
    if bst.value <= s:
        left, right = split_bst(bst.right, s)
        bst.right = left
        return bst, right
    else:
        left, right = split_bst(bst.left, s)
        bst.left = right
        return bst, left


# Fill this in.
def main():
    n2 = Node(2)
    n1 = Node(1, n2)

    n5 = Node(5)
    n4 = Node(4, None, n5)

    root = Node(3, n1, n4)

    print(root)
    # (3, (1, (2)), (4, None, (5)))
    # How the tree looks like
    #     3
    #   /   \
    #  1     4
    #   \     \
    #    2     5

    print(split_bst(root, 2))
    # ((1, (2)), (3, None, (4, None, (5))))
    # Split into two trees
    # 1    And   3
    #  \          \
    #   2          4
    #               \
    #                5


if __name__ == '__main__':
    main()
