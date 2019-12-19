class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return f"({self.value}, {self.next})"


def remove_dup(lst):
    if not lst:
        return None
    current = lst.next
    if not current:
        return lst
    while current.value == lst.value:
        current = current.next
        if not current:
            break
    lst.next = remove_dup(current)
    return lst


def main():
    lst = Node(1, Node(2, Node(2, Node(3, Node(3)))))
    remove_dup(lst)
    assert repr(lst) == "(1, (2, (3, None)))"


if __name__ == '__main__':
    main()
