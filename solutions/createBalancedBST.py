from collections import deque


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        # level-by-level pretty-printer
        nodes = deque([self])
        answer = ''
        while len(nodes):
            node = nodes.popleft()
            if not node:
                continue
            answer += str(node.value)
            nodes.append(node.left)
            nodes.append(node.right)
        return answer


def createBalancedBST(nums):
    mid = int(len(nums) / 2)
    if len(nums) == 1:
        return Node(nums[0])
    root = Node(nums[mid])
    root.left = createBalancedBST(nums[:mid])
    root.right = createBalancedBST(nums[mid + 1:])
    return root


def main():
    print(createBalancedBST([1, 2, 3, 4, 5, 6, 7]))


if __name__ == '__main__':
    main()
# 4261357
#   4
#  / \
# 2   6
# / \ / \
# 1 3 5 7
