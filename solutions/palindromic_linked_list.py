class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


def is_palindrome(node):
    if not (node and node.next):
        return True
    head = node
    current = None
    while node.next:
        if not node.next.next:
            current = node.next.val
            node.next = None
            break
        node = node.next
    if current == head.val:
        return is_palindrome(head.next)
    return False


def main():
    node = Node('a')
    node.next = Node('b')
    node.next.prev = node
    node.next.next = Node('b')
    node.next.next.prev = node.next
    node.next.next.next = Node('a')
    node.next.next.next.prev = node.next.next
    n = Node('c')
    n.next = Node('d')
    n.next.next = Node('e')
    n.next.next.next = Node('d')
    n.next.next.next.next = Node('c')
    assert is_palindrome(n)
    assert is_palindrome(node)


if __name__ == '__main__':
    main()
