class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"(Value: {self.value} Left: {self.left} Right: {self.right})"


def find_subtree(s, t):
    if s and not t:
        return False
    if not s:
        return True
    if s.value == t.value:
        if find_subtree(s.left, t.left) and find_subtree(s.right, t.right):
            return True
    else:
        return find_subtree(s, t.left) or find_subtree(s, t.right)


# Fill this in.
def main():
    t3 = Node(4, Node(3), Node(2))
    t2 = Node(5, Node(4), Node(-1))
    t = Node(1, t2, t3)

    s = Node(4, Node(3), Node(2))
    """
    Tree t:
        1
       / \
      4   5 
     / \ / \
    3  2 4 -1
    
    Tree s:
      4 
     / \
    3  2 
    """

    assert (find_subtree(s, t))
    # True


if __name__ == '__main__':
    main()
