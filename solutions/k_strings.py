from collections import deque


def decode_string(s):
    if not s:
        return ""
    result = ""
    index = 0
    while index < len(s):
        value = s[index]
        if value.isdigit():
            times = int(value)
            closing_index = find_closing(s)
            for _ in range(times):
                result += decode_string(s[index + 2: closing_index])
            result += decode_string(s[closing_index + 1:])
            break
        if value != ']':
            result += value
        index += 1
    return result


def find_closing(string):
    parentheses_stack = list()
    for index, value in enumerate(string):
        if value == '[':
            parentheses_stack.append('x')
        elif value == ']':
            parentheses_stack.pop()
            if not parentheses_stack:
                return index

    return 0


def main():
    assert decode_string("2[a2[b]c]") == "abbcabbc"
    assert decode_string("2[a2[b]2[c]c]") == "abbcccabbccc"


if __name__ == '__main__':
    main()
