class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.parent = None
        self.val = val


def lowestCommonAncestor(root, a, b):
    if not root:
        return False, None
    if root.val == a or root.val == b:
        return root

    res1 = lowestCommonAncestor(root.left, a, b)
    res2 = lowestCommonAncestor(root.right, a, b)
    if res1[0] and res2[0]:
        return True, root
    return res1 if res1 else res2


def main():
    #   a
    #  / \
    # b   c
    #    / \
    #   d*  e*
    root = TreeNode('a')
    root.left = TreeNode('b')
    root.left.parent = root
    root.right = TreeNode('c')
    root.right.parent = root
    a = root.right.left = TreeNode('d')
    root.right.left.parent = root.right
    b = root.right.right = TreeNode('e')
    root.right.right.parent = root.right

    assert lowestCommonAncestor(root, a, b).val == 'c'
