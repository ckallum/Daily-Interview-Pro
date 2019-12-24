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

    def __eq__(self, other):
        return self.value == other.value and (self.left == other.left) and (self.right == other.right)


def get_subtrees(root):
    if not root:
        return []
    results = [root]
    # if root.left:
    results.extend(get_subtrees(root.left))
    # if root.right:
    results.extend(get_subtrees(root.right))
    return results


def dup_trees(root):
    results = []
    left = get_subtrees(root.left)
    right = get_subtrees(root.right)
    for node in right:
        if node in left:
            results.append([node, node])
    return results


# Fill this in.
def main():
    n3_1 = Node(3)
    n2_1 = Node(2, n3_1)
    n3_2 = Node(3)
    n2_2 = Node(2, n3_2)
    n1 = Node(1, n2_1, n2_2)
    # Looks like
    #     1
    #    / \
    #   2   2
    #  /   /
    # 3   3
    print(dup_trees(n1))
    assert repr(dup_trees(n1)) == [[(2, (3)), (2, (3))], [(3), (3)]]
    # There are two duplicate trees
    #
    #     2
    #    /
    #   3
    # and just the leaf
    # 3


if __name__ == '__main__':
    main()
