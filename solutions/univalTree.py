class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def count_unival(root):
    if not root:
        return 0

    unival_count = count_unival(root.right) + count_unival(root.left)
    if root.right or root.left:
        if root.right and root.left:
            if root.val == root.right.val and root.val == root.left.val:
                return unival_count + 1
            else:
                return unival_count
        elif root.right and root.right.val == root.val:
            return unival_count + 1
        elif root.left.val == root.val:
            return unival_count + 1
        else:
            return unival_count

    return 1


def main():
    a = Node(0)
    a.left = Node(1)
    a.right = Node(0)
    a.right.left = Node(1)
    a.right.right = Node(0)
    a.right.left.left = Node(1)
    a.right.left.right = Node(1)
    b = Node(0)
    b.left = Node(0)
    b.left.left = Node(0)
    b.left.right = Node(0)
    assert count_unival(b) == 4
    assert count_unival(a) == 5


if __name__ == '__main__':
    main()
