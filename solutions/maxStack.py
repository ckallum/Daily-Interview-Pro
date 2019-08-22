from sys import maxsize


class OverFlowException(Exception):
    def __init__(self):
        self.message = "Stack overflow"

    def __str__(self):
        return self.message


class UnderFlowException(Exception):
    def __init__(self):
        self.message = "Stack underflow"

    def __str__(self):
        return self.message


class MaxStack:
    def __init__(self, size):
        self.stack = []
        self.size = 0
        self.maxLen = size
        self.m = None

    def push(self, val):
        if self.size == self.maxLen:
            try:
                raise OverFlowException()
            except OverFlowException as e:
                print(e)
        if self.size == 0:
            self.m = val
            self.size += 1
            self.stack.append(val)

        elif val > self.m:
            self.stack.append(2 * val - self.m)
            self.size += 1
            self.m = val
        else:
            self.stack.append(val)
            self.size += 1

    def pop(self):
        if self.size == 0:
            try:
                raise UnderFlowException()
            except UnderFlowException as e:
                print(e)
        val = self.stack.pop(self.size - 1)
        self.size -= 1
        if val > self.m:
            preV = 2*self.m-val
            self.m = preV

    def max(self):
        return self.m

    def __repr__(self):

        return "{}".format(", ".join(str(v) for v in self.stack))


def main():
    s = MaxStack(4)
    s.push(1)
    print(repr(s))
    s.push(2)
    print(repr(s))
    s.push(3)
    print(repr(s))
    s.push(2)
    print(repr(s))
    print(s.max())
    # 3
    s.pop()
    print(s.max())
    s.pop()
    print(s.max())


if __name__ == '__main__':
    main()
