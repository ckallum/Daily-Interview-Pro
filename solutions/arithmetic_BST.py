class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"

arithmetic_dict = {PLUS: lambda x, y: x + y, MINUS: lambda x, y: x - y, TIMES: lambda x, y: x * y,
                   DIVIDE: lambda x, y: x / y}


def evaluate(root):
    if not (root.left and root.right):
        return root.val

    return arithmetic_dict[root.val](evaluate(root.left), evaluate(root.right))


def main():
    tree = Node(TIMES)
    tree.left = Node(PLUS)
    tree.left.left = Node(3)
    tree.left.right = Node(2)
    tree.right = Node(PLUS)
    tree.right.left = Node(4)
    tree.right.right = Node(5)
    assert evaluate(tree) == 45


if __name__ == '__main__':
    main()
