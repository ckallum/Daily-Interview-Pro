from collections import deque


def reverse_bits(num):
    stack = deque([])
    for i in range(32):
        stack.append(1) if num & (1 << i) else stack.append(0)
    print(stack)
    result = 0
    while stack:
        value = stack.popleft()
        result *= 2
        if value == 1:
            result += 1
    print(result)
    return result


def main():
    assert reverse_bits(1234) == 1260388352


if __name__ == '__main__':
    main()
