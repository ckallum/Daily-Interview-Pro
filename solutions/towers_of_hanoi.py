"""
Proof: http://mathforum.org/library/drmath/view/55956.html

This problem is clearly a recursive problem:
    - To move n disks from one pole to another, we must first move n-1 disks to the
    helper pole and then move the n'th disk to the target pole. Finally, move the
    n-1 disks from the helper pole to the target pole.
    - We can see  that the process to move n disks from the source to the target
     is the same as moving n-1 disks from the source to the helper and the helper to
     the source where instead of the target pole being the target, the helper pole
     is now the target for the n-1 disks.
        -This is why we can use recursion.
    - The time complexity is O(2^n-1) as T(n) = 2*T(n-1) + 1 (one operation for
    moving the n-th disk from source to target, T(n-1) operations to move the
    n-1 disks twice: once from source to helper, once from helper to target)
    which we can expand using recurrence relations to obtain (2^n) -1

"""

def towers_of_hanoi(n, source, helper=[], target=[]):
    if n > 0:
        towers_of_hanoi(n - 1, source, target, helper)
        if source:
            target.append(source.pop())
        towers_of_hanoi(n - 1, helper, source, target)
    # print([source, target, helper])
    return source, helper, target


def main():
    assert towers_of_hanoi(4, [4, 3, 2, 1]) == ([], [], [4, 3, 2, 1])


if __name__ == '__main__':
    main()
