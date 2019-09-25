def recursive_solution(n):
    if n == 1:
        return 1
    if n == 0:
        return 0

    return recursive_solution(n - 1) + recursive_solution(n - 2)


def dynamic_solution(n):
    fib_dict = {0: 0, 1: 1}
    for number in range(2, n+1):
        fib_dict[number] = fib_dict[number-1] + fib_dict[number-2]
    return fib_dict[n]


def constant_space_solution(n):
    a = 1
    b = 0
    c = a+b
    for i in range(2, n+1):
        a = b
        b = c
        c = a+b
    return c


def main():
    assert recursive_solution(7) == 13
    assert dynamic_solution(7) == 13
    assert constant_space_solution(7) == 13


if __name__ == '__main__':
    main()
