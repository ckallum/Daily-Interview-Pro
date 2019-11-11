from copy import copy


class Node:
    def __init__(self, value, right=None):
        self.value = value
        self.next = right

    def __repr__(self):
        result = ""
        current = self
        while current:
            result+= str(current.value)
            current = current.next
        return result


def rotate(head, k):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    current = head
    current_pointer = Node(0, current)
    for _ in range(length - k-1):
        current = current.next
    new_head = current.next
    current.next = None
    temp = Node(0, new_head)
    while new_head.next:
        new_head = new_head.next
    new_head.next = current_pointer.next
    return temp.next


def main():
    root = Node(3, Node(4, Node(5, Node(6, Node(7)))))
    root2 = Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10))))))))

    assert repr(rotate(root, 3)) == "56734"
    assert repr(rotate(root2, 4)) == "789103456"


if __name__ == '__main__':
    main()
