import heapq


def closest_nums(nums, k, x):
    heap = []
    for num in nums:
        heapq.heappush(heap, (abs(num - x), num))
    result = []
    for _ in range(k):
        result.append(heapq.heappop(heap)[1])
    return result


# Fill this in.
def main():
    assert (closest_nums([1, 3, 7, 8, 9], 3, 5)) == [3, 7, 8]


if __name__ == '__main__':
    main()
