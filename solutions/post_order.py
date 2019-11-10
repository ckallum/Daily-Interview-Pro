class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return "(" + str(self.value) + ", " + self.left.__repr__() + ", " + self.right.__repr__() + ")"


def helper(post_order, start, end):
    if start == end:
        return None
    elif end - start == 1:
        return Node(post_order[end - 1])
    root = Node(post_order[end - 1])
    for i in range(start, end):
        if post_order[i] >= root.value:
            root.left = helper(post_order, start, i)
            root.right = helper(post_order, i, end - 1)
            break
    return root


def create_tree(post_order):
    return helper(post_order, 0, len(post_order))


def main():
    assert repr(create_tree([1, 3, 2])) == "(2, (1, None, None), (3, None, None))"


if __name__ == '__main__':
    main()
