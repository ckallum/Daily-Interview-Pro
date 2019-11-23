class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"value: {self.value}, left: ({self.left.__repr__()}), right: ({self.right.__repr__()})"


def filter(tree, k):
    if not tree:
        return None
    tree.left = filter(tree.left, k)
    tree.right = filter(tree.right, k)
    if tree.value == k and not (tree.left or tree.right):
        return None
    return tree


# 1
#    / \
#   1   1
#  /   /
# 2   1
def main():
    n5 = Node(2)
    n4 = Node(1)
    n3 = Node(1, n4)
    n2 = Node(1, n5)
    n1 = Node(1, n2, n3)

    print(filter(n1, 1))


if __name__ == '__main__':
    main()
#     1
#    /
#   1
#  /
# 2
# value: 1, left: (value: 1, left: (value: 2, left: (None), right: (None)), right: (None)), right: (None)
