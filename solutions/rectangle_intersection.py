class Rectangle():
    def __init__(self, min_x=0, min_y=0, max_x=0, max_y=0):
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y


def intersection_area(rect1, rect2):
    if rect1.min_x - rect2.max_x > 0 or rect2.min_x - rect1.max_x > 0:
        return 0
    if rect1.min_y - rect2.max_y > 0 or rect2.min_y - rect1.max_y > 0:
        return 0

    x = max(rect1.min_x, rect2.min_x) - min(rect1.max_x, rect2.max_x)
    y = max(rect1.min_y, rect2.min_y) - min(rect1.max_y, rect2.max_y)
    return abs(x * y)


def main():
    rect1 = Rectangle(0, 0, 3, 2)
    rect2 = Rectangle(1, 1, 3, 3)
    rect3 = Rectangle(5, 5, 7, 7)
    assert intersection_area(rect1, rect2) == 2
    assert not intersection_area(rect1, rect3)


if __name__ == '__main__':
    main()
