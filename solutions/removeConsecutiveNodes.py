class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def removeConsecutiveSumTo0(node):
    start = node
    head = Node(None)
    head.next = start
    headpointer = head
    while start:
        removed = False
        total = 0
        end = start
        increment = 0
        while end:
            total += end.value
            if total == 0:
                removed = True
                break
            else:
                end = end.next
                increment += 1
        if removed:
            temp = head.next
            for _ in range(increment):
                temp = head.next
                start = start.next
            if temp is not None:
                head.next = Node(temp.value)
                head = head.next
            else:
                head.next = None
        start = start.next
    return headpointer.next


def main():
    node = Node(10)
    node.next = Node(5)
    node.next.next = Node(-3)
    node.next.next.next = Node(-3)
    node.next.next.next.next = Node(1)
    node.next.next.next.next.next = Node(4)
    node.next.next.next.next.next.next = Node(-4)
    node = removeConsecutiveSumTo0(node)
    while node:
        print(node.value)
        node = node.next


if __name__ == '__main__':
    main()
