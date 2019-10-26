from collections import defaultdict


class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def most_freq_subtree_sum(root, count_dict):
    if not root:
        return 0, max(count_dict, key=count_dict.get)
    count_dict[root.val] += 1
    if not (root.left or root.right):
        return root.val, max(count_dict, key=count_dict.get)
    left_total = most_freq_subtree_sum(root.left, count_dict)[0]
    right_total = most_freq_subtree_sum(root.right, count_dict)[0]
    r = root.val + left_total + right_total
    count_dict[r] += 1
    if root.right and root.left:
        sub_sum = root.val + root.left.val + root.right.val
        count_dict[sub_sum] += 1
    return r, max(count_dict, key=count_dict.get)


# fill this in.


def main():
    default = defaultdict(int)
    root = Node(3, Node(1, Node(1), Node(1)), Node(-3, Node(6), Node(0)))
    assert (most_freq_subtree_sum(root, default)) == (9, 3)
    r = Node(3, Node(1), Node(-3))
    assert (most_freq_subtree_sum(r, default))[1] == 1
    assert (most_freq_subtree_sum(r, default))[0] == 1


if __name__ == '__main__':
    main()
