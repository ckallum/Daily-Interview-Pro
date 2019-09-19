class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        if not self:
            return None
        if not (self.left or self.right):
            return str(self.value)
        result = str(self.value)
        if self.left:
            result += str(self.left)
        if self.right:
            result += str(self.right)
        return result


def make_full_bst(root):
    if not root:
        return None, False
    if not (root.left or root.right):
        return root, True

    left_res = make_full_bst(root.left)
    right_res = make_full_bst(root.right)
    if not (left_res[1] and right_res[1]):
        if left_res[1]:
            return left_res[0], True
        elif right_res[1]:
            return right_res[0], True

    return Node(root.value, left_res[0], right_res[0]), True


def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.right.right = Node(4)
    root.right.left = Node(9)
    root.left.left = Node(0)
    res = make_full_bst(root)[0]
    assert str(res) == "10394"


if __name__ == '__main__':
    main()
