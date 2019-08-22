class Node(object):
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

    def __repr__(self):
        return self.val


def deepest(node, count=1):
    if not node:
        return None
    if not node.left and not node.right:
        return node.val, count

    leftcount = count
    rightcount = count
    leftvalue = ""
    rightvalue = ""
    if node.left:
        leftvalue, leftcount = deepest(node.left, count+1)
    if node.right:
        rightvalue, rightcount = deepest(node.right, count+1)

    return (leftvalue, leftcount) if leftcount > rightcount else (rightvalue, rightcount)


def main():
    root = Node('a')
    root.left = Node('b')
    root.left.left = Node('d')
    root.right = Node('c')
    print(deepest(root))


if __name__ == '__main__':
    main()
