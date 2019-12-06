import operator
from cmath import inf
from collections import defaultdict, deque


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def bfs(root):
    if not root:
        return None
    m = -inf
    max_level = 0
    current = 0
    current_level = 0
    q = deque([(root, current_level)])
    while q:
        c = q.popleft()
        if c[1] != current_level:
            current_level = c[1]
            current = c[0].value
        else:
            current += c[0].value
            if current > m:
                m = current
                max_level = current_level
        if c[0].left:
            q.append((c[0].left, current_level+1))
        if c[0].right:
            q.append((c[0].right, current_level+1))
    return max_level


def recursive_max_sum(root):
    if not root:
        return 0
    level_hash = defaultdict(int)
    helper(root, 0, level_hash)
    return max(level_hash.keys(), key=(lambda key: level_hash[key]))


def helper(root, level, level_hash):
    if not root:
        return
    level_hash[level] += root.value
    helper(root.right, level + 1, level_hash)
    helper(root.left, level + 1, level_hash)


# Fill this in.
def main():
    n3 = Node(4, Node(3), Node(2))
    n2 = Node(5, Node(4), Node(-1))
    n1 = Node(1, n2, n3)

    """
        1          Level 0 - Sum: 1
       / \
      4   5        Level 1 - Sum: 9 
     / \ / \
    3  2 4 -1      Level 2 - Sum: 8
    
    """

    assert recursive_max_sum(n1) == 1
    # Should print 1 as level 1 has the highest level sum
    assert bfs(n1) == 1


if __name__ == '__main__':
    main()
