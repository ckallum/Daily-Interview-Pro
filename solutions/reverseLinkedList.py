class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    # Function to print the list
    def printList(self):
        node = self
        output = ''
        while node is not None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    def recursiveReverseList(self, head):
        if not head:
            return None
        if not head.next:
            return head
        newNode = self.recursiveReverseList(head.next)
        newNode.next = head
        head.next = None
        return head

    def iterativeReverseList(self, head):
        node = head.next
        head.next = None
        while node is not None:
            temp = node.next
            node.next = head
            head = node
            node = temp


def main():
    l1 = ListNode(4)
    l2 = ListNode(3)
    l3 = ListNode(2)
    l4 = ListNode(1)
    l5 = ListNode(0)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l1.printList()
    l1.recursiveReverseList(l1)
    l5.printList()
    l5.iterativeReverseList(l5)
    l1.printList()


if __name__ == '__main__':
    main()
