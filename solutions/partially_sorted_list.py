import heapq


def sort_partially(nums, k):
    heap = nums[:k + 1]
    heapq.heapify(heap)
    current = 0
    for remaining in nums[k+1:]:
        nums[current] = heapq.heappop(heap)
        heapq.heappush(heap, remaining)
        current += 1
    while heap:
        nums[current] = heapq.heappop(heap)
        current += 1

    return nums


def main():
    assert sort_partially([3, 2, 6, 5, 4],2) == [2, 3, 4, 5, 6]


if __name__ == '__main__':
    main()
