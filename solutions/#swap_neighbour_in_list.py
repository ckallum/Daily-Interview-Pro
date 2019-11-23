class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"{self.value}, ({self.next.__repr__()})"


def swap_every_two(llist):
    if not llist or not llist.next:
        return llist

    nn = llist.next.next
    n = llist.next
    n.next = llist
    llist.next = swap_every_two(nn)
    return n


def main():
# Fill this in.

    llist = Node(1, Node(2, Node(3, Node(4, Node(5)))))
    assert repr(swap_every_two(llist)) == "2, (1, (4, (3, (5, (None)))))"



if __name__ == '__main__':
    main()
