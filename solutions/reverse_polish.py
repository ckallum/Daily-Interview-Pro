def reverse_polish_eval(s):
    stack = []
    expressions = {
        "*": lambda a, b: a * b,
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: a / b
    }

    for char in s:
        if char in expressions:
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(expressions[char](num1, num2))
        else:
            stack.append(char)
    return stack.pop()


def main():
    assert reverse_polish_eval([1, 2, 3, '+', 2, '*', '-']) == 9


if __name__ == '__main__':
    main()
