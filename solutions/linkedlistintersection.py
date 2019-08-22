def intersection(a, b):
    d = dict()
    while a:
        d[a.val] = a
        a = a.next
    while b:
        if b.val in d:
            return d[b.val]
        b = b.next
    return None


class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

    def prettyPrint(self):
        c = self
        while c:
            print(c.val)
            c = c.next


def main():
    a = Node(1)
    a.next = Node(2)
    a.next.next = Node(3)
    a.next.next = Node(4)
    b = Node(6)
    b.next = a.next.next
    c = intersection(a, b)
    c.prettyPrint()


if __name__ == '__main__':
    main()
