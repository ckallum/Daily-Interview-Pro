class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


def is_bst(root):

    if (root.left and root.right) is None:
        return True

    if root.left and root.left.key > root.key:
        return False
    elif root.right and root.right.key < root.key:
        return False
    else:
        return (is_bst(root.left) and is_bst(
            root.right)) if root.left.key < root.key < root.right.key else False


def main():
    a = TreeNode(5)
    a.left = TreeNode(3)
    a.right = TreeNode(7)
    a.left.left = TreeNode(1)
    a.left.right = TreeNode(4)
    a.right.left = TreeNode(6)
    assert is_bst(a)


if __name__ == '__main__':
    main()
