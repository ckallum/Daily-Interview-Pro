class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = []


def is_symmetrical(root):
    return find_symmetry(root, root)


def find_symmetry(root1, root2):
    if not (root1 or root2):
        return True
    if not (root1 and root2):
        return False
    if root1.value == root2.value:
        if len(root1.children) == len(root2.children):
            i = 0
            j = len(root1.children)-1
            res = True
            while i < len(root1.children) and j > -1:
                res = res and find_symmetry(root1.children[i], root2.children[j])
                if not res:
                    return False
                i += 1
                j -= 1
    return True


def main():
    root = Node(1)
    node2 = Node(2)
    node22 = Node(2)
    root.children.extend([node2, node22])
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node2.children.extend([node3, node4, node5])
    node22.children.extend([node5, node4, node3])
    assert is_symmetrical(root)


if __name__ == '__main__':
    main()



