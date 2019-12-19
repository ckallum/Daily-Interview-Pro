def remove(parenthesis):
    result_stack = list()
    current_stack = list()
    for p in parenthesis:
        if p == "(":
            if current_stack:
                result_stack.append(p)
            current_stack.append(p)
        else:
            if len(current_stack) != 1:
                result_stack.append(p)
            current_stack.pop()

    return "".join(result_stack)


def main():
    assert remove('(())()') == "()"
    assert remove(('(()())')) == "()()"
    assert remove(('()()')) == ""


if __name__ == '__main__':
    main()
