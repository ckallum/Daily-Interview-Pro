class Node:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

    def __repr__(self):
        return f"(Value: {self.value}, Left: {self.left}, Right: {self.right})"


def inorder_successor(node):
    if not node:
        return None
    if not (node.parent or node.right):
        return node
    if not node.right:
        while node.parent:
            node = node.parent
    else:
        return node.right


# Fill this in.
def main():
    tree = Node(3)
    tree.left = Node(2)
    tree.right = Node(4)
    tree.left.parent = tree
    tree.right.parent = tree
    tree.left.left = Node(1)
    tree.left.left.parent = tree.left
    tree.right.right = Node(5)
    tree.right.right.parent = tree.right
    #     3
    #    / \
    #   2   4
    #  /     \
    # 1       5
    assert (inorder_successor(tree.left)) == 3
    assert (inorder_successor(tree.right)) == 5
