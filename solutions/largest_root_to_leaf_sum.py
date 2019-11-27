from cmath import inf


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def largest_path_sum(tree):
    if not tree:
        return -inf, None
    if not (tree.left or tree.right):
        return tree.value, [tree.value]
    left = largest_path_sum(tree.left)
    right = largest_path_sum(tree.right)
    return (tree.value + left[0], [tree.value] + left[1]) if left[0] > right[0] else (
    tree.value + right[0], [tree.value] + right[1])


# Fill this in.
def main():
    tree = Node(1)
    tree.left = Node(3)
    tree.right = Node(2)
    tree.right.left = Node(4)
    tree.left.right = Node(5)
    #    1
    #  /   \
    # 3     2
    #  \   /
    #   5 4
    assert (largest_path_sum(tree))[1] == [1, 3, 5]


if __name__ == '__main__':
    main()
