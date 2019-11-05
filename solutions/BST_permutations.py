class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        result = str(self.value)
        if self.left:
            result = result + str(self.left)
        if self.right:
            result = result + str(self.right)
        return result


def bst_helper(low, high):
    if low == high:
        return [None]
    results = []
    for i in range(low, high):
        left = bst_helper(low, i)
        right = bst_helper(i+1, high)
        for l in left:
            for r in right:
                results.append(Node(i, l, r))
    return results


def generate_bst(n):
    return bst_helper(1, n+1)


def main():
    nodes = generate_bst(3)
    ns = [str(x) for x in nodes]
    print(ns)
    assert ns == ["123", "132", "213", "312", "321"]


if __name__ == '__main__':
    main()

