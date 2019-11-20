import heapq


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __gt__(self, other):
        return True


def closest_points(points, k, p):
    ps = []
    for point in points:
        heapq.heappush(ps, ((-(point.x-p.x) ** 2 + (point.y-p.y) ** 2), point))
        if len(ps) > k:
            heapq.heappop(ps)
    return [x[1] for x in ps]


def main():
    points = [
        Point(0, 0),
        Point(1, 1),
        Point(2, 2),
        Point(3, 3),
    ]
    print(closest_points(points, 2, Point(0, 2)))
    # [(0, 0), (1, 1)]


if __name__ == '__main__':
    main()
