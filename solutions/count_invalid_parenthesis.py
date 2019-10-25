def count(parentheses):
    p_stack = []
    changes = 0
    for p in parentheses:
        if p == ")":
            if not p_stack:
                changes += 1
            else:
                p_stack.pop()
        else:
            p_stack.append(p)
    if p_stack:
        if len(p_stack) % 2:
            changes += 1+len(p_stack)//2
        else:
            changes += len(p_stack)//2
    return changes


def main():
    assert count(")(") == 2
    assert count("(())())") == 1
    assert count(")(((()(()") == 3


if __name__ == '__main__':
    main()