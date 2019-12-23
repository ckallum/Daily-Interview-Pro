import heapq


def k_closest(points, k):
    points_heap = list()
    for x, y in points:
        heapq.heappush(points_heap, ((x ** 2 + y ** 2), (x, y)))
    result = []
    for i in range(k):
        result.append(heapq.heappop(points_heap)[1])
    return result


def main():
    assert k_closest([(0, 0), (1, 2), (-3, 4), (3, 1)], 2) == [(0, 0), (1, 2)]


if __name__ == '__main__':
    main()
