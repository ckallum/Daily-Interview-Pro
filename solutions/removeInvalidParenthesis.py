from collections import deque


def count_removals(string):
    count = 0
    changes = 0
    for parentheses in string:
        if parentheses == '(':
            count += 1
        elif count > 0 and parentheses == ')':
            count -= 1
        else:
            changes += 1
    changes += count
    return changes


def main():
    assert count_removals("()())()") == 1
    assert count_removals("()())(()") == 2
    assert count_removals("()())))(()") == 4


if __name__ == '__main__':
    main()
