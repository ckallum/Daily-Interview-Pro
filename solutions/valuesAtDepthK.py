class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def valuesAtHeight(root, height):
    if root is None:
        return []

    if height == 1:
        return [root.value]

    rightres = valuesAtHeight(root.right, height - 1)
    leftres = valuesAtHeight(root.left, height - 1)

    if not (rightres or leftres):
        if rightres:
            return rightres
        else:
            return leftres
    print(rightres+leftres)
    return rightres + leftres


def main():
    a = Node(1)
    a.left = Node(2)
    a.right = Node(3)
    a.left.left = Node(4)
    a.left.right = Node(5)
    a.right.right = Node(7)
    assert valuesAtHeight(a, 3) == [7, 5, 4]


if __name__ == '__main__':
    main()
