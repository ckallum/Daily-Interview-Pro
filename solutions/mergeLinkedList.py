from math import inf


class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer


def brutesort(nodes):
    root = Node(None)
    headpointer = root
    nonecount = 0
    while nonecount < len(nodes):
        maxnode = (Node(inf), 0)
        for index, node in enumerate(nodes):
            if node is None:
                nonecount += 1
            elif node.val < maxnode[0].val:
                maxnode = (node, index)
        temp = Node(maxnode[0].val)
        nodes[maxnode[1]] = maxnode[0].next
        root.next = temp
        root = root.next
    return headpointer.next


def mergesort(nodes):
    if len(nodes) == 1:
        return nodes[0]
    elif len(nodes) == 2:
        return merge(nodes[0], nodes[1])
    a = mergesort(nodes[:int(len(nodes) / 2)])
    b = mergesort(nodes[int(len(nodes) / 2):])
    return merge(a, b)


def merge(a, b):
    root = Node(None)
    head = root
    while a and b:
        if a.val < b.val:
            root.next = Node(a.val)
            a = a.next
        else:
            root.next = Node(b.val)
            b = b.next
        root = root.next

    if b is None and a:
        root.next = a
    elif a is None and b:
        root.next = b

    return head.next


def main():
    a = Node(1, Node(3, Node(5)))
    b = Node(2, Node(4, Node(6)))
    c = Node(7, Node(8, Node(9)))
    print(brutesort([a, b, c]))
    print(mergesort([a, b, c]))


if __name__ == '__main__':
    main()
