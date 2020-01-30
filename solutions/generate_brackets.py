def generate_brackets(n):
    result = []
    helper(result, n, "", 0, 0)
    return result


def helper(results, n, current, opened, closed):
    if n == 0 and (opened == closed):
        results.append(current)
    if n > 0:
        helper(results, n - 1, current + "(", opened + 1, closed)
    if opened > closed:
        helper(results, n, current + ")", opened, closed + 1)


def main():
    assert set(generate_brackets(3)) == {'((()))', '(()())', '(())()', '()(())', '()()()'}


if __name__ == '__main__':
    main()
