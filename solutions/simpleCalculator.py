from collections import deque


def eval(expression):
    res = 0
    remainingExp = deque()
    currentExp = deque()
    expression = expression.replace(" ", "")
    for exp in expression:
        if exp == ")":
            for _ in range(len(currentExp)):
                remainingExp.pop()
            while currentExp:
                val1 = currentExp.popleft()
                if val1 == '-':
                    res = -res
                    break
                op = currentExp.popleft()
                if currentExp:
                    val2 = currentExp.popleft()
                    if op == "+":
                        res += int(val1) + int(val2)
                    else:
                        res += int(val1) - int(val2)
                else:
                    if op == "+":
                        res = int(val1) + res
                    else:
                        res = int(val1) - res
            if len(remainingExp) > 1:
                currentExp.append(remainingExp.pop())
                currentExp.appendleft(remainingExp.pop())
            else:
                currentExp = remainingExp

        elif exp == "(":
            currentExp.clear()
        else:
            currentExp.append(exp)
            remainingExp.append(exp)
    print(res)
    return res


def main():
    assert eval('- (3 + ( 2 - 1 ) )') == -4
    assert eval('-((3+4)+(2-1))') == -8
    assert eval('-(-(4+5))') == 9


if __name__ == '__main__':
    main()
