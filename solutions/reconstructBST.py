from collections import deque


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def represent(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            n = q.popleft()
            result += n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return result


def reconstruct(preorder, inorder):
    if not preorder:
        return None
    root = Node(preorder[0])
    index = inorder.index(root.val)
    root.left = reconstruct(preorder[1:index + 1], inorder[:index])
    root.right = reconstruct(preorder[index+1:], inorder[index + 1:])
    return root


def main():
    tree = reconstruct(['a', 'b', 'd', 'e', 'c', 'f', 'g'], ['d', 'b', 'e', 'a', 'f', 'c', 'g'])
    assert tree.represent() == "abcdefg"


if __name__ == '__main__':
    main()
