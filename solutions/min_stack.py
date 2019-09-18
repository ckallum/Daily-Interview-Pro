class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min = None
        self.top = None

    def push(self, x):
        if not self.min:
            self.min = x
            self.stack.append(x)

        if x < self.min:
            if abs(self.min) != self.min:
                self.stack.append(2 * self.min + x)
            else:
                self.stack.append(-(2 * self.min + x))
            self.min = x
        else:
            self.stack.append(x)

        self.top = x

    def pop(self):
        if not self.stack:
            raise Exception("Stack underflow")

        popped = self.stack.pop()
        if popped < self.min:
            if abs(self.min) == self.min:
                self.min = (popped - self.min) * -0.5
            else:
                self.min = (popped-self.min) * 0.5
        if not self.stack:
            self.min = None
            self.top = None
        else:
            self.top = self.stack.pop()
            self.stack.append(self.top)

    def get_top(self):
        if self.top < self.min:
            return self.min
        return self.top

    def get_min(self):
        return self.min


def main():
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.get_min() == -3
    stack.pop()
    assert stack.get_top() == 0
    assert stack.get_min() == -2


if __name__ == '__main__':
    main()
