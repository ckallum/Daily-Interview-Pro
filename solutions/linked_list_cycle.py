class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    if not head:
        return True
    seen = []
    current = head
    while current.val not in seen:
        if not current.next:
            return False
        seen.append(current.val)

    return True


def main():
    testHead = ListNode(4)
    node1 = ListNode(3)
    testHead.next = node1
    node2 = ListNode(2)
    node1.next = node2
    node3 = ListNode(1)
    node2.next = node3
    testTail = ListNode(0)
    node3.next = testTail
    testTail.next = node1

    assert hasCycle(testHead)  # True
