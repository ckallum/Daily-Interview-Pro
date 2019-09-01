class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def tostring(self):
        # preorder traversal
        answer = str(self.key)
        if self.left:
            answer += self.left.tostring
        if self.right:
            answer += self.right.tostring
        return answer


def largest_bst_subtree(root):
    if not root:
        return None, 0, False
    if not root.left and not root.right:
        return root, 1, True

    left_res = largest_bst_subtree(root.left)
    right_res = largest_bst_subtree(root.right)

    if left_res[2] and right_res[2]:
        if root.left.key < root.key < root.right.key:
            return root, 1 + left_res[1] + right_res[1], True
    else:
        return root, max(right_res[1], left_res[1]), False


def main():
    node = TreeNode(5)
    node.left = TreeNode(6)
    node.right = TreeNode(7)
    node.left.left = TreeNode(2)
    node.right.left = TreeNode(4)
    node.right.right = TreeNode(9)
    assert largest_bst_subtree(node)[1] == 3


if __name__ == '__main__':
    main()
